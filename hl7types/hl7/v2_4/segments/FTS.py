"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: FTS
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class FTS(HL7Model):
    """File Trailer (S2.16.7).

    Attributes
    ----------
    fts_1 : str | None
        FTS.1 - File Batch Count (NM) O S2.16.7.1

    fts_2 : str | None
        FTS.2 - File Trailer Comment (ST) O S2.16.7.2
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
        description="O | Item #00079 | LEN:10",
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
        description="O | Item #00080 | LEN:80",
    )

    @field_validator("fts_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
