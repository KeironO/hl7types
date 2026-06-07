"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORG_O20.OBSERVATION_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ROL import ROL

_OBR = OBR
_ROL = ROL


class ORG_O20_OBSERVATION_GROUP(HL7Model):
    """HL7 v2 ORG_O20.OBSERVATION_GROUP group.

    Attributes:
        OBR (OBR): required
        ROL (Optional[List[ROL]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
