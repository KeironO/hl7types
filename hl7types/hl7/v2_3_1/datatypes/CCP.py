"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CCP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CCP(BaseModel):
    """HL7 v2 CCP data type.

    Attributes
    ----------
    ccp_1 : str | None
        CCP.1 (opt) - channel calibration sensitivity correction factor (NM)

    ccp_2 : str | None
        CCP.2 (opt) - channel calibration baseline (NM)

    ccp_3 : str | None
        CCP.3 (opt) - channel calibration time skew (NM)
    """

    ccp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_1",
            "channel_calibration_sensitivity_correction_factor",
            "CCP.1",
        ),
        serialization_alias="CCP.1",
        title="channel calibration sensitivity correction factor",
    )

    ccp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_2",
            "channel_calibration_baseline",
            "CCP.2",
        ),
        serialization_alias="CCP.2",
        title="channel calibration baseline",
    )

    ccp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_3",
            "channel_calibration_time_skew",
            "CCP.3",
        ),
        serialization_alias="CCP.3",
        title="channel calibration time skew",
    )

    model_config = {"populate_by_name": True}
