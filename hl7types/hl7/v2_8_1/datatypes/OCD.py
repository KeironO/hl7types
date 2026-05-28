"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OCD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CNE import CNE


class OCD(BaseModel):
    """HL7 v2 OCD data type."""

    ocd_1: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ocd_1",
            "occurrence_code",
            "OCD.1",
        ),
        serialization_alias="OCD.1",
        title="Occurrence Code",
    )

    ocd_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ocd_2",
            "occurrence_date",
            "OCD.2",
        ),
        serialization_alias="OCD.2",
        title="Occurrence Date",
    )

    model_config = {"populate_by_name": True}
