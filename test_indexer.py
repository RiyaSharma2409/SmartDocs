from data_loader import extract_numpy_docs
from indexer import create_documents

raw_docs = extract_numpy_docs()
split_docs = create_documents(raw_docs)

print("Total Chunks:", len(split_docs))
print("\nSample Chunk:\n")
print(split_docs[0].page_content[:500])