"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class VR(BaseModel):
    """HL7 v2 VR data type.

    Attributes
    ----------
    vr_1 : str | None
        VR.1 (opt) - first data code value (ST)

    vr_2 : str | None
        VR.2 (opt) - Last data code calue (ST)
    """

    vr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_1",
            "first_data_code_value",
            "VR.1",
        ),
        serialization_alias="VR.1",
        title="first data code value",
    )

    vr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_2",
            "last_data_code_calue",
            "VR.2",
        ),
        serialization_alias="VR.2",
        title="Last data code calue",
    )

    model_config = {"populate_by_name": True}
