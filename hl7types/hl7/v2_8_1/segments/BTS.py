"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BTS
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class BTS(HL7Model):
    """Batch Trailer (S2.14.3).

    Attributes
    ----------
    bts_1 : str | None
        BTS.1 - Batch Message Count (ST) O S2.14.3.1

    bts_2 : str | None
        BTS.2 - Batch Comment (ST) O S2.14.2.10

    bts_3 : list[str] | None
        BTS.3 - Batch Totals (NM) O rep S2.14.3.3
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
        description="O | Item #00093",
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
        description="O | Item #00090",
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
        description="O | Item #00095",
    )

    @field_validator("bts_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
