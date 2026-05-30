"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_LICENSE_NO
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_LICENSE_NO(HL7Model):
    """HL7 v2 CM_LICENSE_NO data type.

    Attributes
    ----------
    cm_license_no_1 : str | None
        CM_LICENSE_NO.1 (opt) - License Number (ST)

    cm_license_no_2 : str | None
        CM_LICENSE_NO.2 (opt) - issuing state,province,country (ST)
    """

    cm_license_no_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_license_no_1",
            "license_number",
            "CM_LICENSE_NO.1",
        ),
        serialization_alias="CM_LICENSE_NO.1",
        title="License Number",
    )

    cm_license_no_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_license_no_2",
            "issuing_state_province_country",
            "CM_LICENSE_NO.2",
        ),
        serialization_alias="CM_LICENSE_NO.2",
        title="issuing state,province,country",
    )

    model_config = {"populate_by_name": True}
