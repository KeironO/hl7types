"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORL_O36.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORL_O36_SPECIMEN import ORL_O36_SPECIMEN

_ORL_O36_SPECIMEN = ORL_O36_SPECIMEN
_PID = PID
_PRT = PRT


class ORL_O36_RESPONSE(HL7Model):
    """HL7 v2 ORL_O36.RESPONSE group.

    Attributes:
        PID (PID): Patient Identification, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        SPECIMEN (List[ORL_O36_SPECIMEN]): required
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

    SPECIMEN: List[_ORL_O36_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
    )

    model_config = {"populate_by_name": True}
