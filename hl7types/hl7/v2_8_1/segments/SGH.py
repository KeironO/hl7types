"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SGH
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class SGH(BaseModel):
    """HL7 v2 SGH segment.

    Attributes
    ----------
    sgh_1 : str
        SGH.1 (req) - Set ID - SGH (SI)

    sgh_2 : str | None
        SGH.2 (opt) - Segment Group Name (ST)
    """

    sgh_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "sgh_1",
            "set_id_sgh",
            "SGH.1",
        ),
        serialization_alias="SGH.1",
        title="Set ID - SGH",
        description="Item #3389",
    )

    sgh_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sgh_2",
            "segment_group_name",
            "SGH.2",
        ),
        serialization_alias="SGH.2",
        title="Segment Group Name",
        description="Item #3390",
    )

    model_config = {"populate_by_name": True}
