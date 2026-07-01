from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b")
                 
loader = TextLoader(
    r"C:\Users\VARUN SURYA\OneDrive\Desktop\langchain\DocumentsLoader\text.txt"
)

doc = loader.load()

#type - list
print(type(doc))

#type - Document object 
print(type(doc[0]))

prompt = PromptTemplate(
    template="summarize the following text in 5 points: {text}", 
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"text": doc[0].page_content}))




