"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RRI_I12
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RRI_I12_AUTHORIZATION_CONTACT2 import RRI_I12_AUTHORIZATION_CONTACT2
from ..groups.RRI_I12_OBSERVATION import RRI_I12_OBSERVATION
from ..groups.RRI_I12_PATIENT_VISIT import RRI_I12_PATIENT_VISIT
from ..groups.RRI_I12_PROCEDURE import RRI_I12_PROCEDURE
from ..groups.RRI_I12_PROVIDER_CONTACT import RRI_I12_PROVIDER_CONTACT
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
from ..segments.UAC import UAC

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RF1 = RF1
_RRI_I12_AUTHORIZATION_CONTACT2 = RRI_I12_AUTHORIZATION_CONTACT2
_RRI_I12_OBSERVATION = RRI_I12_OBSERVATION
_RRI_I12_PATIENT_VISIT = RRI_I12_PATIENT_VISIT
_RRI_I12_PROCEDURE = RRI_I12_PROCEDURE
_RRI_I12_PROVIDER_CONTACT = RRI_I12_PROVIDER_CONTACT
_SFT = SFT
_UAC = UAC


class RRI_I12(BaseModel):
    """HL7 v2 RRI_I12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (Optional[MSA]): optional
        RF1 (Optional[RF1]): optional
        AUTHORIZATION_CONTACT2 (Optional[RRI_I12_AUTHORIZATION_CONTACT2]): optional
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

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
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

    AUTHORIZATION_CONTACT2: _RRI_I12_AUTHORIZATION_CONTACT2 | None = Field(
        default=None,
        title="AUTHORIZATION_CONTACT2",
        description="Optional",
    )

    PROVIDER_CONTACT: list[_RRI_I12_PROVIDER_CONTACT] = Field(
        default=...,
        title="PROVIDER_CONTACT",
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

    OBSERVATION: list[_RRI_I12_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PATIENT_VISIT: _RRI_I12_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
