from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_documents(raw_texts):
    """
    Convert raw text strings into LangChain Document objects,
    then split them into smaller chunks.
    """

    # Step 1: Convert each string into a Document object
    docs = [Document(page_content=text) for text in raw_texts]

    # Step 2: Create a text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Step 3: Split documents into smaller chunks
    split_docs = splitter.split_documents(docs)

    return split_docs