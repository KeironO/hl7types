"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: REF_I12.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .REF_I12_RESULTS_NOTES import REF_I12_RESULTS_NOTES

_NTE = NTE
_OBR = OBR
_REF_I12_RESULTS_NOTES = REF_I12_RESULTS_NOTES


class REF_I12_OBSERVATION(HL7Model):
    """HL7 v2 REF_I12.OBSERVATION group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        RESULTS_NOTES (Optional[List[REF_I12_RESULTS_NOTES]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESULTS_NOTES: Optional[List[_REF_I12_RESULTS_NOTES]] = Field(
        default=None,
        title="RESULTS_NOTES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
