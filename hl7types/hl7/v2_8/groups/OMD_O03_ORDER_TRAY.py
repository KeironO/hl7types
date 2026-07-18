"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OMD_O03.ORDER_TRAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODT import ODT
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OMD_O03_TIMING_TRAY import OMD_O03_TIMING_TRAY

_NTE = NTE
_ODT = ODT
_OMD_O03_TIMING_TRAY = OMD_O03_TIMING_TRAY
_ORC = ORC
_PRT = PRT


class OMD_O03_ORDER_TRAY(HL7Model):
    """HL7 v2 OMD_O03.ORDER_TRAY group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING_TRAY (Optional[List[OMD_O03_TIMING_TRAY]]): optional
        ODT (List[ODT]): Diet Tray Instructions, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
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

    TIMING_TRAY: Optional[List[_OMD_O03_TIMING_TRAY]] = Field(
        default=None,
        title="TIMING_TRAY",
    )

    ODT: List[_ODT] = Field(
        min_length=1,
        title="ODT",
        description="Diet Tray Instructions",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
