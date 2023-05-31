# goal make use of template by using message prompt template

from langchain.chat_models import ChatOpenAI  # import chat model
from langchain.prompts.chat import (
    ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)  # import chat prompt template from propmts.chat

from dotenv import dotenv_values

env_val = dotenv_values(".env")
openai_api_key = env_val["openai_api_key"]

chat = ChatOpenAI(openai_api_key=openai_api_key,
                  temperature=0)  # setup chat model

# system template
# accept input_language & output_language
template = "You are a helpful assistant that translaates {input_language} to {output_language}."
system_message_prompts = SystemMessagePromptTemplate.from_template(template)
# human template
human_template = "{text}"
human_message_prompts = HumanMessagePromptTemplate.from_template(
    human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompts, human_message_prompts])  # construc prompts

# get a chat compleation from the formated messages
res = chat(chat_prompt.format_prompt(input_language="English",
                                     output_language="Amharic", text="we love this world").to_messages())

print(res)
