"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORU_R30
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.SFT import SFT

from ..groups.ORU_R30_OBSERVATION import ORU_R30_OBSERVATION
from ..groups.ORU_R30_TIMING_QTY import ORU_R30_TIMING_QTY
from ..groups.ORU_R30_VISIT import ORU_R30_VISIT

_MSH = MSH
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R30_OBSERVATION = ORU_R30_OBSERVATION
_ORU_R30_TIMING_QTY = ORU_R30_TIMING_QTY
_ORU_R30_VISIT = ORU_R30_VISIT
_PD1 = PD1
_PID = PID
_SFT = SFT


class ORU_R30(HL7Model):
    """ORU - Unsolicited Point-Of-Care Observation Message Without Existing Order - Pla (S5.7.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        VISIT (Optional[ORU_R30_VISIT]): optional
        ORC (ORC): Common Order, required
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
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

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
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

    TIMING_QTY: Optional[List[_ORU_R30_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    OBSERVATION: List[_ORU_R30_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
