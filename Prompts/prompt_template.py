from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "What is a good name for a company that makes {product}?"
    )
#this is same as above but using the from_template method instead of the constructor
#here we are manually creating a prompt with a template and input variables. 
prompt_main = PromptTemplate (
   template="What is a good name for a company that makes {product}?",
    input_variables=["product"],
    partial_variables={"product": "colorful socks"}
    ) 

res = prompt.invoke({"product": "colorful socks"})

print(res)
#op - text='What is a good name for a company that makes colorful socks?'

print(prompt_main.invoke())
#op - text='What is a good name for a company that makes colorful socks?'
