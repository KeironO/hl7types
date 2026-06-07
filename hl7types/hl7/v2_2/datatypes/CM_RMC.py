"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_RMC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CM_RMC(HL7Model):
    """HL7 v2 CM_RMC data type.

    Attributes
    ----------
    cm_rmc_1 : str | None
        CM_RMC.1 (opt) - room type (ID)

    cm_rmc_2 : str | None
        CM_RMC.2 (opt) - amount type (ID)

    cm_rmc_3 : str | None
        CM_RMC.3 (opt) - coverage amount (NM)
    """

    cm_rmc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rmc_1",
            "room_type",
            "CM_RMC.1",
        ),
        serialization_alias="CM_RMC.1",
        title="room type",
    )

    cm_rmc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rmc_2",
            "amount_type",
            "CM_RMC.2",
        ),
        serialization_alias="CM_RMC.2",
        title="amount type",
    )

    cm_rmc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rmc_3",
            "coverage_amount",
            "CM_RMC.3",
        ),
        serialization_alias="CM_RMC.3",
        title="coverage amount",
    )

    @field_validator("cm_rmc_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
