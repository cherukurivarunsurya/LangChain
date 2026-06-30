from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_groq import ChatGroq
load_dotenv()

prompt1 = PromptTemplate(
    template= "write a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatGroq(model = "openai/gpt-oss-120b") 

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})


prompt3 = PromptTemplate(
    template='from content of {tweet} and {linkedin} genrate we a content idea for blog',
    input_variables=['tweet','linkedin']
)


chain = parallel_chain |prompt3 | model | parser

print(chain.invoke({'topic':'AI'}))


