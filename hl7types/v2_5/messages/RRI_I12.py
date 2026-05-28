"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RRI_I12
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

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


class RRI_I12(BaseModel):
    """HL7 v2 RRI_I12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (Optional[MSA]): optional
        RF1 (Optional[RF1]): optional
        AUTHORIZATION_CONTACT (Optional[RRI_I12_AUTHORIZATION_CONTACT]): optional
        PROVIDER_CONTACT (List[RRI_I12_PROVIDER_CONTACT]): required
        PID (PID): required
        ACC (Optional[ACC]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        PROCEDURE (Optional[List[RRI_I12_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RRI_I12_OBSERVATION]]): optional
        PATIENT_VISIT (Optional[RRI_I12_PATIENT_VISIT]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    MSA: Optional[_MSA] = Field(
        default=None,
        title="MSA",
        description="Optional",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Optional",
    )

    AUTHORIZATION_CONTACT: Optional[_RRI_I12_AUTHORIZATION_CONTACT] = Field(
        default=None,
        title="AUTHORIZATION_CONTACT",
        description="Optional",
    )

    PROVIDER_CONTACT: List[_RRI_I12_PROVIDER_CONTACT] = Field(
        default=...,
        title="PROVIDER_CONTACT",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
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

    PROCEDURE: Optional[List[_RRI_I12_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_RRI_I12_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_RRI_I12_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
