from enum import Enum


class ListItemsCategory(str, Enum):
    BOTTOMS = "Bottoms"
    SHOES = "Shoes"
    TOPS = "Tops"

    def __str__(self) -> str:
        return str(self.value)
