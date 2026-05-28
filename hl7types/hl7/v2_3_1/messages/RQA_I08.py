"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RQA_I08
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RQA_I08_AUTHORIZATION import RQA_I08_AUTHORIZATION
from ..groups.RQA_I08_GUARANTOR_INSURANCE import RQA_I08_GUARANTOR_INSURANCE
from ..groups.RQA_I08_OBSERVATION import RQA_I08_OBSERVATION
from ..groups.RQA_I08_PROCEDURE import RQA_I08_PROCEDURE
from ..groups.RQA_I08_PROVIDER import RQA_I08_PROVIDER
from ..groups.RQA_I08_VISIT import RQA_I08_VISIT
from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RF1 = RF1
_RQA_I08_AUTHORIZATION = RQA_I08_AUTHORIZATION
_RQA_I08_GUARANTOR_INSURANCE = RQA_I08_GUARANTOR_INSURANCE
_RQA_I08_OBSERVATION = RQA_I08_OBSERVATION
_RQA_I08_PROCEDURE = RQA_I08_PROCEDURE
_RQA_I08_PROVIDER = RQA_I08_PROVIDER
_RQA_I08_VISIT = RQA_I08_VISIT


class RQA_I08(BaseModel):
    """HL7 v2 RQA_I08 message.

    Attributes:
        MSH (MSH): required
        RF1 (Optional[RF1]): optional
        AUTHORIZATION (Optional[RQA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RQA_I08_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[RQA_I08_GUARANTOR_INSURANCE]): optional
        ACC (Optional[ACC]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        PROCEDURE (Optional[List[RQA_I08_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RQA_I08_OBSERVATION]]): optional
        VISIT (Optional[RQA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    RF1: _RF1 | None = Field(
        default=None,
        title="RF1",
        description="Optional",
    )

    AUTHORIZATION: _RQA_I08_AUTHORIZATION | None = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    PROVIDER: list[_RQA_I08_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GUARANTOR_INSURANCE: _RQA_I08_GUARANTOR_INSURANCE | None = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
        description="Optional",
    )

    ACC: _ACC | None = Field(
        default=None,
        title="ACC",
        description="Optional",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: list[_DRG] | None = Field(
        default=None,
        title="DRG",
        description="Optional, repeating",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PROCEDURE: list[_RQA_I08_PROCEDURE] | None = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    OBSERVATION: list[_RQA_I08_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: _RQA_I08_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
