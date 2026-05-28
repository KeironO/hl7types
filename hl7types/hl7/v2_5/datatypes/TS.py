"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: TS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class TS(BaseModel):
    """HL7 v2 TS data type."""

    ts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_1",
            "time",
            "TS.1",
        ),
        serialization_alias="TS.1",
        title="Time",
    )

    ts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_2",
            "degree_of_precision",
            "TS.2",
        ),
        serialization_alias="TS.2",
        title="Degree of Precision",
    )

    model_config = {"populate_by_name": True}
