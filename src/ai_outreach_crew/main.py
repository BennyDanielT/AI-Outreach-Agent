import os
from dotenv import load_dotenv
from ai_outreach_crew.crew import RecruitmentCrew
from datetime import date

load_dotenv()


def run():
    current_date = date.today().strftime("%Y-%m-%d")

    inputs = {
        "organization": "Rimot.io.",
        "website": "https://bluegrid.energy/",
        "role": "DevOps Developer",
        "description": """Rimot io  is looking for a DevOps developer. Work will be on Tyscript and Python codebases. CICD, piepline development and deployment.""",
        "location": "Halifax, Nova Scotia",
        "start_date": "June 30, 2024",
        "category": "Full-Time",
        "current_date": current_date,
    }

    RecruitmentCrew().recruitment_crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
