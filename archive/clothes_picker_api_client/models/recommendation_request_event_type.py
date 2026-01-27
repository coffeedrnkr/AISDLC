from enum import Enum


class RecommendationRequestEventType(str, Enum):
    CASUAL = "Casual"
    DATE = "Date"
    FORMAL = "Formal"
    GYM = "Gym"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
