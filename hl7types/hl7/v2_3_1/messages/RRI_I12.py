"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRI_I12
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
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1

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


class RRI_I12(HL7Model):
    """REF/RRI -  Patient referral.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (Optional[MSA]): MSA - message acknowledgment segment, optional
        RF1 (Optional[RF1]): Referral Infomation, optional
        AUTHORIZATION_CONTACT (Optional[RRI_I12_AUTHORIZATION_CONTACT]): optional
        PROVIDER_CONTACT (List[RRI_I12_PROVIDER_CONTACT]): required
        PID (PID): PID - patient identification segment, required
        ACC (Optional[ACC]): ACC - accident segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[List[DRG]]): DRG - diagnosis related group segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        PROCEDURE (Optional[List[RRI_I12_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RRI_I12_OBSERVATION]]): optional
        PATIENT_VISIT (Optional[RRI_I12_PATIENT_VISIT]): optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: Optional[_MSA] = Field(
        default=None,
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Infomation",
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
        description="PID - patient identification segment",
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
        description="NTE - notes and comments segment",
    )

    model_config = {"populate_by_name": True}
