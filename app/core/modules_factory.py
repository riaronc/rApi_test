from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

from app.app_settings import app_settings

# Initialize Qdrant client
qdrant_client = QdrantClient(**app_settings.qdrant_db_kwargs)
sentence_transformers = SentenceTransformer('all-MiniLM-L6-v2')

collection_name = app_settings.qdrant_default_collection_name
