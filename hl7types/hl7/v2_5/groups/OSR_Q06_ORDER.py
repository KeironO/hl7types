"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OSR_Q06.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .OSR_Q06_CHOICE import OSR_Q06_CHOICE
from .OSR_Q06_TIMING import OSR_Q06_TIMING

_CTI = CTI
_NTE = NTE
_ORC = ORC
_OSR_Q06_CHOICE = OSR_Q06_CHOICE
_OSR_Q06_TIMING = OSR_Q06_TIMING


class OSR_Q06_ORDER(BaseModel):
    """HL7 v2 OSR_Q06.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[OSR_Q06_TIMING]]): optional
        CHOICE (OSR_Q06_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_OSR_Q06_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    CHOICE: _OSR_Q06_CHOICE = Field(
        default=...,
        title="CHOICE",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
