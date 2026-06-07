"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CK_PAT_ID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CK_PAT_ID(HL7Model):
    """HL7 v2 CK_PAT_ID data type.

    Attributes
    ----------
    ck_pat_id_1 : str | None
        CK_PAT_ID.1 (opt) - Patient ID (ST)

    ck_pat_id_2 : str | None
        CK_PAT_ID.2 (opt) - Check digit (NM)

    ck_pat_id_3 : str | None
        CK_PAT_ID.3 (opt) - Check digit scheme (ID)

    ck_pat_id_4 : str | None
        CK_PAT_ID.4 (opt) - Facility ID (ID)
    """

    ck_pat_id_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_1",
            "patient_id",
            "CK_PAT_ID.1",
        ),
        serialization_alias="CK_PAT_ID.1",
        title="Patient ID",
    )

    ck_pat_id_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_2",
            "check_digit",
            "CK_PAT_ID.2",
        ),
        serialization_alias="CK_PAT_ID.2",
        title="Check digit",
    )

    ck_pat_id_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_3",
            "check_digit_scheme",
            "CK_PAT_ID.3",
        ),
        serialization_alias="CK_PAT_ID.3",
        title="Check digit scheme",
    )

    ck_pat_id_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ck_pat_id_4",
            "facility_id",
            "CK_PAT_ID.4",
        ),
        serialization_alias="CK_PAT_ID.4",
        title="Facility ID",
    )

    @field_validator("ck_pat_id_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
