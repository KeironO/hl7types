"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_RMC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_RMC(BaseModel):
    """HL7 v2 CM_RMC data type."""

    cm_rmc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rmc_1",
            "room_type",
            "CM_RMC.1",
        ),
        serialization_alias="CM_RMC.1",
        title="room type",
    )

    cm_rmc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rmc_2",
            "amount_type",
            "CM_RMC.2",
        ),
        serialization_alias="CM_RMC.2",
        title="amount type",
    )

    cm_rmc_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rmc_3",
            "coverage_amount",
            "CM_RMC.3",
        ),
        serialization_alias="CM_RMC.3",
        title="coverage amount",
    )

    model_config = {"populate_by_name": True}
