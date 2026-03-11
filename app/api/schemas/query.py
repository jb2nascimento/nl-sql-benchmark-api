from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500, example="What is the compensation range for Senior Backend Engineer in London?")

class QueryResponse(BaseModel):
    summary: str
    insufficient_data: bool
    parsed_role_title: str | None
    parsed_seniority_level: str | None
    parsed_location: str | None