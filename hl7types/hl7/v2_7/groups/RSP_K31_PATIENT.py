"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_K31.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PID import PID

from .RSP_K31_ADDITIONAL_DEMOGRAPHICS import RSP_K31_ADDITIONAL_DEMOGRAPHICS
from .RSP_K31_PATIENT_VISIT import RSP_K31_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PID = PID
_RSP_K31_ADDITIONAL_DEMOGRAPHICS = RSP_K31_ADDITIONAL_DEMOGRAPHICS
_RSP_K31_PATIENT_VISIT = RSP_K31_PATIENT_VISIT


class RSP_K31_PATIENT(HL7Model):
    """HL7 v2 RSP_K31.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        ADDITIONAL_DEMOGRAPHICS (Optional[RSP_K31_ADDITIONAL_DEMOGRAPHICS]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PATIENT_VISIT (Optional[RSP_K31_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ADDITIONAL_DEMOGRAPHICS: Optional[_RSP_K31_ADDITIONAL_DEMOGRAPHICS] = Field(
        default=None,
        title="ADDITIONAL_DEMOGRAPHICS",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    PATIENT_VISIT: Optional[_RSP_K31_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
