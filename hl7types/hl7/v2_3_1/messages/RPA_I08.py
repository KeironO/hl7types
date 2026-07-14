"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
    """RQA/RPA - Request for treatment authorization information.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        RF1 (Optional[RF1]): Referral Infomation, optional
        AUTHORIZATION (Optional[RPA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RPA_I08_PROVIDER]): required
        PID (PID): PID - patient identification segment, required
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        GT1 (Optional[List[GT1]]): GT1 - guarantor segment, optional
        INSURANCE (Optional[List[RPA_I08_INSURANCE]]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[List[DRG]]): DRG - diagnosis related group segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        PROCEDURE (List[RPA_I08_PROCEDURE]): required
        OBSERVATION (Optional[List[RPA_I08_OBSERVATION]]): optional
        VISIT (Optional[RPA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Infomation",
    )

    AUTHORIZATION: Optional[_RPA_I08_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
    )

    PROVIDER: List[_RPA_I08_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NK1 - next of kin / associated parties segment-",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="GT1 - guarantor segment",
    )

    INSURANCE: Optional[List[_RPA_I08_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="ACC - accident segment",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="DG1 - diagnosis segment",
    )

    DRG: Optional[List[_DRG]] = Field(
        default=None,
        title="DRG",
        description="DRG - diagnosis related group segment",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="AL1 - patient allergy information segment",
    )

    PROCEDURE: List[_RPA_I08_PROCEDURE] = Field(
        min_length=1,
        title="PROCEDURE",
    )

    OBSERVATION: Optional[List[_RPA_I08_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    VISIT: Optional[_RPA_I08_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = {"populate_by_name": True}
