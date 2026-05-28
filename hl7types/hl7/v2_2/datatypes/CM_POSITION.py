"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_POSITION
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_POSITION(BaseModel):
    """HL7 v2 CM_POSITION data type."""

    cm_position_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_position_1",
            "saal",
            "CM_POSITION.1",
        ),
        serialization_alias="CM_POSITION.1",
        title="Saal",
    )

    cm_position_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_position_2",
            "tisch",
            "CM_POSITION.2",
        ),
        serialization_alias="CM_POSITION.2",
        title="Tisch",
    )

    cm_position_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_position_3",
            "stuhl",
            "CM_POSITION.3",
        ),
        serialization_alias="CM_POSITION.3",
        title="Stuhl",
    )

    model_config = {"populate_by_name": True}
