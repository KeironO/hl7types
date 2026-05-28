"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RPA_I08
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RPA_I08_AUTHORIZATION import RPA_I08_AUTHORIZATION
from ..groups.RPA_I08_INSURANCE import RPA_I08_INSURANCE
from ..groups.RPA_I08_OBSERVATION import RPA_I08_OBSERVATION
from ..groups.RPA_I08_PROCEDURE import RPA_I08_PROCEDURE
from ..groups.RPA_I08_PROVIDER import RPA_I08_PROVIDER
from ..groups.RPA_I08_VISIT import RPA_I08_VISIT
from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.GT1 import GT1
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1
from ..segments.SFT import SFT

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_GT1 = GT1
_MSA = MSA
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RF1 = RF1
_RPA_I08_AUTHORIZATION = RPA_I08_AUTHORIZATION
_RPA_I08_INSURANCE = RPA_I08_INSURANCE
_RPA_I08_OBSERVATION = RPA_I08_OBSERVATION
_RPA_I08_PROCEDURE = RPA_I08_PROCEDURE
_RPA_I08_PROVIDER = RPA_I08_PROVIDER
_RPA_I08_VISIT = RPA_I08_VISIT
_SFT = SFT


class RPA_I08(BaseModel):
    """HL7 v2 RPA_I08 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        RF1 (Optional[RF1]): optional
        AUTHORIZATION (Optional[RPA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RPA_I08_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[RPA_I08_INSURANCE]]): optional
        ACC (Optional[ACC]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        PROCEDURE (List[RPA_I08_PROCEDURE]): required
        OBSERVATION (Optional[List[RPA_I08_OBSERVATION]]): optional
        VISIT (Optional[RPA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): optional
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

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    RF1: _RF1 | None = Field(
        default=None,
        title="RF1",
        description="Optional",
    )

    AUTHORIZATION: _RPA_I08_AUTHORIZATION | None = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    PROVIDER: list[_RPA_I08_PROVIDER] = Field(
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

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: list[_RPA_I08_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
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

    PROCEDURE: list[_RPA_I08_PROCEDURE] = Field(
        default=...,
        title="PROCEDURE",
        description="Required, repeating",
    )

    OBSERVATION: list[_RPA_I08_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: _RPA_I08_VISIT | None = Field(
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
