"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NCK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class NCK(BaseModel):
    """HL7 v2 NCK segment.

    Attributes
    ----------
    nck_1 : str
        NCK.1 (req) - SYSTEM DATE/TIME (TS)
    """

    nck_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nck_1",
            "system_date_time",
            "NCK.1",
        ),
        serialization_alias="NCK.1",
        title="SYSTEM DATE/TIME",
        description="Item #742",
    )

    model_config = {"populate_by_name": True}
