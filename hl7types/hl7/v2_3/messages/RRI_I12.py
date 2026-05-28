"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRI_I12
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RRI_I12_AUTHORIZATION import RRI_I12_AUTHORIZATION
from ..groups.RRI_I12_PROCEDURE import RRI_I12_PROCEDURE
from ..groups.RRI_I12_PROVIDER import RRI_I12_PROVIDER
from ..groups.RRI_I12_RESULTS import RRI_I12_RESULTS
from ..groups.RRI_I12_VISIT import RRI_I12_VISIT
from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RF1 = RF1
_RRI_I12_AUTHORIZATION = RRI_I12_AUTHORIZATION
_RRI_I12_PROCEDURE = RRI_I12_PROCEDURE
_RRI_I12_PROVIDER = RRI_I12_PROVIDER
_RRI_I12_RESULTS = RRI_I12_RESULTS
_RRI_I12_VISIT = RRI_I12_VISIT


class RRI_I12(BaseModel):
    """HL7 v2 RRI_I12 message.

    Attributes:
        MSH (MSH): required
        MSA (Optional[MSA]): optional
        RF1 (Optional[RF1]): optional
        AUTHORIZATION (Optional[RRI_I12_AUTHORIZATION]): optional
        PROVIDER (List[RRI_I12_PROVIDER]): required
        PID (PID): required
        ACC (Optional[ACC]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        PROCEDURE (Optional[List[RRI_I12_PROCEDURE]]): optional
        RESULTS (Optional[List[RRI_I12_RESULTS]]): optional
        VISIT (Optional[RRI_I12_VISIT]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA | None = Field(
        default=None,
        title="MSA",
        description="Optional",
    )

    RF1: _RF1 | None = Field(
        default=None,
        title="RF1",
        description="Optional",
    )

    AUTHORIZATION: _RRI_I12_AUTHORIZATION | None = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    PROVIDER: list[_RRI_I12_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
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

    PROCEDURE: list[_RRI_I12_PROCEDURE] | None = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    RESULTS: list[_RRI_I12_RESULTS] | None = Field(
        default=None,
        title="RESULTS",
        description="Optional, repeating",
    )

    VISIT: _RRI_I12_VISIT | None = Field(
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
