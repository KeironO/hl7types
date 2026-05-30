"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RPA_I08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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

from ..groups.RPA_I08_AUTHORIZATION import RPA_I08_AUTHORIZATION
from ..groups.RPA_I08_INSURANCE import RPA_I08_INSURANCE
from ..groups.RPA_I08_OBSERVATION import RPA_I08_OBSERVATION
from ..groups.RPA_I08_PROCEDURE import RPA_I08_PROCEDURE
from ..groups.RPA_I08_PROVIDER import RPA_I08_PROVIDER
from ..groups.RPA_I08_VISIT import RPA_I08_VISIT

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


class RPA_I08(HL7Model):
    """HL7 v2 RPA_I08 message.

    Attributes:
        MSH (MSH): required
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

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Optional",
    )

    AUTHORIZATION: Optional[_RPA_I08_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    PROVIDER: List[_RPA_I08_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_RPA_I08_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Optional",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: Optional[List[_DRG]] = Field(
        default=None,
        title="DRG",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PROCEDURE: List[_RPA_I08_PROCEDURE] = Field(
        default=...,
        title="PROCEDURE",
        description="Required, repeating",
    )

    OBSERVATION: Optional[List[_RPA_I08_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: Optional[_RPA_I08_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
