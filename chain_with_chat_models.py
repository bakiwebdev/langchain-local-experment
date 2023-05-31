# goal using chain together with chat models

from langchain.chat_models import ChatOpenAI  # import chat model
from langchain import LLMChain  # import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)  # import chat model
from dotenv import dotenv_values

env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)  # setup models

# setup system prompt template
template = "You are a helpful assitant that translate {input_language} to {output_language}"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# set up human prompt template
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# set up chat prompt together by combining system and human prompt
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

# build chain takes (llm and prompt)
chain = LLMChain(llm=chat, prompt=chat_prompt)

# run chain
res = chain.run(input_language="English",
                output_language="Dutch", text="i want to buy something")

print(res)
