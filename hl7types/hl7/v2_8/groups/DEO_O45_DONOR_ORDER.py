"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DEO_O45.DONOR_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .DEO_O45_DONOR_OBSERVATION import DEO_O45_DONOR_OBSERVATION

_DEO_O45_DONOR_OBSERVATION = DEO_O45_DONOR_OBSERVATION
_NTE = NTE
_OBR = OBR


class DEO_O45_DONOR_ORDER(HL7Model):
    """HL7 v2 DEO_O45.DONOR_ORDER group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        DONOR_OBSERVATION (Optional[List[DEO_O45_DONOR_OBSERVATION]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DONOR_OBSERVATION: Optional[List[_DEO_O45_DONOR_OBSERVATION]] = Field(
        default=None,
        title="DONOR_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
