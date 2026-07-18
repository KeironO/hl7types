"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OCD
Type: Datatype
"""
from __future__ import annotations

import re

from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .CNE import CNE

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class OCD(HL7Model):
    """Occurrence code and date (S2.A.49).

    Attributes
    ----------
    ocd_1 : CNE
        OCD.1 (req) - Occurrence Code (CNE)

    ocd_2 : str
        OCD.2 (req) - Occurrence Date (DT)
    """

    ocd_1: CNE = Field(
        validation_alias=AliasChoices(
            "ocd_1",
            "occurrence_code",
            "OCD.1",
        ),
        serialization_alias="OCD.1",
        title="Occurrence Code",
    )

    ocd_2: str = Field(
        max_length=8,
        validation_alias=AliasChoices(
            "ocd_2",
            "occurrence_date",
            "OCD.2",
        ),
        serialization_alias="OCD.2",
        title="Occurrence Date",
    )

    @field_validator("ocd_2", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
