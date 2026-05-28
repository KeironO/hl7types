"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class RGS(BaseModel):
    """HL7 v2 RGS segment."""

    rgs_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rgs_1",
            "set_id_rgs",
            "RGS.1",
        ),
        serialization_alias="RGS.1",
        title="Set ID - RGS",
        description="Item #1203",
    )

    rgs_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rgs_2",
            "segment_action_code",
            "RGS.2",
        ),
        serialization_alias="RGS.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    rgs_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rgs_3",
            "resource_group_id",
            "RGS.3",
        ),
        serialization_alias="RGS.3",
        title="Resource Group ID",
        description="Item #1204",
    )

    model_config = {"populate_by_name": True}
