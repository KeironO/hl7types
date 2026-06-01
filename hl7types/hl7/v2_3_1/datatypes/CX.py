"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CX
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .HD import HD


class CX(HL7Model):
    """HL7 v2 CX data type.

    Attributes
    ----------
    cx_1 : str | None
        CX.1 (opt) - ID (ST)

    cx_2 : str | None
        CX.2 (opt) - check digit (NM)

    cx_3 : str | None
        CX.3 (opt) - code identifying the check digit scheme employed (ID)

    cx_4 : HD | None
        CX.4 (opt) - assigning authority (HD)

    cx_5 : str | None
        CX.5 (opt) - identifier type code (IS)

    cx_6 : HD | None
        CX.6 (opt) - assigning facility (HD)
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
            "check_digit",
            "CX.2",
        ),
        serialization_alias="CX.2",
        title="check digit",
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
            "identifier_type_code",
            "CX.5",
        ),
        serialization_alias="CX.5",
        title="identifier type code",
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

    @field_validator("cx_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
