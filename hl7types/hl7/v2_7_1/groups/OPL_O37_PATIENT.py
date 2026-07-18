"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OPL_O37.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .OPL_O37_INSURANCE import OPL_O37_INSURANCE
from .OPL_O37_OBSERVATIONS_ON_PATIENT import OPL_O37_OBSERVATIONS_ON_PATIENT

_AL1 = AL1
_OPL_O37_INSURANCE = OPL_O37_INSURANCE
_OPL_O37_OBSERVATIONS_ON_PATIENT = OPL_O37_OBSERVATIONS_ON_PATIENT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OPL_O37_PATIENT(HL7Model):
    """HL7 v2 OPL_O37.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        OBSERVATIONS_ON_PATIENT (Optional[List[OPL_O37_OBSERVATIONS_ON_PATIENT]]): optional
        INSURANCE (Optional[List[OPL_O37_INSURANCE]]): optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    OBSERVATIONS_ON_PATIENT: Optional[List[_OPL_O37_OBSERVATIONS_ON_PATIENT]] = Field(
        default=None,
        title="OBSERVATIONS_ON_PATIENT",
    )

    INSURANCE: Optional[List[_OPL_O37_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    model_config = ConfigDict(populate_by_name=True)
