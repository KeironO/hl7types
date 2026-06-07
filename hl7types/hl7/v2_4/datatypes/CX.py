"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CX
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .HD import HD


class CX(HL7Model):
    """HL7 v2 CX data type.

    Attributes
    ----------
    cx_1 : str | None
        CX.1 (opt) - ID (ST)

    cx_2 : str | None
        CX.2 (opt) - check digit (ST) (ST)

    cx_3 : str | None
        CX.3 (opt) - code identifying the check digit scheme employed (ID)

    cx_4 : HD | None
        CX.4 (opt) - assigning authority (HD)

    cx_5 : str | None
        CX.5 (opt) - identifier type code (ID) (ID)

    cx_6 : HD | None
        CX.6 (opt) - assigning facility (HD)

    cx_7 : str | None
        CX.7 (opt) - effective date (DT) (DT)

    cx_8 : str | None
        CX.8 (opt) - expiration date (DT)
    """

    cx_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_1",
            "id",
            "CX.1",
        ),
        serialization_alias="CX.1",
        title="ID",
    )

    cx_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_2",
            "check_digit_st",
            "CX.2",
        ),
        serialization_alias="CX.2",
        title="check digit (ST)",
    )

    cx_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_3",
            "code_identifying_the_check_digit_scheme_employed",
            "CX.3",
        ),
        serialization_alias="CX.3",
        title="code identifying the check digit scheme employed",
    )

    cx_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_4",
            "assigning_authority",
            "CX.4",
        ),
        serialization_alias="CX.4",
        title="assigning authority",
    )

    cx_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_5",
            "identifier_type_code_id",
            "CX.5",
        ),
        serialization_alias="CX.5",
        title="identifier type code (ID)",
    )

    cx_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_6",
            "assigning_facility",
            "CX.6",
        ),
        serialization_alias="CX.6",
        title="assigning facility",
    )

    cx_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_7",
            "effective_date_dt",
            "CX.7",
        ),
        serialization_alias="CX.7",
        title="effective date (DT)",
    )

    cx_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cx_8",
            "expiration_date",
            "CX.8",
        ),
        serialization_alias="CX.8",
        title="expiration date",
    )

    @field_validator("cx_7", "cx_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
