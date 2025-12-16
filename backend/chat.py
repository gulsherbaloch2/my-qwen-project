import requests
import xml.etree.ElementTree as ET
import trafilatura
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import secure configuration
from secure_config import (
    SITEMAP_URL, COLLECTION_NAME, COHERE_API_KEY, EMBED_MODEL,
    QDRANT_URL, QDRANT_API_KEY, SEARCH_TOP_K, MAX_TOKENS_RESPONSE, TEMPERATURE
)
from config import CHAT_MODEL

# Initialize clients
cohere_client = cohere.Client(COHERE_API_KEY)

# Connect to Qdrant Cloud
qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)


def embed_text(text):
    """Generate embedding for a text using Cohere"""
    response = cohere_client.embed(
        model=EMBED_MODEL,
        input_type="search_query",  # Use search_query for queries
        texts=[text],
    )
    return response.embeddings[0]  # Return the first embedding


def query_qdrant(query_text, top_k=SEARCH_TOP_K):
    """Query the Qdrant collection for similar content"""
    query_embedding = embed_text(query_text)

    response = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k
    )

    # Return the points list from the response
    return response.points


def format_response(query, results):
    """Format the search results into a coherent response"""
    if not results:
        return "I couldn't find any relevant information to answer your question."

    # Extract the most relevant chunks
    context_parts = []
    for result in results:
        context_parts.append(result.payload["text"])

    # Combine context and generate a response
    context = "\n\n".join(context_parts[:3])  # Use top 3 results

    # Generate a response using Cohere
    response = cohere_client.chat(
        model=CHAT_MODEL,
        message=f"Based on the following context, please answer the question. If the context doesn't contain enough information to answer the question, please say so.\n\nContext: {context}\n\nQuestion: {query}",
        temperature=TEMPERATURE
    )

    return response.text.strip()


def chat_with_humanoid_ai():
    """Main chat function to interact with the humanoid AI book"""
    print("Welcome to the Humanoid AI Book Assistant!")
    print("Ask me anything about the Humanoid AI book content.")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Thank you for using the Humanoid AI Book Assistant. Goodbye!")
            break

        if not user_input:
            print("Please ask a question.")
            continue

        try:
            print("Searching for relevant information...")
            search_results = query_qdrant(user_input, top_k=SEARCH_TOP_K)
            response = format_response(user_input, search_results)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Sorry, I encountered an error: {str(e)}")
            print("Please try asking your question again.\n")


if __name__ == "__main__":
    chat_with_humanoid_ai()