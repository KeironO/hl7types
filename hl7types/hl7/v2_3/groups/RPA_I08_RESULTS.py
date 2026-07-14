"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPA_I08.RESULTS
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


class RPA_I08_RESULTS(HL7Model):
    """HL7 v2 RPA_I08.RESULTS group.

    Attributes:
        OBX (OBX): Observation segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = {"populate_by_name": True}
