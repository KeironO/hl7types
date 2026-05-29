"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RMC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .MOP import MOP


class RMC(BaseModel):
    """HL7 v2 RMC data type.

    Attributes
    ----------
    rmc_1 : CWE
        RMC.1 (req) - Room Type (CWE)

    rmc_2 : CWE | None
        RMC.2 (opt) - Amount Type (CWE)

    rmc_4 : MOP
        RMC.4 (req) - Money or Percentage (MOP)
    """

    rmc_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rmc_1",
            "room_type",
            "RMC.1",
        ),
        serialization_alias="RMC.1",
        title="Room Type",
    )

    rmc_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmc_2",
            "amount_type",
            "RMC.2",
        ),
        serialization_alias="RMC.2",
        title="Amount Type",
    )

    rmc_4: MOP = Field(
        default=...,
        validation_alias=AliasChoices(
            "rmc_4",
            "money_or_percentage",
            "RMC.4",
        ),
        serialization_alias="RMC.4",
        title="Money or Percentage",
    )

    model_config = {"populate_by_name": True}
