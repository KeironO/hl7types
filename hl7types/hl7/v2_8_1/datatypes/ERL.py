"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ERL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class ERL(HL7Model):
    """HL7 v2 ERL data type.

    Attributes
    ----------
    erl_1 : str
        ERL.1 (req) - Segment ID (ST)

    erl_2 : str
        ERL.2 (req) - Segment Sequence (NM)

    erl_3 : str | None
        ERL.3 (opt) - Field Position (NM)

    erl_4 : str | None
        ERL.4 (opt) - Field Repetition (NM)

    erl_5 : str | None
        ERL.5 (opt) - Component Number (NM)

    erl_6 : str | None
        ERL.6 (opt) - Sub-Component Number (NM)
    """

    erl_1: str = Field(
        default=...,
        max_length=3,
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

    @field_validator("erl_2", "erl_3", "erl_4", "erl_5", "erl_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
