"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CX
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class CX(BaseModel):
    """HL7 v2 CX data type."""

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

    model_config = {"populate_by_name": True}
