from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0.7)

chat_history =[
    SystemMessage(content="You are a math teacher")
]

while True:
    user_input = input("user:")
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    if user_input.lower() == "exit":
        break
    chat_history.append(AIMessage(content=response.content))
    print(response.content)

print(chat_history)


    

