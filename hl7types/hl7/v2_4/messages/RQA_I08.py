"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQA_I08
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
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1

from ..groups.RQA_I08_AUTHORIZATION import RQA_I08_AUTHORIZATION
from ..groups.RQA_I08_GUARANTOR_INSURANCE import RQA_I08_GUARANTOR_INSURANCE
from ..groups.RQA_I08_OBSERVATION import RQA_I08_OBSERVATION
from ..groups.RQA_I08_PROCEDURE import RQA_I08_PROCEDURE
from ..groups.RQA_I08_PROVIDER import RQA_I08_PROVIDER
from ..groups.RQA_I08_VISIT import RQA_I08_VISIT

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


class RQA_I08(HL7Model):
    """RQA/RPA - Request for treatment authorization information (S11).

    Attributes:
        MSH (MSH): Message Header, required
        RF1 (Optional[RF1]): Referral Information, optional
        AUTHORIZATION (Optional[RQA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RQA_I08_PROVIDER]): required
        PID (PID): Patient identification, required
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        GUARANTOR_INSURANCE (Optional[RQA_I08_GUARANTOR_INSURANCE]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        PROCEDURE (Optional[List[RQA_I08_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RQA_I08_OBSERVATION]]): optional
        VISIT (Optional[RQA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Information",
    )

    AUTHORIZATION: Optional[_RQA_I08_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
    )

    PROVIDER: List[_RQA_I08_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin / associated parties",
    )

    GUARANTOR_INSURANCE: Optional[_RQA_I08_GUARANTOR_INSURANCE] = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[List[_DRG]] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient allergy information",
    )

    PROCEDURE: Optional[List[_RQA_I08_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    OBSERVATION: Optional[List[_RQA_I08_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    VISIT: Optional[_RQA_I08_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
