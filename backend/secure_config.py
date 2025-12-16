import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Site Configuration
SITEMAP_URL = os.getenv("SITEMAP_URL", "https://my-docusaurus-site-two.vercel.app/sitemap.xml")

# Database Configuration
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "humanoid_ai_book")

# Cohere Configuration
COHERE_API_KEY = os.getenv("COHERE_API_KEY")  # Should be set in environment

EMBED_MODEL = os.getenv("EMBED_MODEL", "embed-english-v3.0")

# Qdrant Configuration
QDRANT_URL = os.getenv("QDRANT_URL")  # Should be set in environment
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")  # Should be set in environment

# Google API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Should be set in environment

# Processing Configuration
CHUNK_MAX_CHARS = int(os.getenv("CHUNK_MAX_CHARS", "1200"))
SEARCH_TOP_K = int(os.getenv("SEARCH_TOP_K", "5"))
MAX_TOKENS_RESPONSE = int(os.getenv("MAX_TOKENS_RESPONSE", "500"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))

# Chat Model Configuration
CHAT_MODEL = os.getenv("CHAT_MODEL", "command-r-plus")

def validate_config():
    """Validate that all required API keys and configuration values are set."""
    errors = []

    if not COHERE_API_KEY:
        errors.append("COHERE_API_KEY is not set")
    if not QDRANT_URL:
        errors.append("QDRANT_URL is not set")
    # For local Qdrant instances, QDRANT_API_KEY can be empty
    # Only check if using a cloud instance with a non-default URL
    if not GOOGLE_API_KEY:
        errors.append("GOOGLE_API_KEY is not set")

    if errors:
        raise ValueError(f"Configuration errors: {'; '.join(errors)}")

    print("[OK] All required API keys and configuration values are set")

if __name__ == "__main__":
    # Test the validation
    validate_config()
    print("Configuration validation passed!")