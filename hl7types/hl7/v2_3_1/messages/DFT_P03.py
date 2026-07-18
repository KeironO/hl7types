"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DFT_P03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

from ..groups.DFT_P03_FINANCIAL import DFT_P03_FINANCIAL
from ..groups.DFT_P03_INSURANCE import DFT_P03_INSURANCE

_ACC = ACC
_DB1 = DB1
_DFT_P03_FINANCIAL = DFT_P03_FINANCIAL
_DFT_P03_INSURANCE = DFT_P03_INSURANCE
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_MSH = MSH
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2


class DFT_P03(HL7Model):
    """DFT/ACK - Post detail financial transaction.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        PV1 (Optional[PV1]): PV1 - patient visit segment-, optional
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
        DB1 (Optional[List[DB1]]): DB1 - Disability segment, optional
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
        FINANCIAL (List[DFT_P03_FINANCIAL]): required
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[DRG]): DRG - diagnosis related group segment, optional
        GT1 (Optional[List[GT1]]): GT1 - guarantor segment, optional
        INSURANCE (Optional[List[DFT_P03_INSURANCE]]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVN - event type segment",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="PD1 - patient additional demographic segment",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PV1 - patient visit segment-",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="PV2 - patient visit - additional information segment",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="DB1 - Disability segment",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="OBX - observation/result segment",
    )

    FINANCIAL: List[_DFT_P03_FINANCIAL] = Field(
        min_length=1,
        title="FINANCIAL",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="DG1 - diagnosis segment",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="DRG - diagnosis related group segment",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="GT1 - guarantor segment",
    )

    INSURANCE: Optional[List[_DFT_P03_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="ACC - accident segment",
    )

    model_config = ConfigDict(populate_by_name=True)
