"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRI_I12.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .RRI_I12_RESULTS_NOTES import RRI_I12_RESULTS_NOTES

_NTE = NTE
_OBR = OBR
_RRI_I12_RESULTS_NOTES = RRI_I12_RESULTS_NOTES


class RRI_I12_OBSERVATION(HL7Model):
    """HL7 v2 RRI_I12.OBSERVATION group.

    Attributes:
        OBR (OBR): OBR - observation request segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        RESULTS_NOTES (Optional[List[RRI_I12_RESULTS_NOTES]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="OBR - observation request segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    RESULTS_NOTES: Optional[List[_RRI_I12_RESULTS_NOTES]] = Field(
        default=None,
        title="RESULTS_NOTES",
    )

    model_config = ConfigDict(populate_by_name=True)
