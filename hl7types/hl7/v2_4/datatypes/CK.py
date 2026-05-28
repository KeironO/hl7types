"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CK
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class CK(BaseModel):
    """HL7 v2 CK data type."""

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

    model_config = {"populate_by_name": True}
