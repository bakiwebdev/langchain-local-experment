from langchain.llms import OpenAI  # import OpenAi class from langchain llms
from dotenv import dotenv_values

env_val = dotenv_values(".env")

openai_key = env_val["openai_api_key"]

# setup llms modle and parameter
llm = OpenAI(model="text-ada-001", temperature=0.9,
             n=2, best_of=2, openai_api_key=openai_key)

# generate prompts
propmt = "tell me a joke"

print(llm(propmt))
