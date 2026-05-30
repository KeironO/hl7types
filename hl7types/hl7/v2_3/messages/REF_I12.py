"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: REF_I12
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
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1

from ..groups.REF_I12_AUTHORIZATION import REF_I12_AUTHORIZATION
from ..groups.REF_I12_INSURANCE import REF_I12_INSURANCE
from ..groups.REF_I12_PROCEDURE import REF_I12_PROCEDURE
from ..groups.REF_I12_PROVIDER import REF_I12_PROVIDER
from ..groups.REF_I12_RESULTS import REF_I12_RESULTS
from ..groups.REF_I12_VISIT import REF_I12_VISIT

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_REF_I12_AUTHORIZATION = REF_I12_AUTHORIZATION
_REF_I12_INSURANCE = REF_I12_INSURANCE
_REF_I12_PROCEDURE = REF_I12_PROCEDURE
_REF_I12_PROVIDER = REF_I12_PROVIDER
_REF_I12_RESULTS = REF_I12_RESULTS
_REF_I12_VISIT = REF_I12_VISIT
_RF1 = RF1


class REF_I12(HL7Model):
    """HL7 v2 REF_I12 message.

    Attributes:
        MSH (MSH): required
        RF1 (Optional[RF1]): optional
        AUTHORIZATION (Optional[REF_I12_AUTHORIZATION]): optional
        PROVIDER (List[REF_I12_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[REF_I12_INSURANCE]]): optional
        ACC (Optional[ACC]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        PROCEDURE (Optional[List[REF_I12_PROCEDURE]]): optional
        RESULTS (Optional[List[REF_I12_RESULTS]]): optional
        VISIT (Optional[REF_I12_VISIT]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Optional",
    )

    AUTHORIZATION: Optional[_REF_I12_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    PROVIDER: List[_REF_I12_PROVIDER] = Field(
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

    INSURANCE: Optional[List[_REF_I12_INSURANCE]] = Field(
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

    PROCEDURE: Optional[List[_REF_I12_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    RESULTS: Optional[List[_REF_I12_RESULTS]] = Field(
        default=None,
        title="RESULTS",
        description="Optional, repeating",
    )

    VISIT: Optional[_REF_I12_VISIT] = Field(
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
