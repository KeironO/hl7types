"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RRI_I12.OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from .RRI_I12_RESULTS_NOTES import RRI_I12_RESULTS_NOTES

_NTE = NTE
_OBR = OBR
_RRI_I12_RESULTS_NOTES = RRI_I12_RESULTS_NOTES


class RRI_I12_OBSERVATION(BaseModel):
    """HL7 v2 RRI_I12.OBSERVATION group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        RESULTS_NOTES (Optional[List[RRI_I12_RESULTS_NOTES]]): optional
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

    RESULTS_NOTES: list[_RRI_I12_RESULTS_NOTES] | None = Field(
        default=None,
        title="RESULTS_NOTES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
