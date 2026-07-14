"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRI_I12.RESULTS_NOTES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT

_NTE = NTE
_OBX = OBX
_PRT = PRT


class RRI_I12_RESULTS_NOTES(HL7Model):
    """HL7 v2 RRI_I12.RESULTS_NOTES group.

    Attributes:
        OBX (OBX): Observation/Result, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
