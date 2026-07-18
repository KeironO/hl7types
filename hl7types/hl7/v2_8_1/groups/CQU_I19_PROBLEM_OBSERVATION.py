"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CQU_I19.PROBLEM_OBSERVATION
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


class CQU_I19_PROBLEM_OBSERVATION(HL7Model):
    """HL7 v2 CQU_I19.PROBLEM_OBSERVATION group.

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
