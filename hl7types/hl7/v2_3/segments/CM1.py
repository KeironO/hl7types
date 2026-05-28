"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class CM1(BaseModel):
    """HL7 v2 CM1 segment."""

    cm1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cm1_1",
            "cm1_set_id",
            "CM1.1",
        ),
        serialization_alias="CM1.1",
        title="CM1 - Set ID",
        description="Item #1021",
    )

    cm1_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm1_2",
            "study_phase_identifier",
            "CM1.2",
        ),
        serialization_alias="CM1.2",
        title="Study Phase Identifier",
        description="Item #1051",
    )

    cm1_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cm1_3",
            "description_of_study_phase",
            "CM1.3",
        ),
        serialization_alias="CM1.3",
        title="Description of Study Phase",
        description="Item #1023",
    )

    model_config = {"populate_by_name": True}
