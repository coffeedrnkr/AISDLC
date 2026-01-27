from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClothingItem")


@_attrs_define
class ClothingItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):  Example: Beige Trench Coat.
        image_url (str | Unset):
        warmth_rating (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    image_url: str | Unset = UNSET
    warmth_rating: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        image_url = self.image_url

        warmth_rating = self.warmth_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if warmth_rating is not UNSET:
            field_dict["warmth_rating"] = warmth_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        image_url = d.pop("image_url", UNSET)

        warmth_rating = d.pop("warmth_rating", UNSET)

        clothing_item = cls(
            id=id,
            name=name,
            image_url=image_url,
            warmth_rating=warmth_rating,
        )

        clothing_item.additional_properties = d
        return clothing_item

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
