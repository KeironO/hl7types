"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class NTE(HL7Model):
    """NOTES AND COMMENTS (S2.10.15).

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 (opt) - Set ID - Notes and Comments (SI) S2.10.15.1

    nte_2 : str | None
        NTE.2 (opt) - Source of Comment (ID) S2.10.15.2 | 0105 - SOURCE OF COMMENT

    nte_3 : list[str] | None
        NTE.3 (opt, rep) - Comment (FT) S2.10.15.3
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
        description="Item #96",
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
        description="Item #97 | Table HL70105",
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
        description="Item #98",
    )

    @field_validator("nte_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
