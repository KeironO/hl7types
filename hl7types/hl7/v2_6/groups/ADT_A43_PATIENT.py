"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A43.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.MRG import MRG
from ..segments.PD1 import PD1
from ..segments.PID import PID

_ARV = ARV
_MRG = MRG
_PD1 = PD1
_PID = PID


class ADT_A43_PATIENT(HL7Model):
    """HL7 v2 ADT_A43.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        MRG (MRG): Merge Patient Information, required
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

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    MRG: _MRG = Field(
        title="MRG",
        description="Merge Patient Information",
    )

    model_config = ConfigDict(populate_by_name=True)
