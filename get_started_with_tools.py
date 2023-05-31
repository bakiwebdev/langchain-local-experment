# load tool class
from langchain.agents import load_tools

# tool names in arrow
tool_names = ["tool1", "tool2"]

# load tools
tool = load_tools(tool_names)

# if a tool require llm to start use this method
llm = ...  # use any llms
tools_with_llms = load_tools(tool_names, llms=llm)
