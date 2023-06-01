# goal
# by defult prompt template validate the input value, on this file code we will see how to escape the validatoin part

from langchain.prompts import PromptTemplate

template = "i love this {thing}!"


# prompt_template = PromptTemplate(input_variables=[
#                                  "thing", "subject"], template=template)  # error due to extra variable

prompt_template2 = PromptTemplate(
    input_variables=["thing", "subject"], template=template, validate_template=False)  # No error

print(prompt_template2.format(thing="framework"))
# -> i love this framework!
