# goal -> use memory with chains and agents to use on chat model
# keep all previous messages into a string, and keep them on their unique memory object

from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  # new to me
from dotenv import dotenv_values  # load env file

env_val = dotenv_values(".env")  # env path
openai_api_key = env_val["openai_api_key"]

# build chat prompt temmplate and adjust place holder to store previous messages
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# setup llm
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)

# setup memory
memory = ConversationBufferMemory(return_messages=True)

# setup conversation chain (meomory, propmt, llm)
conversation = ConversationChain(
    memory=memory, prompt=prompt, llm=llm)

# start conversation

conversation.predict(input="Hi there!")
conversation.predict(input="am doing good, just having fun with ai")
res = conversation.predict(input="tell me about your self")

print(res)
