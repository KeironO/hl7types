"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CP
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .MO import MO


class CP(BaseModel):
    """HL7 v2 CP data type."""

    cp_1: MO = Field(
        default=...,
        validation_alias=AliasChoices(
            "cp_1",
            "price",
            "CP.1",
        ),
        serialization_alias="CP.1",
        title="Price",
    )

    cp_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cp_2",
            "price_type",
            "CP.2",
        ),
        serialization_alias="CP.2",
        title="Price Type",
    )

    cp_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cp_3",
            "from_value",
            "CP.3",
        ),
        serialization_alias="CP.3",
        title="From Value",
    )

    cp_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cp_4",
            "to_value",
            "CP.4",
        ),
        serialization_alias="CP.4",
        title="To Value",
    )

    cp_5: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cp_5",
            "range_units",
            "CP.5",
        ),
        serialization_alias="CP.5",
        title="Range Units",
    )

    cp_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cp_6",
            "range_type",
            "CP.6",
        ),
        serialization_alias="CP.6",
        title="Range Type",
    )

    model_config = {"populate_by_name": True}
