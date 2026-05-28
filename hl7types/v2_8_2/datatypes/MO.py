"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MO
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MO(BaseModel):
    """HL7 v2 MO data type."""

    mo_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_1",
            "quantity",
            "MO.1",
        ),
        serialization_alias="MO.1",
        title="Quantity",
    )

    mo_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_2",
            "denomination",
            "MO.2",
        ),
        serialization_alias="MO.2",
        title="Denomination",
    )

    model_config = {"populate_by_name": True}
