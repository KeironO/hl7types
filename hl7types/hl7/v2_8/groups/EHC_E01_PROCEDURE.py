"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E01.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PR1 import PR1
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_NTE = NTE
_PR1 = PR1
_PRT = PRT
_ROL = ROL


class EHC_E01_PROCEDURE(HL7Model):
    """HL7 v2 EHC_E01.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
