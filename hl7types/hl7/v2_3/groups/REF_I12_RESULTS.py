"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: REF_I12.RESULTS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        OBR (OBR): Observation request segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        OBSERVATION (Optional[List[REF_I12_OBSERVATION]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation request segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    OBSERVATION: Optional[List[_REF_I12_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
