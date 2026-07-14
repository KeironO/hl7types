"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: DFT_P03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL
from ..segments.SFT import SFT

from ..groups.DFT_P03_COMMON_ORDER import DFT_P03_COMMON_ORDER
from ..groups.DFT_P03_FINANCIAL import DFT_P03_FINANCIAL
from ..groups.DFT_P03_INSURANCE import DFT_P03_INSURANCE

_ACC = ACC
_DB1 = DB1
_DFT_P03_COMMON_ORDER = DFT_P03_COMMON_ORDER
_DFT_P03_FINANCIAL = DFT_P03_FINANCIAL
_DFT_P03_INSURANCE = DFT_P03_INSURANCE
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_ROL = ROL
_SFT = SFT


class DFT_P03(HL7Model):
    """DFT/ACK - Post detail financial transaction (S6.4.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        PV1 (Optional[PV1]): Patient Visit, optional
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        COMMON_ORDER (Optional[List[DFT_P03_COMMON_ORDER]]): optional
        FINANCIAL (List[DFT_P03_FINANCIAL]): required
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[DFT_P03_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
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

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
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

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Disability",
    )

    COMMON_ORDER: Optional[List[_DFT_P03_COMMON_ORDER]] = Field(
        default=None,
        title="COMMON_ORDER",
    )

    FINANCIAL: List[_DFT_P03_FINANCIAL] = Field(
        min_length=1,
        title="FINANCIAL",
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

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_DFT_P03_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    model_config = {"populate_by_name": True}
