"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PI
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class PI(BaseModel):
    """HL7 v2 PI data type."""

    pi_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pi_1",
            "id_number_st",
            "PI.1",
        ),
        serialization_alias="PI.1",
        title="ID number (ST)",
    )

    pi_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pi_2",
            "type_of_id_number_is",
            "PI.2",
        ),
        serialization_alias="PI.2",
        title="type of ID number (IS)",
    )

    pi_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pi_3",
            "other_qualifying_info",
            "PI.3",
        ),
        serialization_alias="PI.3",
        title="other qualifying info",
    )

    model_config = {"populate_by_name": True}
