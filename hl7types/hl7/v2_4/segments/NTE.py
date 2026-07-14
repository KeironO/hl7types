"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class NTE(HL7Model):
    """Notes and Comments (S2.16.10).

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 (opt) - Set ID - NTE (SI) S2.16.10.1

    nte_2 : str | None
        NTE.2 (opt) - Source of Comment (ID) S2.16.10.2 | 0105 - Source of comment

    nte_3 : list[str] | None
        NTE.3 (opt, rep) - Comment (FT) S2.16.10.3

    nte_4 : CE | None
        NTE.4 (opt) - Comment Type (CE) S2.16.10.4 | 0364 - Comment type
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

    nte_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_4",
            "comment_type",
            "NTE.4",
        ),
        serialization_alias="NTE.4",
        title="Comment Type",
        description="Item #1318 | Table HL70364",
    )

    @field_validator("nte_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
