from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool

from tools.custom_tools import pse

web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()
# scraper_tool = ScrapeWebsiteTool(
#     website_url="""site:ca.linkedin.com/in ("Calgary * Canada") AND (Java AND Hibernate) AND (Spring OR MySQL)"""
# )
pse_tool = pse


@CrewBase
class RecruitmentCrew:
    """Recruitment Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    website = tasks_config["craft_job_ad_task"]["website"]
    print(f"Website: {website}")

    def __init__(self):
        # self.LLM = Ollama(model="llama3")
        self.LLM = ChatGroq(temperature=0.3, model_name="llama3-8b-8192")

    #################################################################
    # Agents:
    #################################################################

    @crew
    def recruitment_crew(self) -> Crew:
        """Crew for recruiting individuals for opening(s) in an organization"""
        return Crew(
            agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=2
        )
