"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RRI_I12
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
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1
from ..segments.SFT import SFT

from ..groups.RRI_I12_AUTHORIZATION_CONTACT import RRI_I12_AUTHORIZATION_CONTACT
from ..groups.RRI_I12_OBSERVATION import RRI_I12_OBSERVATION
from ..groups.RRI_I12_PATIENT_VISIT import RRI_I12_PATIENT_VISIT
from ..groups.RRI_I12_PROCEDURE import RRI_I12_PROCEDURE
from ..groups.RRI_I12_PROVIDER_CONTACT import RRI_I12_PROVIDER_CONTACT

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RF1 = RF1
_RRI_I12_AUTHORIZATION_CONTACT = RRI_I12_AUTHORIZATION_CONTACT
_RRI_I12_OBSERVATION = RRI_I12_OBSERVATION
_RRI_I12_PATIENT_VISIT = RRI_I12_PATIENT_VISIT
_RRI_I12_PROCEDURE = RRI_I12_PROCEDURE
_RRI_I12_PROVIDER_CONTACT = RRI_I12_PROVIDER_CONTACT
_SFT = SFT


class RRI_I12(HL7Model):
    """REF/RRI - Patient referral (S11.5.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MSA (Optional[MSA]): Message Acknowledgment, optional
        RF1 (Optional[RF1]): Referral Information, optional
        AUTHORIZATION_CONTACT (Optional[RRI_I12_AUTHORIZATION_CONTACT]): optional
        PROVIDER_CONTACT (List[RRI_I12_PROVIDER_CONTACT]): required
        PID (PID): Patient Identification, required
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PROCEDURE (Optional[List[RRI_I12_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RRI_I12_OBSERVATION]]): optional
        PATIENT_VISIT (Optional[RRI_I12_PATIENT_VISIT]): optional
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

    MSA: Optional[_MSA] = Field(
        default=None,
        title="MSA",
        description="Message Acknowledgment",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Information",
    )

    AUTHORIZATION_CONTACT: Optional[_RRI_I12_AUTHORIZATION_CONTACT] = Field(
        default=None,
        title="AUTHORIZATION_CONTACT",
    )

    PROVIDER_CONTACT: List[_RRI_I12_PROVIDER_CONTACT] = Field(
        min_length=1,
        title="PROVIDER_CONTACT",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
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

    PROCEDURE: Optional[List[_RRI_I12_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    OBSERVATION: Optional[List[_RRI_I12_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    PATIENT_VISIT: Optional[_RRI_I12_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
