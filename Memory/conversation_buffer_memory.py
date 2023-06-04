# gole
# it's just a wrapper around ChatMessageHistory that extracts the message in a variable

# import Conversation Buffer Memory
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("Hi!")  # add on chat_memory
memory.chat_memory.add_ai_message("Hello, How can i help you ?")

# load memory and extract it as a string
print(memory.load_memory_variables({}))
# => {'history': 'Human: Hi!\nAI: Hello, How can i help you ?'}

# enables to sent mesage as a list
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("Hi!")
memory.chat_memory.add_ai_message("Hello, How can i help you ?")

# load memory and extract as a list of messages
print(memory.load_memory_variables({}))
# {'history': [HumanMessage(content='Hi!', additional_kwargs={}, example=False), AIMessage(content='Hello, How can i help you ?', additional_kwargs={}, example=False)]}
