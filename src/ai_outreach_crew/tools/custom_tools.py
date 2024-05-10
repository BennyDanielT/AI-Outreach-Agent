import os
import requests
from typing import Any
from crewai_tools import tool
from dotenv import load_dotenv

load_dotenv()


class CustomTools:

    @tool(
        "Scrape LinkedIn for people whose profile match the requirements of a job posting using the Google Programmable Search Engine"
    )
    def pse(**kwargs: Any) -> list:
        """
        Scrape LinkedIn for people whose profile match the requirements of a job posting using the Google Programmable Search Engine

        Args:
            job_description (str): The job description to match candidate profiles against.
            location (str): The location to search for candidates.

        Returns:
            list: A list of dictionaries containing candidate profile information.
        """

        # Set up Google Programmable Search Engine credentials
        api_key = os.getenv("GOOGLE_API_KEY")
        cx = os.getenv("GOOGLE_CX")

        # Define the search query
        query = f"Devops developer profiles on Linkedin"

        # Make the API request
        api_url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
        response = requests.get(api_url)

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
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

if __name__ == "__main__":
    scraper = CustomTools()
    tool = scraper.pse
    tool.run()