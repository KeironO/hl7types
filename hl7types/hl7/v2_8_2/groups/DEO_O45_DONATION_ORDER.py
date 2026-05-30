"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DEO_O45.DONATION_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .DEO_O45_DONATION_OBSERVATION import DEO_O45_DONATION_OBSERVATION

_DEO_O45_DONATION_OBSERVATION = DEO_O45_DONATION_OBSERVATION
_NTE = NTE
_OBR = OBR


class DEO_O45_DONATION_ORDER(HL7Model):
    """HL7 v2 DEO_O45.DONATION_ORDER group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        DONATION_OBSERVATION (Optional[List[DEO_O45_DONATION_OBSERVATION]]): optional
    """

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

    DONATION_OBSERVATION: Optional[List[_DEO_O45_DONATION_OBSERVATION]] = Field(
        default=None,
        title="DONATION_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
