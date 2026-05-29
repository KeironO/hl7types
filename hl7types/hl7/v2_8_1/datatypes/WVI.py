"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: WVI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class WVI(BaseModel):
    """HL7 v2 WVI data type.

    Attributes
    ----------
    wvi_1 : str
        WVI.1 (req) - Channel Number (NM)

    wvi_2 : str | None
        WVI.2 (opt) - Channel Name (ST)
    """

    wvi_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "wvi_1",
            "channel_number",
            "WVI.1",
        ),
        serialization_alias="WVI.1",
        title="Channel Number",
    )

    wvi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvi_2",
            "channel_name",
            "WVI.2",
        ),
        serialization_alias="WVI.2",
        title="Channel Name",
    )

    model_config = {"populate_by_name": True}
