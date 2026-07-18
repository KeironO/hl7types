"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PLN
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .CWE import CWE

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PLN(HL7Model):
    """Practitioner license or other id number (S2.A.54).

    Attributes
    ----------
    pln_1 : str
        PLN.1 (req) - ID Number (ST)

    pln_2 : CWE
        PLN.2 (req) - Type of ID Number (CWE)

    pln_3 : str | None
        PLN.3 (opt) - State/other Qualifying Information (ST)

    pln_4 : str | None
        PLN.4 (opt) - Expiration Date (DT)
    """

    pln_1: str = Field(
        validation_alias=AliasChoices(
            "pln_1",
            "id_number",
            "PLN.1",
        ),
        serialization_alias="PLN.1",
        title="ID Number",
    )

    pln_2: CWE = Field(
        validation_alias=AliasChoices(
            "pln_2",
            "type_of_id_number",
            "PLN.2",
        ),
        serialization_alias="PLN.2",
        title="Type of ID Number",
    )

    pln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_3",
            "state_other_qualifying_information",
            "PLN.3",
        ),
        serialization_alias="PLN.3",
        title="State/other Qualifying Information",
    )

    pln_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_4",
            "expiration_date",
            "PLN.4",
        ),
        serialization_alias="PLN.4",
        title="Expiration Date",
    )

    @field_validator("pln_4", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
