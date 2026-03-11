from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500, example="What is the compensation range for Senior Backend Engineer in London?")

class QueryResponse(BaseModel):
    summary: str
    insufficient_data: bool
    parsed_role_title: str | None
    parsed_seniority_level: str | None
    parsed_location: str | None
    parsed_metric_requested: str | None
    currency: str | None
    p25_base_salary: int | None
    p50_base_salary: int | None
    p75_base_salary: int | None
    p90_base_salary: int | None
    data_points: int | None