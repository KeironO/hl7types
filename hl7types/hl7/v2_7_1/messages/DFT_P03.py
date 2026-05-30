"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
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
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DFT_P03_COMMON_ORDER import DFT_P03_COMMON_ORDER
from ..groups.DFT_P03_FINANCIAL import DFT_P03_FINANCIAL
from ..groups.DFT_P03_INSURANCE import DFT_P03_INSURANCE
from ..groups.DFT_P03_VISIT import DFT_P03_VISIT

_ACC = ACC
_DB1 = DB1
_DFT_P03_COMMON_ORDER = DFT_P03_COMMON_ORDER
_DFT_P03_FINANCIAL = DFT_P03_FINANCIAL
_DFT_P03_INSURANCE = DFT_P03_INSURANCE
_DFT_P03_VISIT = DFT_P03_VISIT
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_MSH = MSH
_PD1 = PD1
_PID = PID
_ROL = ROL
_SFT = SFT
_UAC = UAC


class DFT_P03(HL7Model):
    """HL7 v2 DFT_P03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        ROL (Optional[List[ROL]]): optional
        VISIT (Optional[DFT_P03_VISIT]): optional
        DB1 (Optional[List[DB1]]): optional
        COMMON_ORDER (Optional[List[DFT_P03_COMMON_ORDER]]): optional
        FINANCIAL (List[DFT_P03_FINANCIAL]): required
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[DRG]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[DFT_P03_INSURANCE]]): optional
        ACC (Optional[ACC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    VISIT: Optional[_DFT_P03_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Optional, repeating",
    )

    COMMON_ORDER: Optional[List[_DFT_P03_COMMON_ORDER]] = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional, repeating",
    )

    FINANCIAL: List[_DFT_P03_FINANCIAL] = Field(
        default=...,
        title="FINANCIAL",
        description="Required, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Optional",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_DFT_P03_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
