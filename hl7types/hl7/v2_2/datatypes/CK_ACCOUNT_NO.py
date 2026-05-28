"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CK_ACCOUNT_NO
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CK_ACCOUNT_NO(BaseModel):
    """HL7 v2 CK_ACCOUNT_NO data type."""

    ck_account_no_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_account_no_1",
            "account_number",
            "CK_ACCOUNT_NO.1",
        ),
        serialization_alias="CK_ACCOUNT_NO.1",
        title="account number",
    )

    ck_account_no_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_account_no_2",
            "check_digit",
            "CK_ACCOUNT_NO.2",
        ),
        serialization_alias="CK_ACCOUNT_NO.2",
        title="Check digit",
    )

    ck_account_no_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_account_no_3",
            "check_digit_scheme",
            "CK_ACCOUNT_NO.3",
        ),
        serialization_alias="CK_ACCOUNT_NO.3",
        title="Check digit scheme",
    )

    ck_account_no_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_account_no_4",
            "facility_id",
            "CK_ACCOUNT_NO.4",
        ),
        serialization_alias="CK_ACCOUNT_NO.4",
        title="Facility ID",
    )

    model_config = {"populate_by_name": True}
