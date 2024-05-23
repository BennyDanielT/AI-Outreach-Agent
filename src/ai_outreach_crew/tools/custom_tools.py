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
def pse(location: str, skills: list[str], **kwargs: Any) -> list:
    """
    Scrape LinkedIn for people whose profile match the requirements of a job posting using the Google Programmable Search Engine

    Args:
        location (str): The location to search for candidates.
        skills (List[str]): A list of skills to match against candidate profiles.

    Returns:
        List[dict]: A list of dictionaries containing candidate profile information, including title, link, email, and snippet.
    """

    # Set up Google Programmable Search Engine credentials
    api_key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("GOOGLE_CX")

    skills_query = " OR ".join(f'"{skill}"' for skill in skills)

    # Define the search query
    query = f'site:ca.linkedin.com/in ("{location}") AND ({skills_query}) email "@gmail.com"'
    print(query)

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
        # print(data)
        for item in data["items"]:
            result = {
                "title": item["title"],
                "link": item["link"],
                # "email": item["email"],
                "snippet": item["snippet"],
            }
            results.append(result)
        print(f"Found {len(results)} results")
        print(results)
        return results
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


@tool(
    "Send personalized Emails to target individuals whose profiles match the job requirements"
)
def send_emails(json_data: list[dict], location: str, role: str, organization: str):
    """
    Send personalized emails to target individuals whose profiles match the job requirements

    Args:
        json_data (str): JSON data containing the job requirements
        location (str): Location of the job
        role (str): Role of the job
        organization (str): Organization name

    Returns:
        dict: Dictionary containing status code and message
    """
    try:
        # Load JSON data
        data = json.loads(json_data)

        # SMTP server details
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = os.getenv("EMAIL_ID")
        smtp_password = os.getenv("EMAIL_PASSWORD")

        # Create SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Iterate over individuals and send emails
        for individual in data:
            name = individual["name"]
            email = individual["email"]

            # Create email message
            msg = MIMEText(
                f"Dear {name},\n\nI am writing to regarding an opening in {location} at {organization}.\n\nBest regards,\n{organization}"
            )
            msg["Subject"] = f"{role} - Job Opportunity at {organization}"
            msg["From"] = smtp_username
            msg["To"] = email

            # Send email
            server.send_message(msg)
            print(f"Email sent to: {name} ({email})")

        # Close SMTP connection
        server.quit()
        return {"status_code": 200, "message": "Emails sent successfully"}
    except Exception as e:
        return {"status_code": 500, "message": f"Error: {str(e)}"}


# pse(
#     "Halifax, Nova Scotia",
#     ["TypeScript", "Python", "DevOps", "CICD", "Docker", "Kubernetes"],
# )

# Example JSON data
# json_data = """
# [
#     {
#         "name": "Sai Sandeep Mutyala",
#         "url": "https://ca.linkedin.com/in/sandeepmutyala",
#         "location": "Halifax, Nova Scotia",
#         "experience": "",
#         "skills": "TypeScript, Python, Ruby, HTML, CSS",
#         "email": "benny28dany@gmail.com"
#     },
#     {
#         "name": "Henri Vandersleyen",
#         "url": "https://ca.linkedin.com/in/henri-vandersleyen-a25a8312b",
#         "location": "Halifax, Nova Scotia, Canada",
#         "experience": "May 2012 - Dec 2013 1 year 8 months",
#         "skills": "Software Development Life Cycle SDLC and Project Management",
#         "email": "benny28dany@gmail.com"
#     },
#     {
#         "name": "Huang Zheng",
#         "url": "https://ca.linkedin.com/in/huang-zheng-425948121",
#         "location": "Halifax, Nova Scotia",
#         "experience": "6 years of Backend development experience",
#         "skills": "Python, Software Development Life Cycle SDLC and Project Management",
#         "email": "benny28dany@gmail.com"
#     },
#     {
#         "name": "Aditya Mahale",
#         "url": "https://ca.linkedin.com/in/aditya-mahale",
#         "location": "Halifax, Nova Scotia",
#         "experience": "Senior Software Engineer with seven years of development experience",
#         "skills": "JavaScript, TypeScript, Python, Java, C, SQL",
#         "email": "benny28dany@gmail.com"
#     },
#     {
#         "name": "Son Pham",
#         "url": "https://ca.linkedin.com/in/son-pham-623937222",
#         "location": "Halifax, Nova Scotia, Canada",
#         "experience": "Halifax, Nova Scotia, Canada",
#         "skills": "Software Engineer",
#         "email": "benny28dany@gmail.com"
#     }
# ]
# """

# Call the function with JSON data
# send_emails(json_data, "Toronto", "DevOps Developer", "PolicyMe")


# if __name__ == "__main__":
#     scraper = CustomTools()
#     tool = scraper.pse
#     tool.run()
