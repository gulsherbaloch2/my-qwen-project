"""Configuration file for the AI Assistant Backend."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Qdrant Configuration
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Collection name for Qdrant
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "curriculum_chunks")

# Chunking settings
CHUNK_MAX_CHARS = int(os.getenv("CHUNK_MAX_CHARS", "1200"))

# Embedding model
EMBED_MODEL = os.getenv("EMBED_MODEL", "embed-english-v3.0")

# Search settings
SEARCH_TOP_K = int(os.getenv("SEARCH_TOP_K", "5"))

# Response settings
MAX_TOKENS_RESPONSE = int(os.getenv("MAX_TOKENS_RESPONSE", "500"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))

# Validate required environment variables
REQUIRED_VARS = [
    "GOOGLE_API_KEY",
    "COHERE_API_KEY", 
    "QDRANT_URL",
    "QDRANT_API_KEY"
]

missing_vars = [var for var in REQUIRED_VARS if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")