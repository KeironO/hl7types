"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORL_O22.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .ORL_O22_ORDER import ORL_O22_ORDER

_ORL_O22_ORDER = ORL_O22_ORDER
_PID = PID


class ORL_O22_PATIENT(HL7Model):
    """HL7 v2 ORL_O22.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        ORDER (Optional[List[ORL_O22_ORDER]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ORDER: Optional[List[_ORL_O22_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
