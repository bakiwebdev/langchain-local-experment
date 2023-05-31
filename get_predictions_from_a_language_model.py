from langchain.llms import OpenAI
from dotenv import dotenv_values

env_val = dotenv_values(".env")

openai_key = env_val["openai_api_key"]

llm = OpenAI(model="text-ada-001", temperature="0.6",
             openai_api_key=openai_key)

prompt = "Tell me a joke"

print(llm(prompt))
