"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.TX import TX


class NTE(HL7Model):
    """HL7 v2 NTE segment.

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 (opt) - SET ID - NOTES AND COMMENTS (SI)

    nte_2 : str | None
        NTE.2 (opt) - SOURCE OF COMMENT (ID)

    nte_3 : list[TX] | None
        NTE.3 (req, rep) - COMMENT (TX) [optional: TX has no required components]
    """

    nte_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_notes_and_comments",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="SET ID - NOTES AND COMMENTS",
        description="Item #573",
    )

    nte_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_2",
            "source_of_comment",
            "NTE.2",
        ),
        serialization_alias="NTE.2",
        title="SOURCE OF COMMENT",
        description="Item #574 | Table HL70105",
    )

    nte_3: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="COMMENT",
        description="Item #575",
    )

    @field_validator("nte_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
