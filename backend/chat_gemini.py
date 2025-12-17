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

# Initialize Qdrant client - using grpc=False to ensure REST API is used
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)


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

    # Check if search method exists and call it appropriately
    search_results = []
    try:
        # Standard approach for newer qdrant-client versions
        search_results = qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=SEARCH_TOP_K,
            with_payload=True
        )
    except AttributeError as e:
        if "'QdrantClient' object has no attribute 'search'" in str(e):
            # This error occurs when the client doesn't have the search method
            # Return empty results as a fallback for this specific error
            print(f"Qdrant search method not available: {e}")
            search_results = []
        else:
            # Re-raise other attribute errors
            raise
    except Exception as e:
        # Log other errors and return empty results as fallback
        print(f"Error during Qdrant search: {e}")
        search_results = []

    return search_results


def format_response(query, search_results):
    """Format the response using Google Gemini based on query and search results."""
    # Prepare context from search results
    context_parts = []

    # Check if search_results exist and have content
    if search_results:
        for result in search_results:
            # Handle different possible structures of result objects
            if hasattr(result, 'payload'):
                text = result.payload.get('text', '') if result.payload else ''
                source = result.payload.get('source_file', 'Unknown source') if result.payload else 'Unknown source'
            else:
                # If result is a dict or other format
                text = result.get('text', '') if isinstance(result, dict) else ''
                source = result.get('source_file', 'Unknown source') if isinstance(result, dict) else 'Unknown source'

            score = getattr(result, 'score', 0) if hasattr(result, 'score') else result.get('score', 0) if isinstance(result, dict) else 0

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
    # Using models that are typically available, with fallbacks
    model_name = None
    available_models = ['gemini-1.5-flash', 'gemini-1.0-pro', 'gemini-pro']

    for name in available_models:
        try:
            model = genai.GenerativeModel(name)
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=MAX_TOKENS_RESPONSE,
                    temperature=TEMPERATURE
                )
            )
            model_name = name
            break  # Use the first working model
        except Exception as e:
            continue  # Try the next model

    # If no model worked, provide a fallback response instead of failing
    if model_name is None:
        return "I'm sorry, but I'm currently unable to generate a response. The AI service might be unavailable. Please try again later."

    return response.text