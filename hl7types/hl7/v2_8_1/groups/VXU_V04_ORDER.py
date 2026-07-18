"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: VXU_V04.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .VXU_V04_OBSERVATION import VXU_V04_OBSERVATION
from .VXU_V04_TIMING import VXU_V04_TIMING

_ORC = ORC
_PRT = PRT
_RXA = RXA
_RXR = RXR
_VXU_V04_OBSERVATION = VXU_V04_OBSERVATION
_VXU_V04_TIMING = VXU_V04_TIMING


class VXU_V04_ORDER(HL7Model):
    """HL7 v2 VXU_V04.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING (Optional[List[VXU_V04_TIMING]]): optional
        RXA (RXA): Pharmacy/Treatment Administration, required
        RXR (Optional[RXR]): Pharmacy/Treatment Route, optional
        OBSERVATION (Optional[List[VXU_V04_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING: Optional[List[_VXU_V04_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    OBSERVATION: Optional[List[_VXU_V04_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
