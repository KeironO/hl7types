"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.CLINICAL_HISTORY_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.IAM import IAM
from ..segments.OBR import OBR
from ..segments.ODS import ODS
from ..segments.PR1 import PR1
from ..segments.RF1 import RF1
from ..segments.RMI import RMI

_ACC = ACC
_AL1 = AL1
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_IAM = IAM
_OBR = OBR
_ODS = ODS
_PR1 = PR1
_RF1 = RF1
_RMI = RMI


class CCR_I16_CLINICAL_HISTORY_OBJECT(HL7Model):
    """HL7 v2 CCR_I16.CLINICAL_HISTORY_OBJECT group.

    Attributes:
        OBR (Optional[OBR]): Observation Request, optional
        ODS (Optional[ODS]): Dietary Orders, Supplements, and Preferences, optional
        PR1 (Optional[PR1]): Procedures, optional
        RF1 (Optional[RF1]): Referral Information, optional
        AL1 (Optional[AL1]): Patient Allergy Information, optional
        IAM (Optional[IAM]): Patient Adverse Reaction Information, optional
        ACC (Optional[ACC]): Accident, optional
        RMI (Optional[RMI]): Risk Management Incident, optional
        DB1 (Optional[DB1]): Disability, optional
        DG1 (Optional[DG1]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Observation Request",
    )

    ODS: Optional[_ODS] = Field(
        default=None,
        title="ODS",
        description="Dietary Orders, Supplements, and Preferences",
    )

    PR1: Optional[_PR1] = Field(
        default=None,
        title="PR1",
        description="Procedures",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Information",
    )

    AL1: Optional[_AL1] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    IAM: Optional[_IAM] = Field(
        default=None,
        title="IAM",
        description="Patient Adverse Reaction Information",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    RMI: Optional[_RMI] = Field(
        default=None,
        title="RMI",
        description="Risk Management Incident",
    )

    DB1: Optional[_DB1] = Field(
        default=None,
        title="DB1",
        description="Disability",
    )

    DG1: Optional[_DG1] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    model_config = {"populate_by_name": True}
