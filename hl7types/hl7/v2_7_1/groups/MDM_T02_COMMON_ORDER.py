"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MDM_T02.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (ORC): Common Order, required
        TIMING (Optional[List[MDM_T02_TIMING]]): optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_MDM_T02_TIMING]] = Field(
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

    model_config = ConfigDict(populate_by_name=True)
