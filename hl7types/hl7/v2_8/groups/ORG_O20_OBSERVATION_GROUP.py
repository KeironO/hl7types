"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORG_O20.OBSERVATION_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.PRT import PRT

_OBR = OBR
_PRT = PRT


class ORG_O20_OBSERVATION_GROUP(HL7Model):
    """HL7 v2 ORG_O20.OBSERVATION_GROUP group.

    Attributes:
        OBR (OBR): Observation Request, required
        PRT (Optional[List[PRT]]): Participation Information, optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = ConfigDict(populate_by_name=True)
