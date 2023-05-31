# goal
# this file shows you the type of language models and it's different
# 1) LLM and 2) ChatModel

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import dotenv_values

# set up api key
env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

# setup models
llm = OpenAI(openai_api_key=openai_api_key)
chat_model = ChatOpenAI(openai_api_key=openai_api_key)

llm.predict("say Hi!")  # output => Hi There!

chat_model.predict("say Hi!")  # output => HI! How can i assist you today?
