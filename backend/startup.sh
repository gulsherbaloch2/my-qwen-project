#!/bin/sh
set -e

echo "Starting document ingestion process..."
cd /app  # Ensure we're in the right directory

# Check if docs directory exists
if [ ! -d "./docs" ]; then
    echo "ERROR: docs directory does not exist!"
    ls -la  # List current directory for debugging
    exit 1
fi

echo "Found docs directory, proceeding with ingestion..."
python backend/main.py ingest
echo "Document ingestion process completed."

echo "Starting API server..."
exec uvicorn backend.api:app --host 0.0.0.0 --port 8000