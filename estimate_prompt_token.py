# to estimate prompt token we need to install tiktoken
# pip install tiktoken

from dotenv import dotenv_values
from langchain.llms import OpenAI

env_val = dotenv_values(".env")
openai_key = env_val["openai_api_key"]

llm = OpenAI(openai_api_key=openai_key)

prompt = "Hi! How are you"

tokenSize = llm.get_num_tokens(prompt)

print(tokenSize)
