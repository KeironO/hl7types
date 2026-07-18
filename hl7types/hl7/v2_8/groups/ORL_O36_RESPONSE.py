"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORL_O36.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORL_O36_SPECIMEN import ORL_O36_SPECIMEN

_ARV = ARV
_ORL_O36_SPECIMEN = ORL_O36_SPECIMEN
_PID = PID
_PRT = PRT


class ORL_O36_RESPONSE(HL7Model):
    """HL7 v2 ORL_O36.RESPONSE group.

    Attributes:
        PID (PID): Patient Identification, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
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

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    SPECIMEN: List[_ORL_O36_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
    )

    model_config = ConfigDict(populate_by_name=True)
