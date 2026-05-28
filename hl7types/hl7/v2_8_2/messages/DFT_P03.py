"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DFT_P03_COMMON_ORDER import DFT_P03_COMMON_ORDER
from ..groups.DFT_P03_FINANCIAL import DFT_P03_FINANCIAL
from ..groups.DFT_P03_INSURANCE import DFT_P03_INSURANCE
from ..groups.DFT_P03_VISIT import DFT_P03_VISIT
from ..segments.ACC import ACC
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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
_PRT = PRT
_PV1 = PV1
_ROL = ROL
_SFT = SFT
_UAC = UAC


class DFT_P03(BaseModel):
    """HL7 v2 DFT_P03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
        PV1 (Optional[PV1]): optional
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

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    VISIT: _DFT_P03_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    DB1: list[_DB1] | None = Field(
        default=None,
        title="DB1",
        description="Optional, repeating",
    )

    COMMON_ORDER: list[_DFT_P03_COMMON_ORDER] | None = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional, repeating",
    )

    FINANCIAL: list[_DFT_P03_FINANCIAL] = Field(
        default=...,
        title="FINANCIAL",
        description="Required, repeating",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: _DRG | None = Field(
        default=None,
        title="DRG",
        description="Optional",
    )

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: list[_DFT_P03_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ACC: _ACC | None = Field(
        default=None,
        title="ACC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
