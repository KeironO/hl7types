"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DLD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class DLD(BaseModel):
    """HL7 v2 DLD data type."""

    dld_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "dld_1",
            "discharge_to_location",
            "DLD.1",
        ),
        serialization_alias="DLD.1",
        title="Discharge to Location",
    )

    dld_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dld_2",
            "effective_date",
            "DLD.2",
        ),
        serialization_alias="DLD.2",
        title="Effective Date",
    )

    model_config = {"populate_by_name": True}
