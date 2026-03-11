from datetime import date

from app.application.ports.benchmark_repository import BenchmarkRepository
from app.domain.enums.seniority_level import SeniorityLevel
from app.domain.models.benchmark_record import BenchmarkRecord


class InMemoryBenchmarkRepository(BenchmarkRepository):
    def __init__(self) -> None:
        self._records = [
            BenchmarkRecord(
                role_title="Backend Engineer",
                seniority_level=SeniorityLevel.SENIOR,
                location="London",
                currency="GBP",
                p25_base_salary=85000,
                p50_base_salary=95000,
                p75_base_salary=110000,
                p90_base_salary=125000,
                data_points=137,
                effective_date=date(2026, 1, 1),
            ),
            BenchmarkRecord(
                role_title="Data Engineer",
                seniority_level=SeniorityLevel.STAFF,
                location="Berlin",
                currency="EUR",
                p25_base_salary=90000,
                p50_base_salary=105000,
                p75_base_salary=120000,
                p90_base_salary=135000,
                data_points=89,
                effective_date=date(2026, 1, 1),
            ),
            BenchmarkRecord(
                role_title="Data Scientist",
                seniority_level=SeniorityLevel.MID,
                location="New York",
                currency="USD",
                p25_base_salary=115000,
                p50_base_salary=130000,
                p75_base_salary=150000,
                p90_base_salary=170000,
                data_points=112,
                effective_date=date(2026, 1, 1),
            ),
        ]

    def find_benchmark(
        self,
        role_title: str,
        location: str,
        seniority_level: SeniorityLevel | None,
    ) -> BenchmarkRecord | None:
        for record in self._records:
            if record.role_title != role_title:
                continue

            if record.location != location:
                continue

            if seniority_level is not None and record.seniority_level != seniority_level:
                continue

            return record

        return None