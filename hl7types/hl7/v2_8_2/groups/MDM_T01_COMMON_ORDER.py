"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MDM_T01.COMMON_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .MDM_T01_TIMING import MDM_T01_TIMING

_MDM_T01_TIMING = MDM_T01_TIMING
_NTE = NTE
_OBR = OBR
_ORC = ORC


class MDM_T01_COMMON_ORDER(BaseModel):
    """HL7 v2 MDM_T01.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[MDM_T01_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_MDM_T01_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
