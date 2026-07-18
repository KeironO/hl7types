"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCP
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CCP(HL7Model):
    """Channel calibration parameters (S2.A.4).

    Attributes
    ----------
    ccp_1 : str | None
        CCP.1 (opt) - Channel Calibration Sensitivity Correction Factor (NM)

    ccp_2 : str | None
        CCP.2 (opt) - Channel Calibration Baseline (NM)

    ccp_3 : str | None
        CCP.3 (opt) - Channel Calibration Time Skew (NM)
    """

    ccp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_1",
            "channel_calibration_sensitivity_correction_factor",
            "CCP.1",
        ),
        serialization_alias="CCP.1",
        title="Channel Calibration Sensitivity Correction Factor",
    )

    ccp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_2",
            "channel_calibration_baseline",
            "CCP.2",
        ),
        serialization_alias="CCP.2",
        title="Channel Calibration Baseline",
    )

    ccp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_3",
            "channel_calibration_time_skew",
            "CCP.3",
        ),
        serialization_alias="CCP.3",
        title="Channel Calibration Time Skew",
    )

    @field_validator("ccp_1", "ccp_2", "ccp_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
