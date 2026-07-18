"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
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
from ..segments.PRT import PRT

from .CSU_C09_TIMING_QTY import CSU_C09_TIMING_QTY

_CSU_C09_TIMING_QTY = CSU_C09_TIMING_QTY
_OBR = OBR
_OBX = OBX
_ORC = ORC
_PRT = PRT


class CSU_C09_STUDY_OBSERVATION(HL7Model):
    """HL7 v2 CSU_C09.STUDY_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING_QTY (Optional[List[CSU_C09_TIMING_QTY]]): optional
        OBX (OBX): Observation/Result, required
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING_QTY: Optional[List[_CSU_C09_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)
