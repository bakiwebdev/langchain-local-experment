import os  # we use this to import enviromental variable
from langchain.llms import OpenAI  # llm from openai
from langchain.chains import LLMChain  # import chains
from langchain.prompts import PromptTemplate  # import prompt template
from dotenv import dotenv_values  # import dotenv

# load agent and it's classes
from langchain.agents import load_tools  # to load agent
from langchain.agents import initialize_agent    # to initialize agent
from langchain.agents import AgentType  # to defind the agen type

env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]
# serpapi = env_val["SERPAPI_API_KEY"]
os.environ["SERPAPI_API_KEY"] = "your_serpapi_key"

# load the llm
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)

# load some tools also pass the llm
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# initalize agent with tools, llms and agent type
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# test the agent
agent.run(
    "how should i improve a my linkedin profile https://www.linkedin.com/in/bakiwebdev/")
