# SmartDocs
SmartDocs is a RAG-based technical documentation assistant that delivers source-grounded answers from Python library docs. It uses semantic chunking, OpenAI embeddings, and FAISS vector search for retrieval, with custom prompt guardrails, source citation, and top-k evaluation to minimize hallucinations and improve reliability.

# Features
1. Semantic document chunking with overlap
2. Dense embedding generation (OpenAI embeddings)
3. FAISS-based vector similarity retrieval
4. Custom prompt guardrails for hallucination control
5. Source citation for answer transparency
6. Top-k retrieval evaluation and failure analysis

# Architecture
Documentation → Chunking → Embeddings → FAISS Vector Store
User Query → Embedding → Top-K Retrieval → LLM → Answer + Sources

SmartDocs follows a standard RAG pipeline:
1. Documentation is split into semantically meaningful chunks.
2. Each chunk is converted into a dense embedding.
3. Embeddings are stored in a FAISS vector database.
4. At query time, the system retrieves the most relevant chunks.
5. The LLM generates an answer strictly grounded in retrieved context.

# Tech Stack
1. Python
2. LangChain
3. OpenAI (LLM + Embeddings)
4. FAISS (Vector Search)

# Evaluation
SmartDocs was evaluated using a manually curated test set of documentation-related queries.

Metrics considered:
1. Retrieval hit-rate (Top-k relevance)
2. Faithfulness to retrieved context
3. Hallucination detection via strict prompting

Failure cases were analyzed to study:
1. Chunk size sensitivity
2. Top-k tradeoffs
3. Context noise vs precision

# Hallucination Mitigation
The system uses controlled prompting:
1. Answers must strictly rely on retrieved context.
2. If information is not present, the model returns: "Not found in documentation."
3. Source chunks are returned alongside responses.

# Motivation
Static documentation can be difficult to navigate. SmartDocs transforms structured documentation into an interactive, context-aware assistant while preserving factual accuracy through retrieval grounding.
