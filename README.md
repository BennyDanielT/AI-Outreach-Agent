# AI-Outreach-Agent

This project aims to leverage large language models (LLMs) to automate the process of identifying potential candidates on LinkedIn and sending personalized invitation messages. The goal is to streamline the outreach process and increase the chances of successful connections and engagements.

# How do I install and test the application?

## Prerequisites

- pip
- python >= 3.12
- poetry
- groq API key (You can also use Ollama to serve models locally and utilize them but groq is significantly faster)

1. Clone the repository with `git clone https://github.com/BennyDanielT/AI-Outreach-Agent.git`
2. Ensure you have poetry installed in your machine, if not, execute `pip install poetry`
3. Install the dependencies with `poetry install`
4. Obtain your groq api key on [groq console](https://console.groq.com/keys)
5. Run the application with `poetry run ai_outreach_crew`
6. View the results in the terminal
7. Modify the inputs in `main.py` to test different example
