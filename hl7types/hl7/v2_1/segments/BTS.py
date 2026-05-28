"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: BTS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class BTS(BaseModel):
    """HL7 v2 BTS segment."""

    bts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_1",
            "batch_message_count",
            "BTS.1",
        ),
        serialization_alias="BTS.1",
        title="BATCH MESSAGE COUNT",
        description="Item #664",
    )

    bts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_2",
            "batch_comment",
            "BTS.2",
        ),
        serialization_alias="BTS.2",
        title="BATCH COMMENT",
        description="Item #665",
    )

    bts_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_3",
            "batch_totals",
            "BTS.3",
        ),
        serialization_alias="BTS.3",
        title="BATCH TOTALS",
        description="Item #666",
    )

    model_config = {"populate_by_name": True}
