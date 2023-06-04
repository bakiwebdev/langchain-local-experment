# gole
# use chain in memory, atm i don't understand why thi

from dotenv import dotenv_values
from langchain.llms import OpenAI
# using chain on conversation to remember the previous messages
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

llm = OpenAI(openai_api_key=openai_api_key, temperature=0)  # setup open ai llm

conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory())  # set a chain for conversation and store it on buffer memory

conversation.predict(input="Hi there!")
# ai message
conversation.predict(
    input="I'm doing well! Just having a conversation with an AI")

# Current conversation:
# Human: Hi there!
# AI:  Hi there! It's nice to meet you. My name is AI. What's your name?
# Human: I'm doing well! Just having a conversation with an AI
# AI
