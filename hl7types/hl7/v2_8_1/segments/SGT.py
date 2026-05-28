"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SGT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class SGT(BaseModel):
    """HL7 v2 SGT segment."""

    sgt_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "sgt_1",
            "set_id_sgt",
            "SGT.1",
        ),
        serialization_alias="SGT.1",
        title="Set ID - SGT",
        description="Item #3394",
    )

    sgt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sgt_2",
            "segment_group_name",
            "SGT.2",
        ),
        serialization_alias="SGT.2",
        title="Segment Group Name",
        description="Item #3395",
    )

    model_config = {"populate_by_name": True}
