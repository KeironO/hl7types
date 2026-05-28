"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: WVS
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class WVS(BaseModel):
    """HL7 v2 WVS data type."""

    wvs_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "wvs_1",
            "source_one_name",
            "WVS.1",
        ),
        serialization_alias="WVS.1",
        title="Source One Name",
    )

    wvs_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvs_2",
            "source_two_name",
            "WVS.2",
        ),
        serialization_alias="WVS.2",
        title="Source Two Name",
    )

    model_config = {"populate_by_name": True}
