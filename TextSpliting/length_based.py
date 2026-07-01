from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\VARUN SURYA\OneDrive\Desktop\langchain\DocumentsLoader\Books\warnock_camelot.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

# as we are using the splitter on documents, we will use the split_documents method instead of split_text
result = splitter.split_documents(docs)

print(type(result))