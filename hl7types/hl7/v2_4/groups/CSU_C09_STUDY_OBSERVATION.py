"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CSU_C09.STUDY_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC

_OBR = OBR
_OBX = OBX
_ORC = ORC


class CSU_C09_STUDY_OBSERVATION(HL7Model):
    """HL7 v2 CSU_C09.STUDY_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        OBX (List[OBX]): Observation/Result, required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
