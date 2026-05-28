"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CK
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class CK(BaseModel):
    """HL7 v2 CK data type."""

    ck_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_1",
            "id_number_nm",
            "CK.1",
        ),
        serialization_alias="CK.1",
        title="ID number (NM)",
    )

    ck_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_2",
            "check_digit",
            "CK.2",
        ),
        serialization_alias="CK.2",
        title="check digit",
    )

    ck_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_3",
            "code_identifying_the_check_digit_scheme_employed",
            "CK.3",
        ),
        serialization_alias="CK.3",
        title="code identifying the check digit scheme employed",
    )

    ck_4: HD | None = Field(
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
