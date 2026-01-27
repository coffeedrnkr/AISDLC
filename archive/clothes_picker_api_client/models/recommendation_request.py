from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.recommendation_request_event_type import RecommendationRequestEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendationRequest")


@_attrs_define
class RecommendationRequest:
    """
    Attributes:
        date (datetime.date):  Example: 2025-10-30.
        event_type (RecommendationRequestEventType | Unset):  Default: RecommendationRequestEventType.CASUAL.
        weather_override (str | Unset): Optional. If not provided, backend fetches real weather. Example: Rainy, 15C.
    """

    date: datetime.date
    event_type: RecommendationRequestEventType | Unset = RecommendationRequestEventType.CASUAL
    weather_override: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        weather_override = self.weather_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if weather_override is not UNSET:
            field_dict["weather_override"] = weather_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        _event_type = d.pop("event_type", UNSET)
        event_type: RecommendationRequestEventType | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = RecommendationRequestEventType(_event_type)

        weather_override = d.pop("weather_override", UNSET)

        recommendation_request = cls(
            date=date,
            event_type=event_type,
            weather_override=weather_override,
        )

        recommendation_request.additional_properties = d
        return recommendation_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
