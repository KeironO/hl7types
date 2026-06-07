"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .ORL_O22_GENERAL_ORDER import ORL_O22_GENERAL_ORDER

_ORL_O22_GENERAL_ORDER = ORL_O22_GENERAL_ORDER
_PID = PID


class ORL_O22_PATIENT(HL7Model):
    """HL7 v2 ORL_O22.PATIENT group.

    Attributes:
        PID (PID): required
        GENERAL_ORDER (List[ORL_O22_GENERAL_ORDER]): required
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    GENERAL_ORDER: List[_ORL_O22_GENERAL_ORDER] = Field(
        min_length=1,
        title="GENERAL_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
