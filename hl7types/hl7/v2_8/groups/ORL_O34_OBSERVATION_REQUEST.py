"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORL_O34.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.PRT import PRT

_OBR = OBR
_PRT = PRT


class ORL_O34_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 ORL_O34.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
