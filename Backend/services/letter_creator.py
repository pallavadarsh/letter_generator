import requests

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_letter(details: dict) -> str:
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

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to generate letter: {e}")
        return "An error occurred while generating the letter."

def summarize_report(report_data: dict) -> str:
    report_text = "\n".join([f"{key.capitalize().replace('_', ' ')}: {value}" for key, value in report_data.items() if value])

    prompt = f"""
    Please provide a clear and concise summary of the following police report details. 
    The summary should capture key facts like names, dates, accident locations, causes, 
    responsible parties, vehicles, insurance info, and any important medical or legal details. 
    Present it in a well-structured and informative way.

    Report Details:
    \"\"\"
    {report_text}
    \"\"\"
    """

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant skilled at summarizing accident reports."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to summarize report: {e}")
        return "An error occurred while summarizing the report."
