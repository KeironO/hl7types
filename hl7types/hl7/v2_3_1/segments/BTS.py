"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: BTS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class BTS(BaseModel):
    """HL7 v2 BTS segment.

    Attributes
    ----------
    bts_1 : str | None
        BTS.1 (opt) - Batch Message Count (ST)

    bts_2 : str | None
        BTS.2 (opt) - Batch Comment (ST)

    bts_3 : list[str] | None
        BTS.3 (opt, rep) - Batch Totals (NM)
    """

    bts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_1",
            "batch_message_count",
            "BTS.1",
        ),
        serialization_alias="BTS.1",
        title="Batch Message Count",
        description="Item #93",
    )

    bts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_2",
            "batch_comment",
            "BTS.2",
        ),
        serialization_alias="BTS.2",
        title="Batch Comment",
        description="Item #90",
    )

    bts_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_3",
            "batch_totals",
            "BTS.3",
        ),
        serialization_alias="BTS.3",
        title="Batch Totals",
        description="Item #95",
    )

    model_config = {"populate_by_name": True}
