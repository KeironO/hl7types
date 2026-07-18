"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORI_O24.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IPC import IPC
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .ORI_O24_TIMING import ORI_O24_TIMING

_IPC = IPC
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORI_O24_TIMING = ORI_O24_TIMING
_PRT = PRT


class ORI_O24_ORDER(HL7Model):
    """HL7 v2 ORI_O24.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING (Optional[List[ORI_O24_TIMING]]): optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        IPC (List[IPC]): Imaging Procedure Control Segment, required
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

    TIMING: Optional[List[_ORI_O24_TIMING]] = Field(
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

    IPC: List[_IPC] = Field(
        min_length=1,
        title="IPC",
        description="Imaging Procedure Control Segment",
    )

    model_config = ConfigDict(populate_by_name=True)
