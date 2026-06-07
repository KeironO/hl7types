"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O36.OBSERVATION_REQUEST
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


class ORL_O36_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 ORL_O36.OBSERVATION_REQUEST group.

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
