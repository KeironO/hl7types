"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NTE
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_SI = re.compile(r'\d*')


class NTE(HL7Model):
    """Notes and Comments (S2.15.10).

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 - Set ID - NTE (SI) O S2.15.10.1

    nte_2 : str | None
        NTE.2 - Source of Comment (ID) O S2.15.10.2 | 0105 - Source of comment

    nte_3 : list[str] | None
        NTE.3 - Comment (FT) O rep S2.15.10.3

    nte_4 : CE | None
        NTE.4 - Comment Type (CE) O S2.15.10.4 | 0364 - Comment type
    """

    nte_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_nte",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="Set ID - NTE",
        description="O | Item #00096 | LEN:4",
    )

    nte_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_2",
            "source_of_comment",
            "NTE.2",
        ),
        serialization_alias="NTE.2",
        title="Source of Comment",
        description="O | Item #00097 | Table 0105 - Source of comment | LEN:8",
    )

    nte_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="Comment",
        description="O | Item #00098",
    )

    nte_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_4",
            "comment_type",
            "NTE.4",
        ),
        serialization_alias="NTE.4",
        title="Comment Type",
        description="O | Item #01318 | Table 0364 - Comment type",
    )

    @field_validator("nte_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
