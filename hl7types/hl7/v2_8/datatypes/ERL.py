"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ERL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class ERL(BaseModel):
    """HL7 v2 ERL data type."""

    erl_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "erl_1",
            "segment_id",
            "ERL.1",
        ),
        serialization_alias="ERL.1",
        title="Segment ID",
    )

    erl_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "erl_2",
            "segment_sequence",
            "ERL.2",
        ),
        serialization_alias="ERL.2",
        title="Segment Sequence",
    )

    erl_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erl_3",
            "field_position",
            "ERL.3",
        ),
        serialization_alias="ERL.3",
        title="Field Position",
    )

    erl_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erl_4",
            "field_repetition",
            "ERL.4",
        ),
        serialization_alias="ERL.4",
        title="Field Repetition",
    )

    erl_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erl_5",
            "component_number",
            "ERL.5",
        ),
        serialization_alias="ERL.5",
        title="Component Number",
    )

    erl_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erl_6",
            "sub_component_number",
            "ERL.6",
        ),
        serialization_alias="ERL.6",
        title="Sub-Component Number",
    )

    model_config = {"populate_by_name": True}
