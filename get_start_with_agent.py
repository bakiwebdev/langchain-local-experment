from langchain.agents import load_tools  # load tools when init agent
from langchain.agents import initialize_agent  # to init the agent
from langchain.agents import AgentType  # to define agents
from langchain.llms import OpenAI
from dotenv import dotenv_values
import os

env_val = dotenv_values('.env')  # load env file
openai_api_key = env_val["openai_api_key"]  # get env file for open api key
os.environ["SERPAPI_API_KEY"] = "your_serpapi_key"

llm = OpenAI(openai_api_key=openai_api_key, temperature=0)  # load open ai

# load tools (tools(array) & llm)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# init agent (tool, lmm,  type of agent we want to use, and additonal parameter like verbose)
agent = initialize_agent(
    tools, llm, aget=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# run agent
agent.run("Who is Abrham Aforki and how long he lived")
