"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
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
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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
_SFT = SFT
_UAC = UAC


class RPA_I08(HL7Model):
    """RQA/RPA - Request for treatment authorization information (S11.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        RF1 (Optional[RF1]): Referral Information, optional
        AUTHORIZATION (Optional[RPA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RPA_I08_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[RPA_I08_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PROCEDURE (List[RPA_I08_PROCEDURE]): required
        OBSERVATION (Optional[List[RPA_I08_OBSERVATION]]): optional
        VISIT (Optional[RPA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Information",
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
        description="Patient Identification",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_RPA_I08_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
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
        description="Patient Allergy Information",
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
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
