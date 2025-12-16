"""Secure configuration validation for the AI Assistant Backend."""

import os


def validate_config():
    """Validate that all required environment variables are set."""
    
    required_vars = [
        "GOOGLE_API_KEY",
        "COHERE_API_KEY", 
        "QDRANT_URL",
        "QDRANT_API_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    print("All required environment variables are present")