"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RCI_I05.OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from .RCI_I05_RESULTS import RCI_I05_RESULTS

_NTE = NTE
_OBR = OBR
_RCI_I05_RESULTS = RCI_I05_RESULTS


class RCI_I05_OBSERVATION(BaseModel):
    """HL7 v2 RCI_I05.OBSERVATION group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        RESULTS (Optional[List[RCI_I05_RESULTS]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESULTS: list[_RCI_I05_RESULTS] | None = Field(
        default=None,
        title="RESULTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
