"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: VR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class VR(HL7Model):
    """Value range (S2.A.83).

    Attributes
    ----------
    vr_1 : str | None
        VR.1 (opt) - First Data Code Value (ST)

    vr_2 : str | None
        VR.2 (opt) - Last Data Code Value (ST)
    """

    vr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_1",
            "first_data_code_value",
            "VR.1",
        ),
        serialization_alias="VR.1",
        title="First Data Code Value",
    )

    vr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vr_2",
            "last_data_code_value",
            "VR.2",
        ),
        serialization_alias="VR.2",
        title="Last Data Code Value",
    )

    model_config = ConfigDict(populate_by_name=True)
