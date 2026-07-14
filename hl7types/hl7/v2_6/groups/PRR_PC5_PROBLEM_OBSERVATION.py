"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PRR_PC5.PROBLEM_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class PRR_PC5_PROBLEM_OBSERVATION(HL7Model):
    """HL7 v2 PRR_PC5.PROBLEM_OBSERVATION group.

    Attributes:
        OBX (OBX): Observation/Result, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
