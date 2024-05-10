import json
import os
import requests
from typing import Any
from crewai_tools import tool
from dotenv import load_dotenv

load_dotenv()


class CustomTools:

    @tool(
        "Scrape LinkedIn for people whose profile match the requirements of a job posting using the proxycurl API"
    )
    def scrape_linkedin(**kwargs: Any) -> list:
        """
        Scrape LinkedIn for people whose profile match the requirements of a job posting

        Args:
            job_description (str): The job description to match candidate profiles against.
            location (str): The location to search for candidates.

        Returns:
            list: A list of dictionaries containing candidate profile information.
        """

        # Set up proxycurl API credentials
        api_key = os.getenv("PROXYCURL_API_KEY")
        api_url = "https://nubela.co/proxycurl/api/v2"

        # Define the API endpoint and parameters
        endpoint = "/search/person"
        params = {
            "country": "CA",
            "skills": ["Langchain", "python", "docker"],
        }

        # Make the API request
        headers = {"Authorization": "Bearer " + api_key}
        response = requests.get(f"{api_url}{endpoint}", headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            with open("./documents/linkedin_data.json", "w") as f:
                json.dump(data, f)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []


if __name__ == "__main__":
    instance = CustomTools()
    tool = instance.scrape_linkedin
    tool.run()
