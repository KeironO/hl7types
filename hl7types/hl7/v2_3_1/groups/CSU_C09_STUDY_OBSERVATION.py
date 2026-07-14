"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        ORC (Optional[ORC]): ORC - common order segment, optional
        OBR (OBR): OBR - observation request segment, required
        OBX (List[OBX]): OBX - observation/result segment, required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="ORC - common order segment",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="OBR - observation request segment",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="OBX - observation/result segment",
    )

    model_config = {"populate_by_name": True}
