from dataclasses import dataclass
from datetime import date

from app.domain.enums.seniority_level import SeniorityLevel


@dataclass
class BenchmarkRecord:
    role_title: str
    seniority_level: SeniorityLevel
    location: str
    currency: str
    p25_base_salary: int
    p50_base_salary: int
    p75_base_salary: int
    p90_base_salary: int
    data_points: int
    effective_date: date
