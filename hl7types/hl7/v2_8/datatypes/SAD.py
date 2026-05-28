"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SAD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class SAD(BaseModel):
    """HL7 v2 SAD data type."""

    sad_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sad_1",
            "street_or_mailing_address",
            "SAD.1",
        ),
        serialization_alias="SAD.1",
        title="Street or Mailing Address",
    )

    sad_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sad_2",
            "street_name",
            "SAD.2",
        ),
        serialization_alias="SAD.2",
        title="Street Name",
    )

    sad_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sad_3",
            "dwelling_number",
            "SAD.3",
        ),
        serialization_alias="SAD.3",
        title="Dwelling Number",
    )

    model_config = {"populate_by_name": True}
