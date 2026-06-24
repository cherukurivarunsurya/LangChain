from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# Examples
examples = [
    {
        "english": "Hello",
        "french": "Bonjour"
    },
    {
        "english": "Thank you",
        "french": "Merci"
    },
    {
        "english": "Good Night",
        "french": "Bonne nuit"
    }
]

# Format for each example
example_prompt = PromptTemplate(
    input_variables=["english", "french"],
    template="""  
English: {english}
French: {french}
"""
)

# Few-shot prompt
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Translate the following English words to French:",
    suffix="""
English: {word}
French:
""",
    input_variables=["word"]
)

# Generate final prompt
prompt = few_shot_prompt.invoke({
    "word": "Good Morning"
})

print(prompt)