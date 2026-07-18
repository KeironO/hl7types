"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORL_O40.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORL_O40_ORDER import ORL_O40_ORDER

_ORL_O40_ORDER = ORL_O40_ORDER
_PID = PID
_PRT = PRT


class ORL_O40_PATIENT(HL7Model):
    """HL7 v2 ORL_O40.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        ORDER (Optional[List[ORL_O40_ORDER]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ORDER: Optional[List[_ORL_O40_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
