"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORI_O24.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        ORC (ORC): required
        TIMING (Optional[List[ORI_O24_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        IPC (List[IPC]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_ORI_O24_TIMING]] = Field(
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    IPC: List[_IPC] = Field(
        default=...,
        title="IPC",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
