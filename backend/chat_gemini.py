"""Chat functionality using Google Gemini and Qdrant for retrieval."""

import os
import google.generativeai as genai
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, SearchParams
from qdrant_client.http import models
from config import (
    GOOGLE_API_KEY, COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY,
    COLLECTION_NAME, SEARCH_TOP_K, MAX_TOKENS_RESPONSE, TEMPERATURE
)
import cohere


# Initialize Cohere client for embeddings
cohere_client = cohere.Client(COHERE_API_KEY)

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Qdrant client
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)


def embed_query(query):
    """Generate embeddings for the input query using Cohere."""
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query",
        texts=[query],
    )
    return response.embeddings[0]


def query_qdrant(query_text):
    """Query the Qdrant database for similar documents to the query."""
    query_embedding = embed_query(query_text)
    
    search_results = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=SEARCH_TOP_K,
        with_payload=True
    )
    
    return search_results


def format_response(query, search_results):
    """Format the response using Google Gemini based on query and search results."""
    # Prepare context from search results
    context_parts = []
    for result in search_results:
        text = result.payload.get('text', '')
        source = result.payload.get('source_file', 'Unknown source')
        score = result.score
        
        context_parts.append(f"Source: {source}\nRelevance Score: {score}\nContent: {text}\n---")
    
    combined_context = "\n".join(context_parts)
    
    # Create a prompt for Gemini that includes the context
    prompt = f"""
    You are an AI assistant for the Physical AI & Humanoid Robotics Curriculum.
    Answer the user's query based on the provided context from the curriculum.
    If the context doesn't contain relevant information, politely say that you don't have enough information to answer the query.
    
    Context:
    {combined_context}
    
    User Query:
    {query}
    
    Response:
    """
    
    # Use the Gemini model to generate a response
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=MAX_TOKENS_RESPONSE,
            temperature=TEMPERATURE
        )
    )
    
    return response.text