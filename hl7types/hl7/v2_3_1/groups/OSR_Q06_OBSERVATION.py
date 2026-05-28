"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OSR_Q06.OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from .OSR_Q06_CHOICE import OSR_Q06_CHOICE

_CTI = CTI
_NTE = NTE
_ORC = ORC
_OSR_Q06_CHOICE = OSR_Q06_CHOICE


class OSR_Q06_OBSERVATION(BaseModel):
    """HL7 v2 OSR_Q06.OBSERVATION group.

    Attributes:
        ORC (ORC): required
        CHOICE (OSR_Q06_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    CHOICE: _OSR_Q06_CHOICE = Field(
        default=...,
        title="CHOICE",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
