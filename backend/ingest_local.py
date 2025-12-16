import requests
import xml.etree.ElementTree as ET
import trafilatura
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import cohere
from dotenv import load_dotenv
import os

# Load environment variables directly
load_dotenv()

# Import configuration values directly from environment
SITEMAP_URL = os.getenv("SITEMAP_URL", "https://my-docusaurus-site-two.vercel.app/sitemap.xml")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "physical_ai_curriculum")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBED_MODEL = os.getenv("EMBED_MODEL", "embed-english-v3.0")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "")  # Empty for local Qdrant
CHUNK_MAX_CHARS = int(os.getenv("CHUNK_MAX_CHARS", "1200"))

# Initialize clients
cohere_client = cohere.Client(COHERE_API_KEY)

# Connect to LOCAL Qdrant - explicitly without API key for local instance
qdrant = QdrantClient(
    url=QDRANT_URL,
    # Only include api_key if it's not empty (for local instance)
    **({"api_key": QDRANT_API_KEY} if QDRANT_API_KEY else {})
)

def get_all_urls(sitemap_url):
    """Extract URLs from sitemap with better error handling"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(sitemap_url, headers=headers)
        response.raise_for_status()
        # Check if the sitemap redirects to the old GitHub Pages
        if "gulsherbaloch2.github.io" in response.text:
            print("Sitemap redirects to old GitHub Pages. Using fallback URLs.")
            raise Exception("Sitemap redirects to old domain")

        xml = response.text
        root = ET.fromstring(xml)

        urls = []
        for child in root:
            loc_tag = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
            if loc_tag is not None:
                url = loc_tag.text
                # Only include URLs that contain educational content, not blog posts
                if "physical-ai-humanoid-robotics" in url or "docs" in url:
                    urls.append(url)

        print("\nFOUND EDUCATIONAL URLS:")
        for u in urls:
            print(" -", u)

        return urls
    except Exception as e:
        print(f"Error fetching or parsing sitemap: {e}")
        # Fallback to manual list of URLs if sitemap fails
        fallback_urls = [
            "https://my-docusaurus-site-two.vercel.app/docs/intro",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-1/introduction",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-1/robotic-actuators",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-1/robotic-sensors",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-2/introduction",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-2/ai-control-systems",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-2/machine-learning",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-3/introduction",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-3/kinematics",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-3/dynamics",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-4/introduction",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-4/computer-vision",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-4/sensor-fusion",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-5/introduction",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-5/imitation-learning",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-5/reinforcement-learning",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-6/introduction",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-6/safety-ethics",
            "https://my-docusaurus-site-two.vercel.app/docs/physical-ai-humanoid-robotics/module-6/social-robotics"
        ]
        print("\nUSING FALLBACK EDUCATIONAL URLS:")
        for u in fallback_urls:
            print(" -", u)
        return fallback_urls


def extract_text_from_url(url):
    """Download page and extract text with better error handling"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text
        text = trafilatura.extract(html, include_comments=False, include_formatting=False)

        if not text or len(text.strip()) < 50:  # If text is too short, try alternative extraction
            # Simple fallback: extract content between body tags
            import re
            body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
            if body_match:
                body_content = body_match.group(1)
                # Remove script and style tags
                body_content = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
                # Remove HTML tags to get plain text
                text = re.sub(r'<[^>]+>', ' ', body_content)

        if not text:
            print(f"[WARNING] No text extracted from: {url}")
            return ""

        # Clean up the text
        text = text.strip()
        if len(text) < 50:
            print(f"[WARNING] Very short text extracted from: {url} (length: {len(text)})")

        return text
    except Exception as e:
        print(f"[ERROR] Failed to extract text from {url}: {e}")
        return ""


def chunk_text(text, max_chars=1200):
    """Chunk text with better handling of sentence boundaries"""
    if not text or len(text) <= max_chars:
        return [text] if text else []

    chunks = []
    paragraphs = text.split('\n\n')  # Split by paragraph first

    current_chunk = ""
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        # If adding this paragraph would exceed the limit
        if len(current_chunk) + len(paragraph) + 2 > max_chars:  # +2 for the \n\n we're adding
            # Save the current chunk if it's not empty
            if current_chunk.strip():
                chunks.append(current_chunk.strip())

            # If the paragraph itself is longer than max_chars, split it
            if len(paragraph) > max_chars:
                # Split the long paragraph into sentences
                sentences = paragraph.split('. ')
                sentences = [s + '.' for s in sentences if s.strip()]

                temp_chunk = ""
                for sentence in sentences:
                    if len(temp_chunk) + len(sentence) + 2 > max_chars:
                        if temp_chunk.strip():
                            chunks.append(temp_chunk.strip())
                        temp_chunk = sentence
                    else:
                        if temp_chunk:
                            temp_chunk += " " + sentence
                        else:
                            temp_chunk = sentence

                if temp_chunk.strip():
                    current_chunk = temp_chunk
            else:
                # Start a new chunk with this paragraph
                current_chunk = paragraph
        else:
            # Add the paragraph to the current chunk
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph

    # Add the last chunk if it's not empty
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def embed(text):
    """Create embedding with error handling"""
    try:
        response = cohere_client.embed(
            model=EMBED_MODEL,
            input_type="search_query",  # Use search_query for queries
            texts=[text],
        )
        return response.embeddings[0]  # Return the first embedding
    except Exception as e:
        print(f"[ERROR] Failed to create embedding for text: {e}")
        return None


def create_collection():
    """Create Qdrant collection"""
    print("\nCreating Qdrant collection...")
    try:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=1024,        # Cohere embed-english-v3.0 dimension
                distance=Distance.COSINE
            )
        )
        print(f"Created new collection: {COLLECTION_NAME}")
    except Exception as e:
        print(f"Collection creation error (might already exist): {e}")


def save_chunk_to_qdrant(chunk, chunk_id, url):
    """Save a text chunk to Qdrant with error handling"""
    vector = embed(chunk)

    if vector is None:
        print(f"Skipping chunk {chunk_id} due to embedding error")
        return False

    try:
        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=chunk_id,  # Using sequential ID
                    vector=vector,
                    payload={
                        "url": url,
                        "text": chunk,
                        "chunk_id": chunk_id
                    }
                )
            ]
        )
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save chunk {chunk_id}: {e}")
        return False


def ingest_book():
    """Main ingestion function"""
    urls = get_all_urls(SITEMAP_URL)

    create_collection()

    global_id = 1

    for url in urls:
        print(f"\nProcessing: {url}")
        text = extract_text_from_url(url)

        if not text:
            continue

        print(f"Extracted text length: {len(text)} characters")
        chunks = chunk_text(text, CHUNK_MAX_CHARS)

        print(f"Generated {len(chunks)} chunks")
        for ch in chunks:
            if save_chunk_to_qdrant(ch, global_id, url):
                print(f"Saved chunk {global_id} ({len(ch)} chars)")
                global_id += 1
            else:
                print(f"Failed to save chunk {global_id}")

    print("\nIngestion completed successfully!")
    print("Total chunks stored:", global_id - 1)


if __name__ == "__main__":
    print("Starting local ingestion process...")
    ingest_book()