"""Contains all the data models used in inputs/outputs"""

from .clothing_item import ClothingItem
from .list_items_category import ListItemsCategory
from .outfit_response import OutfitResponse
from .recommendation_request import RecommendationRequest
from .recommendation_request_event_type import RecommendationRequestEventType
from .toggle_favorite_outfit_response_200 import ToggleFavoriteOutfitResponse200

__all__ = (
    "ClothingItem",
    "ListItemsCategory",
    "OutfitResponse",
    "RecommendationRequest",
    "RecommendationRequestEventType",
    "ToggleFavoriteOutfitResponse200",
)
