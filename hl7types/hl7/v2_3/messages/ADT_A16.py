"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A16
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_MSH = MSH
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2


class ADT_A16(HL7Model):
    """ADT/ACK -  Pending discharge.

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
        OBX (Optional[List[OBX]]): Observation segment, optional
        DG1 (Optional[DG1]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Demographic",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient visit - additional information",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Disability Segment",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation segment",
    )

    DG1: Optional[_DG1] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    model_config = {"populate_by_name": True}
