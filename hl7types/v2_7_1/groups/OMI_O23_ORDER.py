"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMI_O23.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.DG1 import DG1
from ..segments.IPC import IPC
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OMI_O23_OBSERVATION import OMI_O23_OBSERVATION
from .OMI_O23_TIMING import OMI_O23_TIMING

_CTD = CTD
_DG1 = DG1
_IPC = IPC
_NTE = NTE
_OBR = OBR
_OMI_O23_OBSERVATION = OMI_O23_OBSERVATION
_OMI_O23_TIMING = OMI_O23_TIMING
_ORC = ORC
_PRT = PRT


class OMI_O23_ORDER(BaseModel):
    """HL7 v2 OMI_O23.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[OMI_O23_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OMI_O23_OBSERVATION]]): optional
        IPC (List[IPC]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_OMI_O23_TIMING]] = Field(
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

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OMI_O23_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    IPC: List[_IPC] = Field(
        default=...,
        title="IPC",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
