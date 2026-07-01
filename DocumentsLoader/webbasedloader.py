from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    web_path= 'https://en.wikipedia.org/wiki/Main_Page'
)

doc = loader.load()

print(doc[0].page_content)
