"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MDM_T02.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .MDM_T02_TIMING import MDM_T02_TIMING

_MDM_T02_TIMING = MDM_T02_TIMING
_NTE = NTE
_OBR = OBR
_ORC = ORC


class MDM_T02_COMMON_ORDER(HL7Model):
    """HL7 v2 MDM_T02.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[MDM_T02_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_MDM_T02_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
