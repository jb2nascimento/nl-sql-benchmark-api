from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5,
        max_length=500,
        json_schema_extra={"example": "What is the compensation range for Senior Backend Engineer in London?"},
    )


class BenchmarkResponse(BaseModel):
    currency: str
    p25_base_salary: int
    p50_base_salary: int
    p75_base_salary: int
    p90_base_salary: int
    data_points: int


class QueryResponse(BaseModel):
    summary: str
    insufficient_data: bool
    parsed_role_title: str | None
    parsed_seniority_level: str | None
    parsed_location: str | None
    parsed_metric_requested: str | None
    benchmark: BenchmarkResponse | None
    notes: list[str]
