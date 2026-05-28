"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RP
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class RP(BaseModel):
    """HL7 v2 RP data type."""

    rp_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_1",
            "pointer",
            "RP.1",
        ),
        serialization_alias="RP.1",
        title="Pointer",
    )

    rp_2: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_2",
            "application_id",
            "RP.2",
        ),
        serialization_alias="RP.2",
        title="Application ID",
    )

    rp_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_3",
            "type_of_data",
            "RP.3",
        ),
        serialization_alias="RP.3",
        title="Type of Data",
    )

    rp_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_4",
            "subtype",
            "RP.4",
        ),
        serialization_alias="RP.4",
        title="Subtype",
    )

    model_config = {"populate_by_name": True}
