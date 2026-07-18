"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORP_O10.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID

_NTE = NTE
_PID = PID


class ORP_O10_PATIENT(HL7Model):
    """HL7 v2 ORP_O10.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
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

    model_config = ConfigDict(populate_by_name=True)
