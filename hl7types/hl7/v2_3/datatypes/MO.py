"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MO
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MO(BaseModel):
    """HL7 v2 MO data type.

    Attributes
    ----------
    mo_1 : str | None
        MO.1 (opt) - quantity (NM)

    mo_2 : str | None
        MO.2 (opt) - denomination (ID)
    """

    mo_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_1",
            "quantity",
            "MO.1",
        ),
        serialization_alias="MO.1",
        title="quantity",
    )

    mo_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_2",
            "denomination",
            "MO.2",
        ),
        serialization_alias="MO.2",
        title="denomination",
    )

    model_config = {"populate_by_name": True}
