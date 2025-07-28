from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

agent=Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    description="You are a helpful web assistant. Answer any question using DuckDuckGo search and answer based on the expert from relevant sources",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("What is Nvidia currently investing on",stream=True)