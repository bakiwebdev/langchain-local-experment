# goal
# on this file we will learn how to save a prompt template than load gain localy

from langchain.prompts import PromptTemplate, load_prompt  # to load saved prompts

template = "i love this {thing}!"


prompt_template = PromptTemplate(input_variables=["thing"], template=template)

# save to JSON | YAML file and that's the only format langchain support right now
prompt_template.save("awsome_prompt.json")

# now load the saved prompt template
loaded_prompt = load_prompt("awsome_prompt.json")

# check if the prompt and loaded prompt is equal
assert prompt_template == loaded_prompt
