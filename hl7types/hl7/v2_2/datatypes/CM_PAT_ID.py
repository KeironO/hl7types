"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PAT_ID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_PAT_ID(HL7Model):
    """HL7 v2 CM_PAT_ID data type.

    Attributes
    ----------
    cm_pat_id_1 : str | None
        CM_PAT_ID.1 (opt) - Patient ID (ST)

    cm_pat_id_2 : str | None
        CM_PAT_ID.2 (opt) - Check digit (NM)

    cm_pat_id_3 : str | None
        CM_PAT_ID.3 (opt) - Check digit scheme (ID)

    cm_pat_id_4 : str | None
        CM_PAT_ID.4 (opt) - Facility ID (ID)

    cm_pat_id_5 : str | None
        CM_PAT_ID.5 (opt) - type (ID)
    """

    cm_pat_id_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_1",
            "patient_id",
            "CM_PAT_ID.1",
        ),
        serialization_alias="CM_PAT_ID.1",
        title="Patient ID",
    )

    cm_pat_id_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_2",
            "check_digit",
            "CM_PAT_ID.2",
        ),
        serialization_alias="CM_PAT_ID.2",
        title="Check digit",
    )

    cm_pat_id_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_3",
            "check_digit_scheme",
            "CM_PAT_ID.3",
        ),
        serialization_alias="CM_PAT_ID.3",
        title="Check digit scheme",
    )

    cm_pat_id_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_4",
            "facility_id",
            "CM_PAT_ID.4",
        ),
        serialization_alias="CM_PAT_ID.4",
        title="Facility ID",
    )

    cm_pat_id_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pat_id_5",
            "type_",
            "CM_PAT_ID.5",
        ),
        serialization_alias="CM_PAT_ID.5",
        title="type",
    )

    model_config = {"populate_by_name": True}
