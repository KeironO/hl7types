"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TX import TX


class NTE(BaseModel):
    """HL7 v2 NTE segment."""

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

    nte_3: List[TX] = Field(
        default=...,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="COMMENT",
        description="Item #575",
    )

    model_config = {"populate_by_name": True}
