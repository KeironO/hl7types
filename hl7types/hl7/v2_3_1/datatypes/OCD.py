"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OCD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class OCD(BaseModel):
    """HL7 v2 OCD data type."""

    ocd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ocd_1",
            "occurrence_code",
            "OCD.1",
        ),
        serialization_alias="OCD.1",
        title="occurrence code",
    )

    ocd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ocd_2",
            "occurrence_date",
            "OCD.2",
        ),
        serialization_alias="OCD.2",
        title="occurrence date",
    )

    model_config = {"populate_by_name": True}
