"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CSU_C09.STUDY_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (Optional[ORC]): Common order segment, optional
        OBR (OBR): Observation request segment, required
        OBX (List[OBX]): Observation segment, required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common order segment",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation request segment",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="Observation segment",
    )

    model_config = ConfigDict(populate_by_name=True)
