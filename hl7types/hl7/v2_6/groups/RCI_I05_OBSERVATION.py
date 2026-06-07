"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RCI_I05.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .RCI_I05_RESULTS import RCI_I05_RESULTS

_NTE = NTE
_OBR = OBR
_RCI_I05_RESULTS = RCI_I05_RESULTS


class RCI_I05_OBSERVATION(HL7Model):
    """HL7 v2 RCI_I05.OBSERVATION group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        RESULTS (Optional[List[RCI_I05_RESULTS]]): optional
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

    RESULTS: Optional[List[_RCI_I05_RESULTS]] = Field(
        default=None,
        title="RESULTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
