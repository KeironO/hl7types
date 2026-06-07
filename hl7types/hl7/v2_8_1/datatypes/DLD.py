"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DLD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .CWE import CWE


class DLD(HL7Model):
    """HL7 v2 DLD data type.

    Attributes
    ----------
    dld_1 : CWE
        DLD.1 (req) - Discharge to Location (CWE)

    dld_2 : str | None
        DLD.2 (opt) - Effective Date (DTM)
    """

    dld_1: CWE = Field(
        validation_alias=AliasChoices(
            "dld_1",
            "discharge_to_location",
            "DLD.1",
        ),
        serialization_alias="DLD.1",
        title="Discharge to Location",
    )

    dld_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dld_2",
            "effective_date",
            "DLD.2",
        ),
        serialization_alias="DLD.2",
        title="Effective Date",
    )

    @field_validator("dld_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
