# gole
# ChatMessageHistory is a core utility class , it's lightweigth wrapper wich exposes convenience methods for saving human messages, ai messages and fetch them all.

from dotenv import dotenv_values
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message("Hi!")
history.add_ai_message("Hello, How can i help you ?")

print(history.messages)

# [HumanMessage(content='Hi!', additional_kwargs={}, example=False), AIMessage(content='Hello, How can i help you', additional_kwargs={}, example=False)]
