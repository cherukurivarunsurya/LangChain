from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke():
        pass


class llm(Runnable):
    ans = ["hi","hello","namaste"]
    
    def invoke(self, prompt):
        return f"{prompt}" + random.choice(llm.ans)
    

    
class Prompttest:

    def __init__(self, prompt: str, input_variables: list[str]):
        self.prompt = prompt
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.prompt.format(**input_dict)
    

prompt = Prompttest(
    prompt="hello whats the is {topic}?" ,
    input_variables=["topic"]
)

res_prompt = prompt.format({"topic": "lancgchain"})

llm = llm()

res = llm.invoke(res_prompt)

print(res)

