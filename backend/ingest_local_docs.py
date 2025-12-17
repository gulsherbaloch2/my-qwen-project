#!/usr/bin/env python3
"""
Script to ingest local documentation files instead of using a sitemap
"""

import os
import glob
from pathlib import Path
import markdown
import re
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import cohere

# Import configuration
from config import (
    COLLECTION_NAME, COHERE_API_KEY, EMBED_MODEL,
    QDRANT_URL, QDRANT_API_KEY, CHUNK_MAX_CHARS
)

# Initialize clients
cohere_client = cohere.Client(COHERE_API_KEY)

# Connect to Qdrant Cloud
qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

# Function to extract text content from markdown files, excluding frontmatter
def extract_text_from_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove frontmatter (content between --- and --- at the beginning)
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Convert markdown to plain text
    html = markdown.markdown(content)
    
    # Remove HTML tags to get plain text
    text = re.sub(r'<[^>]+>', '', html)
    
    return text

# Function to chunk documents
def chunk_text(text, max_chars=CHUNK_MAX_CHARS):
    chunks = []
    while len(text) > max_chars:
        # Find a good breaking point (sentence or paragraph boundary)
        split_pos = -1
        for pos in [text.rfind('. ', max_chars//2, max_chars), 
                    text.rfind('! ', max_chars//2, max_chars), 
                    text.rfind('? ', max_chars//2, max_chars),
                    text.rfind('\n', max_chars//2, max_chars),
                    text.rfind(' ', max_chars//2, max_chars)]:
            if pos != -1:
                split_pos = pos + 1
                break
        
        if split_pos == -1:  # If no good break found, just split at max_chars
            split_pos = max_chars
            
        chunks.append(text[:split_pos])
        text = text[split_pos:]
    
    if text:  # Add the remaining text if any
        chunks.append(text)
    
    return chunks

# Create embedding function
def embed(text):
    response = cohere_client.embed(
        model=EMBED_MODEL,
        input_type="search_document",  # Use search_document for documents
        texts=[text],
    )
    return response.embeddings[0]  # Return the first embedding

# Create collection function
def create_collection():
    print("\nCreating Qdrant collection...")
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=1024,        # Cohere embed-english-v3.0 dimension
            distance=Distance.COSINE
        )
    )

# Function to save chunk to Qdrant
def save_chunk_to_qdrant(chunk, chunk_id, source_file):
    vector = embed(chunk)

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=chunk_id,
                vector=vector,
                payload={
                    "source_file": source_file,
                    "text": chunk,
                    "chunk_id": chunk_id
                }
            )
        ]
    )

def ingest_local_docs():
    # Get all markdown files from the docs directory (now copied to root level during build)
    docs_path = os.path.join(os.path.dirname(__file__), '..', 'docs')

    md_files = glob.glob(os.path.join(docs_path, '**', '*.md'), recursive=True)
    
    print(f"Found {len(md_files)} markdown files in docs directory")
    for file in md_files:
        print(f" - {file}")
    
    # Create the collection
    create_collection()
    
    global_id = 1
    
    for file_path in md_files:
        print(f"\nProcessing: {file_path}")
        
        try:
            text = extract_text_from_md_file(file_path)
            
            if not text.strip():
                print(f"  WARNING: No text extracted from {file_path}")
                continue
            
            print(f"  Extracted text length: {len(text)} characters")
            
            chunks = chunk_text(text, CHUNK_MAX_CHARS)
            print(f"  Split into {len(chunks)} chunks")
            
            for i, chunk in enumerate(chunks):
                save_chunk_to_qdrant(chunk, global_id, file_path)
                print(f"  Saved chunk {global_id} ({len(chunk)} chars)")
                global_id += 1
                
        except Exception as e:
            print(f"  ERROR processing {file_path}: {e}")
            continue

    print(f"\nIngestion completed successfully!")
    print(f"Total chunks stored: {global_id - 1}")
    
    # Verify the collection exists and show basic stats
    try:
        collection_info = qdrant.get_collection(collection_name=COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' now has {collection_info.point_count} vectors")
    except Exception as e:
        print(f"Could not verify collection stats: {e}")


if __name__ == "__main__":
    ingest_local_docs()