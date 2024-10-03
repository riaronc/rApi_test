from pydantic import BaseModel


class ResultCandidate(BaseModel):
    sentence: str
    score: float

class SearchQueryRequest(BaseModel):
    input_query: str


class SearchQueryResponse(BaseModel):
    results: list[ResultCandidate]
