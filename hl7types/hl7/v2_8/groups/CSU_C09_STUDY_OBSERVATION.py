"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CSU_C09.STUDY_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.PRT import PRT

from .CSU_C09_STUDY_OBSERVATION_ORDER import CSU_C09_STUDY_OBSERVATION_ORDER
from .CSU_C09_TIMING_QTY import CSU_C09_TIMING_QTY

_CSU_C09_STUDY_OBSERVATION_ORDER = CSU_C09_STUDY_OBSERVATION_ORDER
_CSU_C09_TIMING_QTY = CSU_C09_TIMING_QTY
_OBR = OBR
_OBX = OBX
_PRT = PRT


class CSU_C09_STUDY_OBSERVATION(BaseModel):
    """HL7 v2 CSU_C09.STUDY_OBSERVATION group.

    Attributes:
        STUDY_OBSERVATION_ORDER (Optional[CSU_C09_STUDY_OBSERVATION_ORDER]): optional
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
        TIMING_QTY (Optional[List[CSU_C09_TIMING_QTY]]): optional
        OBX (OBX): required
    """

    STUDY_OBSERVATION_ORDER: Optional[_CSU_C09_STUDY_OBSERVATION_ORDER] = Field(
        default=None,
        title="STUDY_OBSERVATION_ORDER",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING_QTY: Optional[List[_CSU_C09_TIMING_QTY]] = Field(
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
