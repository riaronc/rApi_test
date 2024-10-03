import logging
import ssl

import PyPDF2
import nltk
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

from app.app_settings import app_settings

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('punkt_tab')


def pdf_to_sentences(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text = f"{text} {page.extract_text()}\n"

    _sentences = nltk.tokenize.sent_tokenize(text)
    return _sentences


def initial_setup():
    sentences = pdf_to_sentences('data/example.pdf')
    logging.info(f'Extracted {len(sentences)} sentences from the PDF')
    qdrant_client = QdrantClient(**app_settings.qdrant_db_kwargs)
    logging.info(f'Connected to Qdrant at {app_settings.qdrant_host}:{app_settings.qdrant_port}')

    model = SentenceTransformer('all-MiniLM-L6-v2')
    logging.info('Loaded SentenceTransformer model')

    # Generate embeddings
    embeddings = model.encode(sentences, show_progress_bar=True)
    vector_size = embeddings.shape[1]
    logging.info(f'Generated embeddings of size {vector_size}')

    if not qdrant_client.collection_exists(app_settings.qdrant_default_collection_name):
        logging.warning(f'Collection {app_settings.qdrant_default_collection_name} does not exist. Creating...')
        qdrant_client.create_collection(
            collection_name=app_settings.qdrant_default_collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )
        logging.info(f'Collection {app_settings.qdrant_default_collection_name} created')

    # Prepare data for upload
    points = []
    for i, (embedding, sentence) in enumerate(zip(embeddings, sentences)):
        point = PointStruct(
            id=i,
            vector=embedding.tolist(),
            payload={'sentence': sentence}
        )
        points.append(point)

    # Upload points to Qdrant
    qdrant_client.upsert(collection_name=app_settings.qdrant_default_collection_name, points=points)
    logging.info(f'Uploaded {len(points)} points to collection {app_settings.qdrant_default_collection_name}')
