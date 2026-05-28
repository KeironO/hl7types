"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: REF_I12.RESULTS_NOTES
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT

_NTE = NTE
_OBX = OBX
_PRT = PRT


class REF_I12_RESULTS_NOTES(BaseModel):
    """HL7 v2 REF_I12.RESULTS_NOTES group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
