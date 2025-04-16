
from fastapi import APIRouter, UploadFile, File
from services.excel_reader import parse_excel_file
from services.letter_creator import generate_letter , summarize_report
#from services.langgraph_engine import run_agentic_workflow
from fastapi.responses import JSONResponse
from utils.send_trace import send_trace
import uuid

router = APIRouter()

@router.get("/ping")
async def ping():
    return JSONResponse(content={"message": "all is well"})

@router.post("/generate")
async def generate_letters(file: UploadFile = File(...)):
    content = await file.read()
    records = parse_excel_file(content)
    trace_id = str(uuid.uuid4())

    all_letters = []
    combined_summary = []

    for row in records:
        letter = generate_letter(row)
        summary = summarize_report(row)
        all_letters.append(letter)
        combined_summary.append(summary)

    # Run the agentic workflow and get trace URL
    await send_trace(records, trace_id, all_letters, combined_summary)

    return JSONResponse(content={
        "trace_id": trace_id,
        "summary": "\n\n".join(combined_summary),
        "letters": all_letters
    })
