from groq import Groq
import os

# Set your GROQ API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def generate_letter(details: dict) -> str:
    """Generate a personalized legal letter using GROQ LLM based on accident details."""
    
    prompt = f"""
    Write a professional and empathetic legal letter for the following accident case:

    Name: {details.get('Name', 'Client')}
    Date: {details.get('Date', 'N/A')}
    Location: {details.get('Location', 'Unknown')}
    Cause: {details.get('Cause', 'Unknown')}
    Responsible Party: {details.get('Responsible Party', 'Unknown')}
    Vehicle: {details.get('Vehicle', 'Unknown')}
    Insurance: {details.get('Insurance', 'Unknown')}
    Address: {details.get('Address', '')}
    Description: {details.get('Description', '')}

    The letter should address the client by name, acknowledge the accident and circumstances, mention the responsible party and insurance, describe the incident concisely, and offer legal and medical assistance. Close professionally with your law firm.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


def generate_letters(reports: list) -> list:
    """Generate legal letters for multiple accident cases and return as a list."""
    return [generate_letter(details) for details in reports]


def summarize_report(text: str) -> str:
    """Generate a more detailed and descriptive summary using Groq's LLaMA 3 model."""
    prompt = f"""
    Please provide a clear and concise summary of the following police report text. 
    The summary should capture key facts like names, dates, accident locations, causes, 
    responsible parties, vehicles, insurance info, and any important medical or legal details. 
    Present it in a well-structured and informative way.

    Report Text:
    \"\"\"
    {text}
    \"\"\"
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant skilled at summarizing accident reports."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()