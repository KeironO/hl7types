"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OMI_O23.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class OMI_O23_ORDER(HL7Model):
    """HL7 v2 OMI_O23.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[OMI_O23_TIMING]]): optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        CTD (Optional[CTD]): Contact Data, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        OBSERVATION (Optional[List[OMI_O23_OBSERVATION]]): optional
        IPC (List[IPC]): Imaging Procedure Control Segment, required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_OMI_O23_TIMING]] = Field(
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    OBSERVATION: Optional[List[_OMI_O23_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    IPC: List[_IPC] = Field(
        min_length=1,
        title="IPC",
        description="Imaging Procedure Control Segment",
    )

    model_config = {"populate_by_name": True}
