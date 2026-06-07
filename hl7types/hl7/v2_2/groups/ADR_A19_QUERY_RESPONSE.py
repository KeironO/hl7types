"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADR_A19.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PR1 import PR1
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from .ADR_A19_INSURANCE import ADR_A19_INSURANCE

_ACC = ACC
_ADR_A19_INSURANCE = ADR_A19_INSURANCE
_AL1 = AL1
_DG1 = DG1
_EVN = EVN
_GT1 = GT1
_NK1 = NK1
_OBX = OBX
_PID = PID
_PR1 = PR1
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class ADR_A19_QUERY_RESPONSE(HL7Model):
    """HL7 v2 ADR_A19.QUERY_RESPONSE group.

    Attributes:
        EVN (Optional[EVN]): optional
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        OBX (Optional[List[OBX]]): optional
        AL1 (Optional[List[AL1]]): optional
        DG1 (Optional[List[DG1]]): optional
        PR1 (Optional[List[PR1]]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[ADR_A19_INSURANCE]]): optional
        ACC (Optional[ACC]): optional
        UB1 (Optional[UB1]): optional
        UB2 (Optional[UB2]): optional
    """

    EVN: Optional[_EVN] = Field(
        default=None,
        title="EVN",
        description="Optional",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Required",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    PR1: Optional[List[_PR1]] = Field(
        default=None,
        title="PR1",
        description="Optional, repeating",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_ADR_A19_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Optional",
    )

    UB1: Optional[_UB1] = Field(
        default=None,
        title="UB1",
        description="Optional",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
