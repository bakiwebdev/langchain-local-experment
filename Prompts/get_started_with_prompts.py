# goal
# talk about what is prompt and prompt template


# Prompt is a text string ("template") that can take in a set of parameters from the end user
# Prompt template may contain
#   instruction to the language model
#   a set of few shot examples to help the language model generate a better response
#   a question to the language model

from langchain.prompts import PromptTemplate

template = """
I Want you to act as a naming consultant for new companies.
What is a good name for a company that makes {product}?
"""

prompt = PromptTemplate(input_variables=["product"], template=template)

prompt.format(product="Car")
# prints
# -> I Want you to act as a naming consultant for new companies.
# -> What is a good name for a company that makes Car?
