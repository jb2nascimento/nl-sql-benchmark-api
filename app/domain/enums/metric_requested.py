from enum import Enum

class MetricRequested(str, Enum):
    RANGE = "range"
    P25 = "p25"
    P50 = "p50"
    P75 = "p75"
    P90 = "p90"
