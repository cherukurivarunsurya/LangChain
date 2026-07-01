from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path= r'C:\Users\VARUN SURYA\OneDrive\Desktop\langchain\DocumentsLoader\Books',
    glob="*.pdf",               #glob=  "**/*" - all files in that folder and subfolders glob="**/*.pdf"
    loader_cls=PyPDFLoader      #glob="**/*.pdf" - all pdf files in that folder and subfolders(smae for other file types also)
                                #glob="*.pdf" - all pdf files in that folder only(same fro other file types also)
)

doc = loader.load()

print(len(doc))

print(doc[0].page_content)

