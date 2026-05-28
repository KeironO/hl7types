"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CSU_C09.STUDY_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .CSU_C09_TIMING_QTY import CSU_C09_TIMING_QTY

_CSU_C09_TIMING_QTY = CSU_C09_TIMING_QTY
_OBR = OBR
_OBX = OBX
_ORC = ORC
_PRT = PRT


class CSU_C09_STUDY_OBSERVATION(BaseModel):
    """HL7 v2 CSU_C09.STUDY_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
        TIMING_QTY (Optional[List[CSU_C09_TIMING_QTY]]): optional
        OBX (OBX): required
    """

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_CSU_C09_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    model_config = {"populate_by_name": True}
