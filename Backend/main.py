import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.ocr_service import process_file
from services.nlp_service import extract_accident_details, summarize_report
from services.letter_service import generate_letters
import os
import pandas as pd

app = FastAPI()


# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow only specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/process_report")
def process_report(file: UploadFile = File(...)):
    try:
        # Save Temp File
        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as buffer:
            buffer.write(file.file.read())

        if temp_file.lower().endswith((".png", ".jpg", ".jpeg")):
            # Extract Text from Image/PDF
            extracted_text = process_file(temp_file)
            extracted_text = extracted_text.get("text", "")

            if not extracted_text:
                raise HTTPException(status_code=400, detail="No text extracted from the image.")    

            # Run AI-based NLP for Details Extraction
            details = extract_accident_details(extracted_text)

        elif temp_file.lower().endswith(".csv"): 
            df = pd.read_csv(temp_file)
            details = df.to_dict(orient="records")
            extracted_text = " ".join(df.astype(str).values.flatten()) 

        else:
            return {"error": "Unsupported file type"}


        # Generate Legal Letter
        letter = generate_letters(details)

        # Summarize Long Reports
        summary = summarize_report(extracted_text)

        os.remove(temp_file)

        return {"details": details, "letter": letter, "summary": summary}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":

    # Uncomment the line below to run the FastAPI server
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)