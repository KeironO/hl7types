"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CCP
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CCP(BaseModel):
    """HL7 v2 CCP data type."""

    ccp_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_1",
            "channel_calibration_sensitivity_correction_factor",
            "CCP.1",
        ),
        serialization_alias="CCP.1",
        title="channel calibration sensitivity correction factor",
    )

    ccp_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccp_2",
            "channel_calibration_baseline",
            "CCP.2",
        ),
        serialization_alias="CCP.2",
        title="channel calibration baseline",
    )

    ccp_3: str | None = Field(
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
