"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PAT_ID_0192
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class CM_PAT_ID_0192(HL7Model):
    """HL7 v2 CM_PAT_ID_0192 data type.

    Attributes
    ----------
    cm_pat_id_0192_1 : str | None
        CM_PAT_ID_0192.1 (opt) - Patient ID (ST)

    cm_pat_id_0192_2 : str | None
        CM_PAT_ID_0192.2 (opt) - Check digit (NM)

    cm_pat_id_0192_3 : str | None
        CM_PAT_ID_0192.3 (opt) - Check digit scheme (ID)

    cm_pat_id_0192_4 : str | None
        CM_PAT_ID_0192.4 (opt) - Facility ID (ID)

    cm_pat_id_0192_5 : str | None
        CM_PAT_ID_0192.5 (opt) - type (ID)
    """

    cm_pat_id_0192_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_0192_1",
            "patient_id",
            "CM_PAT_ID_0192.1",
        ),
        serialization_alias="CM_PAT_ID_0192.1",
        title="Patient ID",
    )

    cm_pat_id_0192_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_0192_2",
            "check_digit",
            "CM_PAT_ID_0192.2",
        ),
        serialization_alias="CM_PAT_ID_0192.2",
        title="Check digit",
    )

    cm_pat_id_0192_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_0192_3",
            "check_digit_scheme",
            "CM_PAT_ID_0192.3",
        ),
        serialization_alias="CM_PAT_ID_0192.3",
        title="Check digit scheme",
    )

    cm_pat_id_0192_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_0192_4",
            "facility_id",
            "CM_PAT_ID_0192.4",
        ),
        serialization_alias="CM_PAT_ID_0192.4",
        title="Facility ID",
    )

    cm_pat_id_0192_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_0192_5",
            "type_",
            "CM_PAT_ID_0192.5",
        ),
        serialization_alias="CM_PAT_ID_0192.5",
        title="type",
    )

    @field_validator("cm_pat_id_0192_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
