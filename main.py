from data_loader import extract_numpy_docs
from indexer import create_documents
from vector_store import create_vector_store
from rag_pipeline import create_llm, generate_answer


def main():
    print("Extracting NumPy documentation...")
    raw_docs = extract_numpy_docs()

    print("Splitting documents into chunks...")
    split_docs = create_documents(raw_docs)

    print("Creating vector store...")
    vectorstore = create_vector_store(split_docs)

    print("Loading local LLM...")
    client = create_llm()

    while True:
        query = input("\nAsk a NumPy question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        retrieved_docs = vectorstore.similarity_search(query, k=3)

        answer = generate_answer(client, query, retrieved_docs)

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()