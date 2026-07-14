"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MDM_T01.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .MDM_T01_TIMING import MDM_T01_TIMING

_MDM_T01_TIMING = MDM_T01_TIMING
_NTE = NTE
_OBR = OBR
_ORC = ORC


class MDM_T01_COMMON_ORDER(HL7Model):
    """HL7 v2 MDM_T01.COMMON_ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[MDM_T01_TIMING]]): optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_MDM_T01_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
