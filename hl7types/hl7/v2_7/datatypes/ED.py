"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ED
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .HD import HD
from .TX import TX


class ED(BaseModel):
    """HL7 v2 ED data type."""

    ed_1: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_1",
            "source_application",
            "ED.1",
        ),
        serialization_alias="ED.1",
        title="Source Application",
    )

    ed_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ed_2",
            "type_of_data",
            "ED.2",
        ),
        serialization_alias="ED.2",
        title="Type of Data",
    )

    ed_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_3",
            "data_subtype",
            "ED.3",
        ),
        serialization_alias="ED.3",
        title="Data Subtype",
    )

    ed_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ed_4",
            "encoding",
            "ED.4",
        ),
        serialization_alias="ED.4",
        title="Encoding",
    )

    ed_5: TX = Field(
        default=...,
        validation_alias=AliasChoices(
            "ed_5",
            "data",
            "ED.5",
        ),
        serialization_alias="ED.5",
        title="Data",
    )

    model_config = {"populate_by_name": True}
