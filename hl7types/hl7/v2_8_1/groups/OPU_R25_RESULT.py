"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPU_R25.RESULT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT

_NTE = NTE
_OBX = OBX
_PRT = PRT


class OPU_R25_RESULT(BaseModel):
    """HL7 v2 OPU_R25.RESULT group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
