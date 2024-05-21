import os
import requests
from typing import Any
from crewai_tools import tool
from dotenv import load_dotenv
import json
import smtplib
from email.mime.text import MIMEText

load_dotenv(override=True)


# class CustomTools:


@tool(
    "Scrape LinkedIn for people whose profile match the requirements of a job posting using the Google Programmable Search Engine and return the details of the people."
)
def pse(location: str, skills: str, **kwargs: Any) -> list:
    """
    Scrape LinkedIn for people whose profile match the requirements of a job posting using the Google Programmable Search Engine

    Args:
        location (str): The location to search for candidates.
        skills (str): The skills to match against candidate profiles.

    Returns:
        list: A list of dictionaries containing candidate profile information.
    """

    # Set up Google Programmable Search Engine credentials
    api_key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("GOOGLE_CX")

    # Define the search query
    query = f'site:ca.linkedin.com/in ("{location}") AND ({skills})'

    # Make the API request
    api_url = (
        f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    )
    response = requests.get(api_url)
    # site:ca.linkedin.com/in ("Calgary * Canada") AND (Java AND Hibernate) AND (Spring OR MySQL)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        results = []
        for item in data["items"]:
            result = {
                "title": item["title"],
                "link": item["link"],
                "snippet": item["snippet"],
            }
            results.append(result)
        print(f"Found {len(results)} results")
        print(results)
        return results
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# @tool(
#     "Send personalized Emails to target individuals whose profiles match the job requirements"
# )
def send_emails(json_data, location: str, role: str, organization: str):
    """
    Send personalized emails to target individuals whose profiles match the job requirements

    Args:
        json_data (str): JSON data containing the job requirements
        location (str): Location of the job
        role (str): Role of the job
        organization (str): Organization name

    Returns:
        str: Success message
    """
    # Load JSON data
    data = json.loads(json_data)
    password = os.getenv("EMAIL_PASSWORD")

    # SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "bd12bendan28@gmail.com"
    smtp_password = password

    # Create SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Iterate over individuals and send emails
    for individual in data["individuals"]:
        name = individual["name"]
        email = individual["email"]

        # Create email message
        msg = MIMEText(
            f"Dear {name},\n\nThis is a test email.\n\nBest regards,\nNick Fury"
        )
        msg["Subject"] = "Job Opportunity at Avengers Inc."
        msg["From"] = smtp_username
        msg["To"] = email

        # Send email
        server.send_message(msg)
        print(f"Email sent to: {name} ({email})")

    # Close SMTP connection
    server.quit()
    return {"status_code": 200, "message": "success"}


# Example JSON data
json_data = """
{
  "individuals": [
    {
      "name": "Benny Daniel",
      "email": "benny28dany@gmail.com"
    },
    {
      "name": "Maverick Morales",
      "email": "benny28dany@gmail.com"
    }
  ]
}
"""

# Call the function with JSON data
send_emails(json_data, "Toronto", "DevOps Developer", "PolicyMe")


# if __name__ == "__main__":
#     scraper = CustomTools()
#     tool = scraper.pse
#     tool.run()
