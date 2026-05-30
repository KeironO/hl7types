"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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

from .CSU_C09_TIMING_QTY import CSU_C09_TIMING_QTY

_CSU_C09_TIMING_QTY = CSU_C09_TIMING_QTY
_OBR = OBR
_OBX = OBX
_ORC = ORC


class CSU_C09_STUDY_OBSERVATION(HL7Model):
    """HL7 v2 CSU_C09.STUDY_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        TIMING_QTY (Optional[List[CSU_C09_TIMING_QTY]]): optional
        OBX (List[OBX]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    TIMING_QTY: Optional[List[_CSU_C09_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    OBX: List[_OBX] = Field(
        default=...,
        title="OBX",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
