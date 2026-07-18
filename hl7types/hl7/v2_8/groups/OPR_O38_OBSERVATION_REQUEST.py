"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OPR_O38.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

_OBR = OBR
_ORC = ORC
_PRT = PRT


class OPR_O38_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 OPR_O38.OBSERVATION_REQUEST group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        OBR (OBR): Observation Request, required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    model_config = ConfigDict(populate_by_name=True)
