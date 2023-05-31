# gole combine agents with chat model
from langchain.agents import load_tools  # import load tool
from langchain.agents import initialize_agent  # import init agent
from langchain.agents import AgentType  # import agent type
from langchain.chat_models import ChatOpenAI  # chat model from open ai
# open ai llm why? because some tool need llm inorder to run
from langchain.llms import OpenAI
from dotenv import dotenv_values  # load env file
import os

env_val = dotenv_values(".env")  # env path
openai_api_key = env_val["openai_api_key"]
# serpapi = env_val["SERPAPI_API_KEY"]

# you should insert it manually here
os.environ["SERPAPI_API_KEY"] = "your_serpapi_key"

# load the chat language model
chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)

# load llm and agent tools
tool_names = ["serpapi", "llm-math"]  # note llm-math need llm
llm = OpenAI(openai_api_key=openai_api_key, temperature=0)

tools = load_tools(tool_names, llm)

# init agents (tools, llms and agent type)
agent = initialize_agent(
    tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# run agent with prompt

agent.run("Who is Biruk Endris and what is his current age ?")
