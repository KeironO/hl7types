"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CSU_C09.STUDY_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.ROL import ROL
from .CSU_C09_TIMING_QTY import CSU_C09_TIMING_QTY

_CSU_C09_TIMING_QTY = CSU_C09_TIMING_QTY
_OBR = OBR
_OBX = OBX
_ORC = ORC
_ROL = ROL


class CSU_C09_STUDY_OBSERVATION(BaseModel):
    """HL7 v2 CSU_C09.STUDY_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        ROL (Optional[List[ROL]]): optional
        TIMING_QTY (Optional[List[CSU_C09_TIMING_QTY]]): optional
        OBX (List[OBX]): required
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

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_CSU_C09_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    OBX: list[_OBX] = Field(
        default=...,
        title="OBX",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
