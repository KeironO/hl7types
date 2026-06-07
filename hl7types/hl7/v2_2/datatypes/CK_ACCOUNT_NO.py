"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CK_ACCOUNT_NO
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CK_ACCOUNT_NO(HL7Model):
    """HL7 v2 CK_ACCOUNT_NO data type.

    Attributes
    ----------
    ck_account_no_1 : str | None
        CK_ACCOUNT_NO.1 (opt) - account number (NM)

    ck_account_no_2 : str | None
        CK_ACCOUNT_NO.2 (opt) - Check digit (NM)

    ck_account_no_3 : str | None
        CK_ACCOUNT_NO.3 (opt) - Check digit scheme (ID)

    ck_account_no_4 : str | None
        CK_ACCOUNT_NO.4 (opt) - Facility ID (ID)
    """

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

    @field_validator("ck_account_no_1", "ck_account_no_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
