from abc import ABC, abstractmethod

from app.domain.enums.seniority_level import SeniorityLevel
from app.domain.models.benchmark_record import BenchmarkRecord

class BenchmarkRepository(ABC):
    @abstractmethod
    def find_benchmark(
        self,
        role_title: str,
        location: str,
        seniority_level: SeniorityLevel | None,
    ) -> BenchmarkRecord | None:
        pass