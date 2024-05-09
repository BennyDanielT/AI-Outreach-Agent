
import os
from typing import Any
from crewai_tools import tool


class CustomTools:

    @tool("Scrape LinkedIn for people whose profile match the requirements of a job posting")
    def scrape_linkedin(self, **kwargs: Any) -> None:
        """
        Scrape LinkedIn for people whose profile match the requirements of a job posting
        """
        
    
