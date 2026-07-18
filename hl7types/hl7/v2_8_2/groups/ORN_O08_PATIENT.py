"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORN_O08.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PID import PID

_ARV = ARV
_NTE = NTE
_PID = PID


class ORN_O08_PATIENT(HL7Model):
    """HL7 v2 ORN_O08.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        ARV (Optional[List[ARV]]): Access Restriction, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
