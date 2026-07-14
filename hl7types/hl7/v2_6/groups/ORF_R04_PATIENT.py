"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORF_R04.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PID import PID

_NTE = NTE
_OBX = OBX
_PID = PID


class ORF_R04_PATIENT(HL7Model):
    """HL7 v2 ORF_R04.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
