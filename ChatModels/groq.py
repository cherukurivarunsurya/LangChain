from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0.7) 

result = model.invoke("can you explain langchain?")

print(result.content)