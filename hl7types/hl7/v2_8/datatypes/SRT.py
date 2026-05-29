"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SRT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class SRT(BaseModel):
    """HL7 v2 SRT data type.

    Attributes
    ----------
    srt_1 : str
        SRT.1 (req) - Sort-by Field (ST)

    srt_2 : str | None
        SRT.2 (opt) - Sequencing (ID)
    """

    srt_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "srt_1",
            "sort_by_field",
            "SRT.1",
        ),
        serialization_alias="SRT.1",
        title="Sort-by Field",
    )

    srt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "srt_2",
            "sequencing",
            "SRT.2",
        ),
        serialization_alias="SRT.2",
        title="Sequencing",
    )

    model_config = {"populate_by_name": True}
