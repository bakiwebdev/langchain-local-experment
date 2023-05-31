from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import dotenv_values

# set up env file
env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

# setup openai llm
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)

# setup prompt
prompt = PromptTemplate(input_variables=[
                        "product"], template="what is the good name for a company that makes {product}")

# now let run simple chain that will take user prompt and put in the prompt template then generate response
chain = LLMChain(llm=llm, prompt=prompt)

# run chain
res = chain.run("Colorful socks")

print(res)
