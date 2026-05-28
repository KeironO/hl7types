"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DIN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class DIN(BaseModel):
    """HL7 v2 DIN data type."""

    din_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "din_1",
            "date",
            "DIN.1",
        ),
        serialization_alias="DIN.1",
        title="Date",
    )

    din_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "din_2",
            "institution_name",
            "DIN.2",
        ),
        serialization_alias="DIN.2",
        title="Institution Name",
    )

    model_config = {"populate_by_name": True}
