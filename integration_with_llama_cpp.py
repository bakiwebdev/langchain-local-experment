from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

# specify modle
local_path = "./models/ggml-gpt4all-j-v1.3-groovy.bin"

# template
template = """Question: {question}
Answer: Let's work this out in a step by step way to be sure we have the right answer."""

# prompt
prompt = PromptTemplate(template=template, input_variables=["question"])

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

n_gpu_layers = 20

n_batch = 200

llm = LlamaCpp(
    model_path=local_path,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    callback_manager=callback_manager,
    verbose=True
)

llm_chain = LLMChain(prompt=prompt, llm=llm)


queston = "Write me a song about Ethiopia"

llm_chain.run(queston)
