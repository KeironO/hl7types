"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: NDS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class NDS(BaseModel):
    """HL7 v2 NDS segment."""

    nds_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nds_1",
            "notification_reference_number",
            "NDS.1",
        ),
        serialization_alias="NDS.1",
        title="Notification Reference Number",
        description="Item #1398",
    )

    nds_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nds_2",
            "notification_date_time",
            "NDS.2",
        ),
        serialization_alias="NDS.2",
        title="Notification Date/Time",
        description="Item #1399",
    )

    nds_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "nds_3",
            "notification_alert_severity",
            "NDS.3",
        ),
        serialization_alias="NDS.3",
        title="Notification Alert Severity",
        description="Item #1400 | Table HL70367",
    )

    nds_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "nds_4",
            "notification_code",
            "NDS.4",
        ),
        serialization_alias="NDS.4",
        title="Notification Code",
        description="Item #1401 | Table HL79999",
    )

    model_config = {"populate_by_name": True}
