import csv
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class VideoMetrics:
    title: str
    ctr: float
    retention_rate: float
    
    

class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: list[VideoMetrics]) -> list[dict]:
        
        ...

class ClickbaitReport(BaseReport):
    def generate(self, data: list[VideoMetrics]) -> list[dict]:
        filtered = [
            m for m in data
            if m.ctr > 15 and m.retention_rate < 40
        ]
        filtered.sort(key=lambda m: m.ctr, reverse=True)
        return [
            {"title": m.title, "ctr": m.ctr, "retention_rate": m.retention_rate}
            for m in filtered
        ]


REPORTS = {
    "clickbait": ClickbaitReport(),
}