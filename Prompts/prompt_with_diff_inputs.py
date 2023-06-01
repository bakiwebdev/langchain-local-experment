# goal
# show prompt with different input size

from langchain.prompts import PromptTemplate

template_with_no_input = "Tell me a joke"
prompt_with_no_input = PromptTemplate(
    input_variables=[], template=template_with_no_input)

print(prompt_with_no_input.format())
# -> Tell me a joke


template_with_one_input = "Tell me a joke about {subject}"
prompt_with_one_input = PromptTemplate(
    input_variables=["subject"], template=template_with_one_input)
print(prompt_with_one_input.format(subject="programmer"))
# -> Tell me a joke about programmer


template_with_multiple_input = "Tell me a {adjective} joke about {content}."
prompt_with_multiple_input = PromptTemplate(
    input_variables=["adjective", "content"], template=template_with_multiple_input)

print(prompt_with_multiple_input.format(adjective="funny", content="chicken"))
# -> Tell me a funny joke about chicken
