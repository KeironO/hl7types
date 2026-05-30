"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: FTS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class FTS(HL7Model):
    """HL7 v2 FTS segment.

    Attributes
    ----------
    fts_1 : str | None
        FTS.1 (opt) - FILE BATCH COUNT (ST)

    fts_2 : str | None
        FTS.2 (opt) - FILE TRAILER COMMENT (ST)
    """

    fts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fts_1",
            "file_batch_count",
            "FTS.1",
        ),
        serialization_alias="FTS.1",
        title="FILE BATCH COUNT",
        description="Item #667",
    )

    fts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fts_2",
            "file_trailer_comment",
            "FTS.2",
        ),
        serialization_alias="FTS.2",
        title="FILE TRAILER COMMENT",
        description="Item #668",
    )

    model_config = {"populate_by_name": True}
