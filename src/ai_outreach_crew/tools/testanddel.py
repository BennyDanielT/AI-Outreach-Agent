import os
import requests
from typing import Any
from crewai_tools import tool
from dotenv import load_dotenv
import json
import smtplib
from email.mime.text import MIMEText

load_dotenv(override=True)


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
