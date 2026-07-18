"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CK
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .HD import HD

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CK(HL7Model):
    """Composite id with check digit (S2.9.5).

    Attributes
    ----------
    ck_1 : str | None
        CK.1 (opt) - ID number (NM) (NM)

    ck_2 : str | None
        CK.2 (opt) - check digit (NM) (NM)

    ck_3 : str | None
        CK.3 (opt) - code identifying the check digit scheme employed (ID)

    ck_4 : HD | None
        CK.4 (opt) - assigning authority (HD)
    """

    ck_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_1",
            "id_number_nm",
            "CK.1",
        ),
        serialization_alias="CK.1",
        title="ID number (NM)",
    )

    ck_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_2",
            "check_digit_nm",
            "CK.2",
        ),
        serialization_alias="CK.2",
        title="check digit (NM)",
    )

    ck_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_3",
            "code_identifying_the_check_digit_scheme_employed",
            "CK.3",
        ),
        serialization_alias="CK.3",
        title="code identifying the check digit scheme employed",
    )

    ck_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_4",
            "assigning_authority",
            "CK.4",
        ),
        serialization_alias="CK.4",
        title="assigning authority",
    )

    @field_validator("ck_1", "ck_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
