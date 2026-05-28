"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRI_I12.RESULTS_NOTES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class RRI_I12_RESULTS_NOTES(BaseModel):
    """HL7 v2 RRI_I12.RESULTS_NOTES group.

    Attributes:
        OBX (OBX): required
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
