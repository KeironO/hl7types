"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CK
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .HD import HD


class CK(HL7Model):
    """HL7 v2 CK data type.

    Attributes
    ----------
    ck_1 : str | None
        CK.1 (opt) - ID number (NM) (NM)

    ck_2 : str | None
        CK.2 (opt) - check digit (NM)

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
            "check_digit",
            "CK.2",
        ),
        serialization_alias="CK.2",
        title="check digit",
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
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
