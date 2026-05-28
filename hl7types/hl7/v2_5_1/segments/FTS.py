"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: FTS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class FTS(BaseModel):
    """HL7 v2 FTS segment."""

    fts_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fts_1",
            "file_batch_count",
            "FTS.1",
        ),
        serialization_alias="FTS.1",
        title="File Batch Count",
        description="Item #79",
    )

    fts_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fts_2",
            "file_trailer_comment",
            "FTS.2",
        ),
        serialization_alias="FTS.2",
        title="File Trailer Comment",
        description="Item #80",
    )

    model_config = {"populate_by_name": True}
