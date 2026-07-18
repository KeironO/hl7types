"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PDA import PDA
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL

from ..groups.ADT_A03_PROCEDURE import ADT_A03_PROCEDURE

_ADT_A03_PROCEDURE = ADT_A03_PROCEDURE
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_MSH = MSH
_OBX = OBX
_PD1 = PD1
_PDA = PDA
_PID = PID
_PV1 = PV1
_PV2 = PV2
_ROL = ROL


class ADT_A03(HL7Model):
    """ADT/ACK -  Discharge/end visit (S3).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        PROCEDURE (Optional[List[ADT_A03_PROCEDURE]]): optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        PDA (Optional[PDA]): Patient death and autopsy, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="patient additional demographic",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
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
        description="Disability",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    PROCEDURE: Optional[List[_ADT_A03_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    PDA: Optional[_PDA] = Field(
        default=None,
        title="PDA",
        description="Patient death and autopsy",
    )

    model_config = ConfigDict(populate_by_name=True)
