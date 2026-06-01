"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DIN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CWE import CWE


class DIN(HL7Model):
    """HL7 v2 DIN data type.

    Attributes
    ----------
    din_1 : str
        DIN.1 (req) - Date (DTM)

    din_2 : CWE
        DIN.2 (req) - Institution Name (CWE)
    """

    din_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "din_1",
            "date",
            "DIN.1",
        ),
        serialization_alias="DIN.1",
        title="Date",
    )

    din_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "din_2",
            "institution_name",
            "DIN.2",
        ),
        serialization_alias="DIN.2",
        title="Institution Name",
    )

    @field_validator("din_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
