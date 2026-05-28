"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RMC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class RMC(BaseModel):
    """HL7 v2 RMC data type."""

    rmc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmc_1",
            "room_type",
            "RMC.1",
        ),
        serialization_alias="RMC.1",
        title="room type",
    )

    rmc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmc_2",
            "amount_type",
            "RMC.2",
        ),
        serialization_alias="RMC.2",
        title="amount type",
    )

    rmc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmc_3",
            "coverage_amount",
            "RMC.3",
        ),
        serialization_alias="RMC.3",
        title="coverage amount",
    )

    model_config = {"populate_by_name": True}
