from typing import Annotated

from fastapi import Body

from app.app_settings import app_settings
from app.core.modules_factory import qdrant_client, sentence_transformers
from . import schemas


async def process_search(
        request: schemas.SearchQueryRequest = Annotated[schemas.SearchQueryRequest, Body(...)]
) -> schemas.SearchQueryResponse:
    query_embedding = sentence_transformers.encode(request.input_query).tolist()

    # Search in Qdrant
    search_result = qdrant_client.search(
        collection_name=app_settings.qdrant_default_collection_name,
        query_vector=query_embedding,
        limit=3,
        with_payload=True
    )

    # Extract and format results
    results = []
    for result in search_result:
        results.append(schemas.ResultCandidate.model_validate({
            'sentence': result.payload['sentence'],
            'score': result.score
        }))

    return schemas.SearchQueryResponse.model_validate({'results': results})
