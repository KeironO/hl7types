"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORL_O22.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .ORL_O22_ORDER import ORL_O22_ORDER

_ORL_O22_ORDER = ORL_O22_ORDER
_PID = PID


class ORL_O22_PATIENT(HL7Model):
    """HL7 v2 ORL_O22.PATIENT group.

    Attributes:
        PID (PID): required
        ORDER (Optional[List[ORL_O22_ORDER]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    ORDER: Optional[List[_ORL_O22_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
