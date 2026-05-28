"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CCP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CCP(BaseModel):
    """HL7 v2 CCP data type."""

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

    model_config = {"populate_by_name": True}
