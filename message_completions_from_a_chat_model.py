# get chat completions by by passing one or more messages to the chat model

from langchain.chat_models import ChatOpenAI  # import chat model
from langchain.schema import (
    AIMessage, HumanMessage, SystemMessage)  # type of message
from dotenv import dotenv_values

env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

chat = ChatOpenAI(openai_api_key=openai_api_key,
                  temperature=0)  # init chat model

# get complition by passing a single message.
single_res = chat([HumanMessage(
    content="Translate this sentence from English to Amharic. I love programing.")])

# print(single_res)

# multiple messages
messages = [
    SystemMessage(
        content="Your are a help full assistant that translates English to Amharic"),
    HumanMessage(content="whos pen is this ?")
]

multiple_message = chat(messages)

print(multiple_message)
