import requests

# --- Configuration ---
GROQ_API_KEY = ""  # TODO: Replace with your actual Groq API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# HTTP headers required for Groq API
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# --- Function: Generate Legal Letter ---
def generate_letter(details: dict) -> str:
    """
    Generates a professional legal letter for a given accident case using Groq LLM.
    Accepts a dictionary of case details and returns the generated letter as a string.
    """
    # Constructing the prompt using user-provided accident details
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

    The letter should address the client by name, acknowledge the accident and circumstances,
    mention the responsible party and insurance, describe the incident concisely,
    and offer legal and medical assistance. Close professionally with your law firm.
    """

    # Payload to send to Groq API
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7  # Controls randomness/creativity
    }

    try:
        # Send POST request to Groq API
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raises an error for non-2xx responses

        # Extract and return the generated letter
        return response.json()['choices'][0]['message']['content'].strip()

    except requests.exceptions.RequestException as e:
        # Print and return error fallback in case of failure
        print(f"[ERROR] Failed to generate letter: {e}")
        return "An error occurred while generating the letter."


# --- Function: Summarize Report ---
def summarize_report(report_data: dict) -> str:
    """
    Generates a clear, concise summary of accident report data using Groq LLM.
    Accepts a dictionary of report fields and returns a structured summary string.
    """

    # Convert dict fields into a readable text block
    report_text = "\n".join([
        f"{key.capitalize().replace('_', ' ')}: {value}"
        for key, value in report_data.items() if value
    ])

    # Construct prompt for summarization
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

    # Request payload for Groq summarization
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant skilled at summarizing accident reports."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        # Send POST request to Groq API
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        # Extract and return summary
        return response.json()['choices'][0]['message']['content'].strip()

    except requests.exceptions.RequestException as e:
        # Log and return error fallback
        print(f"[ERROR] Failed to summarize report: {e}")
        return "An error occurred while summarizing the report."
