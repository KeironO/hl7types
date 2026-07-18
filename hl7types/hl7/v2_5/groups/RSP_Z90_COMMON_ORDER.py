"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z90.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .RSP_Z90_OBSERVATION import RSP_Z90_OBSERVATION
from .RSP_Z90_TIMING import RSP_Z90_TIMING

_CTD = CTD
_NTE = NTE
_OBR = OBR
_ORC = ORC
_RSP_Z90_OBSERVATION = RSP_Z90_OBSERVATION
_RSP_Z90_TIMING = RSP_Z90_TIMING


class RSP_Z90_COMMON_ORDER(HL7Model):
    """HL7 v2 RSP_Z90.COMMON_ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[RSP_Z90_TIMING]]): optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        CTD (Optional[CTD]): Contact Data, optional
        OBSERVATION (List[RSP_Z90_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_RSP_Z90_TIMING]] = Field(
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

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    OBSERVATION: List[_RSP_Z90_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
