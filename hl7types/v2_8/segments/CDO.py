"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CDO
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ


class CDO(BaseModel):
    """HL7 v2 CDO segment."""

    cdo_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdo_1",
            "set_id_cdo",
            "CDO.1",
        ),
        serialization_alias="CDO.1",
        title="Set ID - CDO",
        description="Item #3430",
    )

    cdo_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdo_2",
            "action_code",
            "CDO.2",
        ),
        serialization_alias="CDO.2",
        title="Action Code",
        description="Item #816 | Table HL70206",
    )

    cdo_3: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdo_3",
            "cumulative_dosage_limit",
            "CDO.3",
        ),
        serialization_alias="CDO.3",
        title="Cumulative Dosage Limit",
        description="Item #3397",
    )

    cdo_4: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdo_4",
            "cumulative_dosage_limit_time_interval",
            "CDO.4",
        ),
        serialization_alias="CDO.4",
        title="Cumulative Dosage Limit Time Interval",
        description="Item #3398 | Table HL70924",
    )

    model_config = {"populate_by_name": True}
