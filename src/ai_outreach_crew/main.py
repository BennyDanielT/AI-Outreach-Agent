import os
from dotenv import load_dotenv

load_dotenv()

from ai_outreach_crew.crew import RecruitmentCrew


def run():
    inputs = {
        "organization": "Rimot.io.",
        "website": "https://bluegrid.energy/",
        "role": "DevOps Developer",
        "description": """Rimot is looking for a DevOps developer. Work will be on Tyscript and Python codebases. CICD, piepline development and deployment.""",
        "location": "Halifax, Nova Scotia",
        "start_date": "June 30, 2024",
        "category": "Full-Time",
    }

    RecruitmentCrew().recruitment_crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
