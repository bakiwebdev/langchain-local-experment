# from dotenv import dotenv_values
# from langchain.llms import OpenAI

# env_val = dotenv_values(".env")
# openai_key = env_val["openai_api_key"]

# llm = OpenAI(openai_api_key=openai_key)

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(input_variables=[
                        "product"], template="What is a good name for a company that makes {product}?")

# let see how this works using .format(key=value)

print(prompt.format(product="Colorfull Socks"))
