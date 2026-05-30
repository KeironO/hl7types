"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: REF_I12.RESULTS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .REF_I12_OBSERVATION import REF_I12_OBSERVATION

_NTE = NTE
_OBR = OBR
_REF_I12_OBSERVATION = REF_I12_OBSERVATION


class REF_I12_RESULTS(HL7Model):
    """HL7 v2 REF_I12.RESULTS group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[REF_I12_OBSERVATION]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_REF_I12_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
