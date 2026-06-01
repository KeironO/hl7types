"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ELD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CE import CE


class ELD(HL7Model):
    """HL7 v2 ELD data type.

    Attributes
    ----------
    eld_1 : str | None
        ELD.1 (opt) - segment ID (ST)

    eld_2 : str | None
        ELD.2 (opt) - sequence (NM)

    eld_3 : str | None
        ELD.3 (opt) - field position (NM)

    eld_4 : CE | None
        ELD.4 (opt) - code identifying error (CE)
    """

    eld_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_1",
            "segment_id",
            "ELD.1",
        ),
        serialization_alias="ELD.1",
        title="segment ID",
    )

    eld_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_2",
            "sequence",
            "ELD.2",
        ),
        serialization_alias="ELD.2",
        title="sequence",
    )

    eld_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_3",
            "field_position",
            "ELD.3",
        ),
        serialization_alias="ELD.3",
        title="field position",
    )

    eld_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eld_4",
            "code_identifying_error",
            "ELD.4",
        ),
        serialization_alias="ELD.4",
        title="code identifying error",
    )

    @field_validator("eld_2", "eld_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
