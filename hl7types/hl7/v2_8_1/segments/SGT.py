"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SGT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')


class SGT(HL7Model):
    """Segment Group Trailer (S2.14.14).

    Attributes
    ----------
    sgt_1 : str
        SGT.1 - Set ID - SGT (SI) R S2.14.14.1

    sgt_2 : str | None
        SGT.2 - Segment Group Name (ST) O S2.14.14.2
    """

    sgt_1: str = Field(
        validation_alias=AliasChoices(
            "sgt_1",
            "set_id_sgt",
            "SGT.1",
        ),
        serialization_alias="SGT.1",
        title="Set ID - SGT",
        description="R | Item #03394 | LEN:4",
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
        description="O | Item #03395",
    )

    @field_validator("sgt_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
