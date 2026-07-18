"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: REF_I12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.REF_I12_AUTHORIZATION_CONTACT1 import REF_I12_AUTHORIZATION_CONTACT1
from ..groups.REF_I12_INSURANCE import REF_I12_INSURANCE
from ..groups.REF_I12_OBSERVATION import REF_I12_OBSERVATION
from ..groups.REF_I12_PATIENT_VISIT import REF_I12_PATIENT_VISIT
from ..groups.REF_I12_PROCEDURE import REF_I12_PROCEDURE
from ..groups.REF_I12_PROVIDER_CONTACT import REF_I12_PROVIDER_CONTACT

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_REF_I12_AUTHORIZATION_CONTACT1 = REF_I12_AUTHORIZATION_CONTACT1
_REF_I12_INSURANCE = REF_I12_INSURANCE
_REF_I12_OBSERVATION = REF_I12_OBSERVATION
_REF_I12_PATIENT_VISIT = REF_I12_PATIENT_VISIT
_REF_I12_PROCEDURE = REF_I12_PROCEDURE
_REF_I12_PROVIDER_CONTACT = REF_I12_PROVIDER_CONTACT
_RF1 = RF1
_SFT = SFT
_UAC = UAC


class REF_I12(HL7Model):
    """REF/RRI - Patient referral (S11.5.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        RF1 (Optional[RF1]): Referral Information, optional
        AUTHORIZATION_CONTACT1 (Optional[REF_I12_AUTHORIZATION_CONTACT1]): optional
        PROVIDER_CONTACT (List[REF_I12_PROVIDER_CONTACT]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[REF_I12_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PROCEDURE (Optional[List[REF_I12_PROCEDURE]]): optional
        OBSERVATION (Optional[List[REF_I12_OBSERVATION]]): optional
        PATIENT_VISIT (Optional[REF_I12_PATIENT_VISIT]): optional
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

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Information",
    )

    AUTHORIZATION_CONTACT1: Optional[_REF_I12_AUTHORIZATION_CONTACT1] = Field(
        default=None,
        title="AUTHORIZATION_CONTACT1",
    )

    PROVIDER_CONTACT: List[_REF_I12_PROVIDER_CONTACT] = Field(
        min_length=1,
        title="PROVIDER_CONTACT",
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

    INSURANCE: Optional[List[_REF_I12_INSURANCE]] = Field(
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

    PROCEDURE: Optional[List[_REF_I12_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    OBSERVATION: Optional[List[_REF_I12_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    PATIENT_VISIT: Optional[_REF_I12_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
