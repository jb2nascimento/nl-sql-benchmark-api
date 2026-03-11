from dataclasses import dataclass

@dataclass
class QueryResult:
    summary: str
    insufficient_data: bool
    parsed_role_title: str | None
    parsed_seniority_level: str | None
    parsed_location: str | None
    parsed_metric_requested: str | None