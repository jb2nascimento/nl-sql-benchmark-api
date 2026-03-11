from dataclasses import dataclass

from app.domain.enums.metric_requested import MetricRequested
from app.domain.enums.seniority_level import SeniorityLevel


@dataclass
class ParsedQuery:
    role_title: str | None
    seniority_level: SeniorityLevel | None
    location: str | None
    metric_requested: MetricRequested | None
