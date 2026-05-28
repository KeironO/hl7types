"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SPD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class SPD(BaseModel):
    """HL7 v2 SPD data type."""

    spd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spd_1",
            "specialty_name",
            "SPD.1",
        ),
        serialization_alias="SPD.1",
        title="specialty name",
    )

    spd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spd_2",
            "governing_board",
            "SPD.2",
        ),
        serialization_alias="SPD.2",
        title="governing board",
    )

    spd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spd_3",
            "eligible_or_certified",
            "SPD.3",
        ),
        serialization_alias="SPD.3",
        title="eligible or certified",
    )

    spd_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spd_4",
            "date_of_certification",
            "SPD.4",
        ),
        serialization_alias="SPD.4",
        title="date of certification",
    )

    model_config = {"populate_by_name": True}
