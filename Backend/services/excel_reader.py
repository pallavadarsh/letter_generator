import pandas as pd
from io import BytesIO

def parse_excel_file(file_bytes: bytes):
    df = pd.read_csv(BytesIO(file_bytes))  # If you switch to Excel, use pd.read_excel\
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df.to_dict(orient="records")
