#!/bin/sh
set -e

echo "Starting document ingestion process..."
python backend/main.py ingest || echo "Document ingestion failed, but continuing with API server startup..."

echo "Starting API server..."
exec uvicorn backend.api:app --host 0.0.0.0 --port 8000