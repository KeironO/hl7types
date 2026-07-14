"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORU_R30
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ORU_R30_OBSERVATION import ORU_R30_OBSERVATION
from ..groups.ORU_R30_TIMING_QTY import ORU_R30_TIMING_QTY
from ..groups.ORU_R30_VISIT import ORU_R30_VISIT

_MSH = MSH
_NTE = NTE
_OBR = OBR
_OBX = OBX
_ORC = ORC
_ORU_R30_OBSERVATION = ORU_R30_OBSERVATION
_ORU_R30_TIMING_QTY = ORU_R30_TIMING_QTY
_ORU_R30_VISIT = ORU_R30_VISIT
_PD1 = PD1
_PID = PID
_ROL = ROL
_SFT = SFT
_UAC = UAC


class ORU_R30(HL7Model):
    """ORU - Unsolicited Point-Of-Care Observation Message Without Existing Order - Pla (S5.7.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        VISIT (Optional[ORU_R30_VISIT]): optional
        ORC (ORC): Common Order, required
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ROL (Optional[List[ROL]]): Role, optional
        TIMING_QTY (Optional[List[ORU_R30_TIMING_QTY]]): optional
        OBSERVATION (List[ORU_R30_OBSERVATION]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    VISIT: Optional[_ORU_R30_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
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

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    TIMING_QTY: Optional[List[_ORU_R30_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    OBSERVATION: List[_ORU_R30_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
