import spacy
from transformers import pipeline
import re

# Load spaCy NLP Model
nlp = spacy.load("en_core_web_sm")

# Load Hugging Face Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

import re

def extract_accident_details(text: str) -> list:
    """Extract accident-related details from multiple police reports dynamically."""
    doc = nlp(text)
    details_list = []
    
    # Generalized regex patterns
    date_pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    vehicle_pattern = re.compile(r'([A-Z][a-z]+\s[A-Z][a-z]+)')  # Generic vehicle model pattern
    insurance_pattern = re.compile(r'([A-Z][a-zA-Z]+\sInsurance)')  # General insurance name pattern
    cause_pattern = re.compile(r'([A-Za-z\s]+accident|rear-ended|hit by a speeding vehicle|collision|crash|side-swipe|t-bone)', re.IGNORECASE)
    responsible_pattern = re.compile(r'([A-Z][a-z]+\s[A-Z][a-z]+)\s(?:caused|was responsible for) the accident', re.IGNORECASE)
    
    current_details = {
        "name": "Unknown", "date": "N/A", "location": "Unknown",
        "cause": "Unknown", "responsible_party": "Unknown", "vehicle": "Unknown",
        "insurance": "Unknown", "address": "Unknown", "description": "Unknown"
    }
    
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if current_details["name"] != "Unknown":  # New person likely indicates a new record
                details_list.append(current_details)
                current_details = {
                    "name": "Unknown", "date": "N/A", "location": "Unknown",
                    "cause": "Unknown", "responsible_party": "Unknown", "vehicle": "Unknown",
                    "insurance": "Unknown", "address": "Unknown", "description": "Unknown"
                }
            current_details["name"] = ent.text
        elif ent.label_ == "DATE" or date_pattern.match(ent.text):
            current_details["date"] = ent.text
        elif ent.label_ == "GPE":  # Geo-Political Entity (Location)
            current_details["location"] = ent.text
        elif insurance_pattern.search(ent.text):
            current_details["insurance"] = insurance_pattern.search(ent.text).group()
        elif vehicle_pattern.search(ent.text):
            current_details["vehicle"] = vehicle_pattern.search(ent.text).group()
        elif cause_pattern.search(text):
            current_details["cause"] = cause_pattern.search(text).group()
        elif responsible_pattern.search(text):
            current_details["responsible_party"] = responsible_pattern.search(text).group(1)
    
    # Append the last extracted details
    if current_details["name"] != "Unknown":
        details_list.append(current_details)
    
    return details_list



def summarize_report(text: str) -> str:
    """Generate a more detailed summary with proper description."""
    summary = summarizer(
        text, 
        max_length=300,  # Increase for more detail
        min_length=100,  # Ensure enough context
        do_sample=True,  # Allow diverse outputs
        temperature=0.7,  # Balance randomness & coherence
        top_k=50  # Consider top 50 tokens for variety
    )
    return summary[0]['summary_text']
