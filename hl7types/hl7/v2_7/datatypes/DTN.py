"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DTN
Type: Datatype
"""
from __future__ import annotations

import re

from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class DTN(HL7Model):
    """Day type and number (S2.A.23).

    Attributes
    ----------
    dtn_1 : CWE
        DTN.1 (req) - Day Type (CWE)

    dtn_2 : str
        DTN.2 (req) - Number of Days (NM)
    """

    dtn_1: CWE = Field(
        validation_alias=AliasChoices(
            "dtn_1",
            "day_type",
            "DTN.1",
        ),
        serialization_alias="DTN.1",
        title="Day Type",
    )

    dtn_2: str = Field(
        validation_alias=AliasChoices(
            "dtn_2",
            "number_of_days",
            "DTN.2",
        ),
        serialization_alias="DTN.2",
        title="Number of Days",
    )

    @field_validator("dtn_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
