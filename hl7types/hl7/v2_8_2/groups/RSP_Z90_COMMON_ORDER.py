"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_Z90.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        ORC (ORC): required
        TIMING (Optional[List[RSP_Z90_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION (List[RSP_Z90_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_RSP_Z90_TIMING]] = Field(
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

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBSERVATION: List[_RSP_Z90_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
