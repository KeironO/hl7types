"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CX
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CWE import CWE
from .HD import HD


class CX(HL7Model):
    """HL7 v2 CX data type.

    Attributes
    ----------
    cx_1 : str
        CX.1 (req) - ID Number (ST)

    cx_2 : str | None
        CX.2 (opt) - Identifier Check Digit (ST)

    cx_3 : str | None
        CX.3 (opt) - Check Digit Scheme (ID)

    cx_4 : HD | None
        CX.4 (opt) - Assigning Authority (HD)

    cx_5 : str
        CX.5 (req) - Identifier Type Code (ID)

    cx_6 : HD | None
        CX.6 (opt) - Assigning Facility (HD)

    cx_7 : str | None
        CX.7 (opt) - Effective Date (DT)

    cx_8 : str | None
        CX.8 (opt) - Expiration Date (DT)

    cx_9 : CWE | None
        CX.9 (opt) - Assigning Jurisdiction (CWE)

    cx_10 : CWE | None
        CX.10 (opt) - Assigning Agency or Department (CWE)

    cx_11 : str | None
        CX.11 (opt) - Security Check (ST)

    cx_12 : str | None
        CX.12 (opt) - Security Check Scheme (ID)
    """

    cx_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cx_1",
            "id_number",
            "CX.1",
        ),
        serialization_alias="CX.1",
        title="ID Number",
    )

    cx_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_2",
            "identifier_check_digit",
            "CX.2",
        ),
        serialization_alias="CX.2",
        title="Identifier Check Digit",
    )

    cx_3: Optional[str] = Field(
        default=None,
        max_length=3,
        validation_alias=AliasChoices(
            "cx_3",
            "check_digit_scheme",
            "CX.3",
        ),
        serialization_alias="CX.3",
        title="Check Digit Scheme",
    )

    cx_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_4",
            "assigning_authority",
            "CX.4",
        ),
        serialization_alias="CX.4",
        title="Assigning Authority",
    )

    cx_5: str = Field(
        default=...,
        max_length=5,
        validation_alias=AliasChoices(
            "cx_5",
            "identifier_type_code",
            "CX.5",
        ),
        serialization_alias="CX.5",
        title="Identifier Type Code",
    )

    cx_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_6",
            "assigning_facility",
            "CX.6",
        ),
        serialization_alias="CX.6",
        title="Assigning Facility",
    )

    cx_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_7",
            "effective_date",
            "CX.7",
        ),
        serialization_alias="CX.7",
        title="Effective Date",
    )

    cx_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_8",
            "expiration_date",
            "CX.8",
        ),
        serialization_alias="CX.8",
        title="Expiration Date",
    )

    cx_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_9",
            "assigning_jurisdiction",
            "CX.9",
        ),
        serialization_alias="CX.9",
        title="Assigning Jurisdiction",
    )

    cx_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_10",
            "assigning_agency_or_department",
            "CX.10",
        ),
        serialization_alias="CX.10",
        title="Assigning Agency or Department",
    )

    cx_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_11",
            "security_check",
            "CX.11",
        ),
        serialization_alias="CX.11",
        title="Security Check",
    )

    cx_12: Optional[str] = Field(
        default=None,
        max_length=3,
        validation_alias=AliasChoices(
            "cx_12",
            "security_check_scheme",
            "CX.12",
        ),
        serialization_alias="CX.12",
        title="Security Check Scheme",
    )

    @field_validator("cx_7", "cx_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
