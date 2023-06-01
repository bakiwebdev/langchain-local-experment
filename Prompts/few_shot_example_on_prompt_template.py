# goal
#!!not sure but not working
# add few shot examples on prompt template for better response

from langchain.prompts import PromptTemplate, FewShotPromptTemplate

# first create a list of few shot examples.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"}
]

# create template
template = """
Word: {word}
Antonym: {anotonym}
"""

# format template
prompt_template = PromptTemplate(
    input_variables=["word", "anotonym"], template=template, validate_template=False)

# create few shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    # import examples
    examples=examples,
    # import template
    example_prompt=prompt_template,
    # (prefix) some text before the example
    prefix="Give the antonym of every input\n",
    # (suffix) somet text after the example
    suffix="word: {input}\nantonym: ",
    # example separater for each parameter
    example_separator="\n"  # separate by new line
)


print(few_shot_prompt(input="big"))
