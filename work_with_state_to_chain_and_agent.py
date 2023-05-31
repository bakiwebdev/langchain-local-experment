# on this example we use conversational chain to remember pervious input/output
# use verbose=True to see the prompt

from langchain import OpenAI, ConversationChain
from dotenv import dotenv_values

env_val = dotenv_values('.env')  # load env file
openai_api_key = env_val["openai_api_key"]  # get env file for open api key

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)  # setup llms
# setup a conversational chain to remember and verbose ture to print the prompts
conversation = ConversationChain(llm=llm, verbose=True)
output = conversation.predict(input="Hi there!")
output = conversation.predict(
    input="I'm doing well! just having a conversation with an AI.")
print(output)
