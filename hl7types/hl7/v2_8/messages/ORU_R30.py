"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORU_R30
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ORU_R30_OBSERVATION import ORU_R30_OBSERVATION
from ..groups.ORU_R30_PATIENT_OBSERVATION import ORU_R30_PATIENT_OBSERVATION
from ..groups.ORU_R30_TIMING_QTY import ORU_R30_TIMING_QTY
from ..groups.ORU_R30_VISIT import ORU_R30_VISIT
from ..segments.ARV import ARV
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ARV = ARV
_MSH = MSH
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R30_OBSERVATION = ORU_R30_OBSERVATION
_ORU_R30_PATIENT_OBSERVATION = ORU_R30_PATIENT_OBSERVATION
_ORU_R30_TIMING_QTY = ORU_R30_TIMING_QTY
_ORU_R30_VISIT = ORU_R30_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT
_SFT = SFT
_UAC = UAC


class ORU_R30(BaseModel):
    """HL7 v2 ORU_R30 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_OBSERVATION (Optional[List[ORU_R30_PATIENT_OBSERVATION]]): optional
        VISIT (Optional[ORU_R30_VISIT]): optional
        ORC (ORC): required
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[ORU_R30_TIMING_QTY]]): optional
        OBSERVATION (List[ORU_R30_OBSERVATION]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    PATIENT_OBSERVATION: list[_ORU_R30_PATIENT_OBSERVATION] | None = Field(
        default=None,
        title="PATIENT_OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: _ORU_R30_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_ORU_R30_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    OBSERVATION: list[_ORU_R30_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
