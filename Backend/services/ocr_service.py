import pytesseract
from PIL import Image
import pandas as pd
import io

def process_file(file_path: str) -> dict:
    """Process a file: Extract text from an image or read CSV file."""
    try:
        # Set the path for Tesseract OCR
        pytesseract.pytesseract.tesseract_cmd = r"C:/Users/HP/anaconda3/envs/project/Scripts/pytesseract.exe"

        image = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(image)
        return {"message": "Image processed successfully", "text": extracted_text}
    
    except Exception as e:
        return {"error": str(e)}