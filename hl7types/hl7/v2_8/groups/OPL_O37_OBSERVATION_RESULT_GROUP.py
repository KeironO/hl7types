"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OPL_O37.OBSERVATION_RESULT_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PRT import PRT

_OBX = OBX
_PRT = PRT


class OPL_O37_OBSERVATION_RESULT_GROUP(HL7Model):
    """HL7 v2 OPL_O37.OBSERVATION_RESULT_GROUP group.

    Attributes:
        OBX (OBX): Observation/Result, required
        PRT (Optional[List[PRT]]): Participation Information, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = ConfigDict(populate_by_name=True)
