import langchain
from gptcache import cache
from gptcache.manager.factory import manager_factory
from gptcache.processor.pre import get_prompt
from langchain.cache import GPTCache
import hashlib
from langchain.llms import OpenAI
from dotenv import dotenv_values

# set up api key
env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]


llm = OpenAI(openai_api_key=openai_api_key,
             model="text-davinci-002", n=2, best_of=2)


def get_hashed_name(name):
    return hashlib.sha256(name.encode()).hexdigest()


def init_gptcache(cache_obj: cache, llm: str):
    hashed_llm = get_hashed_name(llm)
    cache_obj.init(
        pre_embedding_func=get_prompt,
        data_manager=manager_factory(
            manager="map", data_dir=f"map_cache_{hashed_llm}"),
    )


langchain.llm_cache = GPTCache(init_gptcache)

print(llm("Tell me a joke"))


print(llm("Tell me a joke about me"))
