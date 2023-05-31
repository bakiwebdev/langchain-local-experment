# goal
# show how prompt template work and how to expost the formated prompt

from langchain.prompts import PromptTemplate, ChatPromptTemplate

string_prompt = PromptTemplate.from_template("tell me a joke about {subject}")

chat_prompt = ChatPromptTemplate.from_template(
    "tell me a joke about {subject}")


# format_template will expost the constructed prompt

string_prompt_value = string_prompt.format_prompt(subject="soccer")

chat_prompt_value = chat_prompt.format_prompt(subject="soccer")

print(string_prompt_value.to_string())  # tell me a joke about soccer
print(chat_prompt_value.to_string())  # Human: tell me a joke about soccer
