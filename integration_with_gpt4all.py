from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """Question: {question}
Answer: Let's think step by step."""  # bulid template

prompt = PromptTemplate(template=template, input_variables=["question"])

# specify modle
# a model i download from GPT4All
local_path = "./models/ggml-gpt4all-j-v1.3-groovy.bin"

callbacks = [StreamingStdOutCallbackHandler()]

llm = GPT4All(model=local_path, backend="gptj",
              callbacks=callbacks, verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "tell me about ethiopian history"

llm_chain.run(question)
