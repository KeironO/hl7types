"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADR_A19.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from .ADR_A19_INSURANCE import ADR_A19_INSURANCE
from .ADR_A19_PROCEDURE import ADR_A19_PROCEDURE

_ACC = ACC
_ADR_A19_INSURANCE = ADR_A19_INSURANCE
_ADR_A19_PROCEDURE = ADR_A19_PROCEDURE
_AL1 = AL1
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_NK1 = NK1
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class ADR_A19_QUERY_RESPONSE(HL7Model):
    """HL7 v2 ADR_A19.QUERY_RESPONSE group.

    Attributes:
        EVN (Optional[EVN]): EVN - event type segment, optional
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        PV1 (PV1): PV1 - patient visit segment-, required
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
        DB1 (Optional[List[DB1]]): DB1 - Disability segment, optional
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[DRG]): DRG - diagnosis related group segment, optional
        PROCEDURE (Optional[List[ADR_A19_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): GT1 - guarantor segment, optional
        INSURANCE (Optional[List[ADR_A19_INSURANCE]]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
        UB1 (Optional[UB1]): UB1 - UB82 data segment, optional
        UB2 (Optional[UB2]): UB2 - UB92 data segment, optional
    """

    EVN: Optional[_EVN] = Field(
        default=None,
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

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NK1 - next of kin / associated parties segment-",
    )

    PV1: _PV1 = Field(
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

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="AL1 - patient allergy information segment",
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

    PROCEDURE: Optional[List[_ADR_A19_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="GT1 - guarantor segment",
    )

    INSURANCE: Optional[List[_ADR_A19_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="ACC - accident segment",
    )

    UB1: Optional[_UB1] = Field(
        default=None,
        title="UB1",
        description="UB1 - UB82 data segment",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="UB2 - UB92 data segment",
    )

    model_config = ConfigDict(populate_by_name=True)
