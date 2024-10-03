from fastapi import APIRouter, Depends

from . import dependencies
from . import schemas

search_router = APIRouter()


@search_router.post(
    '',
    response_model=schemas.SearchQueryResponse)
async def search(
        results: schemas.SearchQueryResponse = Depends(dependencies.process_search)
):
    """ Search for a query in the database """
    return results
