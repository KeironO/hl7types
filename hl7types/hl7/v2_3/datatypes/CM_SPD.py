"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_SPD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_SPD(BaseModel):
    """HL7 v2 CM_SPD data type."""

    cm_spd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_1",
            "specialty_name",
            "CM_SPD.1",
        ),
        serialization_alias="CM_SPD.1",
        title="specialty name",
    )

    cm_spd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_2",
            "governing_board",
            "CM_SPD.2",
        ),
        serialization_alias="CM_SPD.2",
        title="governing board",
    )

    cm_spd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_3",
            "eligible_or_certified",
            "CM_SPD.3",
        ),
        serialization_alias="CM_SPD.3",
        title="eligible or certified",
    )

    cm_spd_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_4",
            "date_of_certification",
            "CM_SPD.4",
        ),
        serialization_alias="CM_SPD.4",
        title="date of certification",
    )

    model_config = {"populate_by_name": True}
