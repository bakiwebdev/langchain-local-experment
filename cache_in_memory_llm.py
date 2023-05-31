import langchain
from langchain.cache import InMemoryCache  # load in memory catch
from langchain.llms import OpenAI
from dotenv import dotenv_values

# set up api key
env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]


llm = OpenAI(openai_api_key=openai_api_key,
             model="text-davinci-002", n=2, best_of=2)

langchain.llm_cache = InMemoryCache()

# %%time
print(llm("tell me joke"))

print(llm("how do use say how are you ?"))
