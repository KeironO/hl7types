"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DTN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class DTN(BaseModel):
    """HL7 v2 DTN data type."""

    dtn_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "dtn_1",
            "day_type",
            "DTN.1",
        ),
        serialization_alias="DTN.1",
        title="Day Type",
    )

    dtn_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dtn_2",
            "number_of_days",
            "DTN.2",
        ),
        serialization_alias="DTN.2",
        title="Number of Days",
    )

    model_config = {"populate_by_name": True}
