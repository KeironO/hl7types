"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RPA_I08.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .RPA_I08_RESULTS import RPA_I08_RESULTS

_NTE = NTE
_OBR = OBR
_RPA_I08_RESULTS = RPA_I08_RESULTS


class RPA_I08_OBSERVATION(HL7Model):
    """HL7 v2 RPA_I08.OBSERVATION group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        RESULTS (Optional[List[RPA_I08_RESULTS]]): optional
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

    RESULTS: Optional[List[_RPA_I08_RESULTS]] = Field(
        default=None,
        title="RESULTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
