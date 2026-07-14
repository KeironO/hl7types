"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMQ_O57.ORDER_DOCUMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.SGH import SGH
from ..segments.SGT import SGT
from ..segments.TXA import TXA

_NTE = NTE
_OBX = OBX
_PRT = PRT
_SGH = SGH
_SGT = SGT
_TXA = TXA


class OMQ_O57_ORDER_DOCUMENT(HL7Model):
    """HL7 v2 OMQ_O57.ORDER_DOCUMENT group.

    Attributes:
        SGH (SGH): Segment Group Header, required
        OBX (OBX): Observation/Result, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TXA (Optional[TXA]): Transcription Document Header, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        SGT (SGT): Segment Group Trailer, required
    """

    SGH: _SGH = Field(
        title="SGH",
        description="Segment Group Header",
    )

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TXA: Optional[_TXA] = Field(
        default=None,
        title="TXA",
        description="Transcription Document Header",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    SGT: _SGT = Field(
        title="SGT",
        description="Segment Group Trailer",
    )

    model_config = {"populate_by_name": True}
