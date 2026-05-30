"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BAR_P01.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_PR1 = PR1
_PRT = PRT
_ROL = ROL


class BAR_P01_PROCEDURE(HL7Model):
    """HL7 v2 BAR_P01.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
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
