from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage
from dotenv import dotenv_values

# set up api key
env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]


llm = OpenAI(openai_api_key=openai_api_key, streaming=True, callbacks=[
             StreamingStdOutCallbackHandler()], temperature=0)
# resp = llm("write me a song about sparkling water.")

# print(resp)  # will stream the output

# print(llm("tell me a joke."))

chat = ChatOpenAI(openai_api_key=openai_api_key, streaming=True, callbacks=[
    StreamingStdOutCallbackHandler()], temperature=0)

resp = chat([HumanMessage(content="Write me a song about Ethiopia.")])

print(resp)
