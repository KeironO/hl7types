"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: FTS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class FTS(HL7Model):
    """FILE TRAILER (S2.10.12).

    Attributes
    ----------
    fts_1 : str | None
        FTS.1 - File Batch Count (NM) NA S2.10.12.1

    fts_2 : str | None
        FTS.2 - File Trailer Comment (ST) NA S2.10.12.2
    """

    fts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fts_1",
            "file_batch_count",
            "FTS.1",
        ),
        serialization_alias="FTS.1",
        title="File Batch Count",
        description="NA | Item #00079 | LEN:10",
    )

    fts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fts_2",
            "file_trailer_comment",
            "FTS.2",
        ),
        serialization_alias="FTS.2",
        title="File Trailer Comment",
        description="NA | Item #00080 | LEN:80",
    )

    @field_validator("fts_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
