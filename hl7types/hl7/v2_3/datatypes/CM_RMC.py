"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_RMC
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CM_RMC(HL7Model):
    """Room coverage.

    Attributes
    ----------
    cm_rmc_1 : str | None
        CM_RMC.1 (opt) - room type (IS)

    cm_rmc_2 : str | None
        CM_RMC.2 (opt) - amount type (IS)

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
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
