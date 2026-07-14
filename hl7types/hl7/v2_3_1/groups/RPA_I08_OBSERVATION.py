"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        OBR (OBR): OBR - observation request segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        RESULTS (Optional[List[RPA_I08_RESULTS]]): optional
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

    RESULTS: Optional[List[_RPA_I08_RESULTS]] = Field(
        default=None,
        title="RESULTS",
    )

    model_config = {"populate_by_name": True}
