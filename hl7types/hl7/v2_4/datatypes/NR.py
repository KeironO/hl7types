"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class NR(HL7Model):
    """HL7 v2 NR data type.

    Attributes
    ----------
    nr_1 : str | None
        NR.1 (opt) - Low Value (NM)

    nr_2 : str | None
        NR.2 (opt) - High Value (NM)
    """

    nr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nr_1",
            "low_value",
            "NR.1",
        ),
        serialization_alias="NR.1",
        title="Low Value",
    )

    nr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nr_2",
            "high_value",
            "NR.2",
        ),
        serialization_alias="NR.2",
        title="High Value",
    )

    @field_validator("nr_1", "nr_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
