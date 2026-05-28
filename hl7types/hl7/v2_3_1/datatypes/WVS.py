"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: WVS
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class WVS(BaseModel):
    """HL7 v2 WVS data type."""

    wvs_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvs_1",
            "source_name_1",
            "WVS.1",
        ),
        serialization_alias="WVS.1",
        title="source name 1",
    )

    wvs_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvs_2",
            "source_name_2",
            "WVS.2",
        ),
        serialization_alias="WVS.2",
        title="source name 2",
    )

    model_config = {"populate_by_name": True}
