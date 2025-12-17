FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY . .

# Copy docs from the docusaurus site
COPY ../my-docusaurus-site/docs ./docs

EXPOSE 8000

# Run document ingestion first, then start the API server
CMD ["sh", "-c", "python backend/main.py ingest && uvicorn api:app --host 0.0.0.0 --port 8000"]