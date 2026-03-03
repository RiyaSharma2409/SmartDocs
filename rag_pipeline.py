import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def create_llm():
    """
    Create Groq client using API key.
    """

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    return client


def generate_answer(client, query, retrieved_docs):
    """
    Generate grounded answer using Groq LLaMA 3.
    """

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a NumPy documentation assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "Not found in documentation." 
DO NOT give answers on your own. ONLY provide answers from the documentation. 

Rules to generate answer:
1. Generate answer in simple language for user understanding.
2. DO NOT miss out on the details.
3. Give answer ONLY from the documentation.
4. ALWAYS provide examples based on the user query for better user understanding.
5. The answer SHOULD BE Medium length, NEITHER too long NOR too brief.
6. REMEMBER the user query in case the user asks a follow up question.

CONSTRAINTS: DO NOT GIVE ANSWER IF IT IS NOT FOUND IN THE DOCUMENTATION. 

Context:
{context}

Question:
{query}

Answer:
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return completion.choices[0].message.content.strip()