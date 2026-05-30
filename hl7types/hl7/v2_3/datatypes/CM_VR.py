"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_VR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_VR(HL7Model):
    """HL7 v2 CM_VR data type.

    Attributes
    ----------
    cm_vr_1 : str | None
        CM_VR.1 (opt) - first data code value (ST)

    cm_vr_2 : str | None
        CM_VR.2 (opt) - Last data code calue (ST)
    """

    cm_vr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_vr_1",
            "first_data_code_value",
            "CM_VR.1",
        ),
        serialization_alias="CM_VR.1",
        title="first data code value",
    )

    cm_vr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_vr_2",
            "last_data_code_calue",
            "CM_VR.2",
        ),
        serialization_alias="CM_VR.2",
        title="Last data code calue",
    )

    model_config = {"populate_by_name": True}
