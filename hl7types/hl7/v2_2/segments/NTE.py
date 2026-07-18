"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NTE
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')


class NTE(HL7Model):
    """NOTES AND COMMENTS (S2.10.15).

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 - Set ID - Notes and Comments (SI) NA S2.10.15.1

    nte_2 : str | None
        NTE.2 - Source of Comment (ID) NA S2.10.15.2 | 0105 - SOURCE OF COMMENT

    nte_3 : list[str] | None
        NTE.3 - Comment (FT) NA rep S2.10.15.3
    """

    nte_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_notes_and_comments",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="Set ID - Notes and Comments",
        description="NA | Item #00096 | LEN:4",
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
        description="NA | Item #00097 | Table 0105 - SOURCE OF COMMENT | LEN:8",
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
        description="NA | Item #00098",
    )

    @field_validator("nte_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
