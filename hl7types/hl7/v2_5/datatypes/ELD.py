"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ELD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class ELD(BaseModel):
    """HL7 v2 ELD data type."""

    eld_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_1",
            "segment_id",
            "ELD.1",
        ),
        serialization_alias="ELD.1",
        title="Segment ID",
    )

    eld_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_2",
            "segment_sequence",
            "ELD.2",
        ),
        serialization_alias="ELD.2",
        title="Segment Sequence",
    )

    eld_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_3",
            "field_position",
            "ELD.3",
        ),
        serialization_alias="ELD.3",
        title="Field Position",
    )

    eld_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_4",
            "code_identifying_error",
            "ELD.4",
        ),
        serialization_alias="ELD.4",
        title="Code Identifying Error",
    )

    model_config = {"populate_by_name": True}
