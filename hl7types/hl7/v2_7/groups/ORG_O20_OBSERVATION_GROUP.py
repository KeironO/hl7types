"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORG_O20.OBSERVATION_GROUP
Type: Group
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR

_OBR = OBR


class ORG_O20_OBSERVATION_GROUP(HL7Model):
    """HL7 v2 ORG_O20.OBSERVATION_GROUP group.

    Attributes:
        OBR (OBR): required
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
