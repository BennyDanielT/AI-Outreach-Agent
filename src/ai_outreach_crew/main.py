import os
from dotenv import load_dotenv

load_dotenv()

from ai_outreach_crew.crew import RecruitmentCrew


def run():
    inputs = {
        "organization": "AstraZeneca India Pvt. Ltd.",
        "role": "DevOps Developer",
        "description": "The AstraZeneca Global Technology center in Chennai, India requires a DevOps developer to manage infrastructure in the cloud using AWS. We are looking for someone who has expertise in infrastructure as code, AWS Services, Containerization technology and Python. The ideal candidate can work on AWS CDK, Terraform and Kubernetes to spin up clusters and deploy production-grade applications on the cloud. We need someone with at least 4 years of experience. Proficiency in Java and Typescript codebases are a plus. AWS Certifications are a plus.",
        "location": "Halifax, Nova Scotia",
        "start_date": "June 20, 2024",
        "category": "Full-Time",
    }

    RecruitmentCrew().recruitment_crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
