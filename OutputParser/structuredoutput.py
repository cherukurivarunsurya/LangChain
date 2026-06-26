from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0.7)

#using ResponseSchema we can define the structure of the output we want from the model. 
#we need to create a ResponseSchema class for each field we want in the output. with name and description
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

# we created schema so we will build a parser with that schema using for_response_schemas method of StructuredOutputParser. 
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)