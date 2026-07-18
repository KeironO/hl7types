"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RCI_I05.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        OBR (OBR): OBR - observation request segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        RESULTS (Optional[List[RCI_I05_RESULTS]]): optional
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

    RESULTS: Optional[List[_RCI_I05_RESULTS]] = Field(
        default=None,
        title="RESULTS",
    )

    model_config = ConfigDict(populate_by_name=True)
