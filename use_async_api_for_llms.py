# goal
# simple program to use llm in asyc way

import time  # to tell how long it take to execute
import asyncio  # library to use async/await
from langchain.llms import OpenAI
from dotenv import dotenv_values

# set up api key
env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

# seriall func


def generate_serially():
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)
    for _ in range(10):
        resp = llm.generate(["Hello, how are you?"])
        print(resp.generations[0][0].text)


async def async_generate(llm):
    resp = await llm.agenerate(["Hello, how are you?"])
    print(resp.generations[0][0].text)


async def generate_concurrently():
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)
    tasks = [async_generate(llm) for _ in range(10)]
    await asyncio.gather(*tasks)


s = time.perf_counter()
# If running this outside of Jupyter, use asyncio.run(generate_concurrently())
asyncio.run(generate_concurrently())
# await generate_concurrently()
elapsed = time.perf_counter() - s
print('\033[1m' +
      f"Concurrent executed in {elapsed:0.2f} seconds." + '\033[0m')

s = time.perf_counter()
generate_serially()
elapsed = time.perf_counter() - s
print('\033[1m' + f"Serial executed in {elapsed:0.2f} seconds." + '\033[0m')
