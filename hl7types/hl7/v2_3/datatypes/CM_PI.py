"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PI
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_PI(BaseModel):
    """HL7 v2 CM_PI data type."""

    cm_pi_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pi_1",
            "id_number_st",
            "CM_PI.1",
        ),
        serialization_alias="CM_PI.1",
        title="ID number (ST)",
    )

    cm_pi_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pi_2",
            "type_of_id_number_is",
            "CM_PI.2",
        ),
        serialization_alias="CM_PI.2",
        title="type of ID number (IS)",
    )

    cm_pi_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pi_3",
            "other_qualifying_info",
            "CM_PI.3",
        ),
        serialization_alias="CM_PI.3",
        title="other qualifying info",
    )

    model_config = {"populate_by_name": True}
