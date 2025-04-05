def generate_letter(details: dict) -> str:
    """Generate a personalized legal letter based on extracted accident details."""
    return f"""
    Dear {details.get('Name', 'Client')},

    We hope you are doing well. We understand that you were involved in an accident on {details.get('Date', 'N/A')} at {details.get('Location', 'Unknown')}.
    Based on the details provided, the incident appears to have been caused by {details.get('Cause', 'Unknown')}.

    The responsible party for the accident is identified as {details.get('Responsible Party', 'Unknown')}.
    Your vehicle ({details.get('Vehicle', 'Unknown')}) was affected in the incident, and your insurance provider ({details.get('Insurance', 'Unknown')}) may cover the damages.

    {details.get('Description', '')}

    Given these circumstances, you may have legal rights and could be eligible for compensation.
    Our legal team is here to guide you through the process and ensure that you receive the necessary support, including medical assistance and legal consultation.

    Please reach out to us at your earliest convenience to discuss the next steps.

    Best regards,  
    [Your Law Firm Name]
    """

def generate_letters(reports: list) -> list:
    """Generate legal letters for multiple accident cases and return as a list."""
    return [generate_letter(details) for details in reports]