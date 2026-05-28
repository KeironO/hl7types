"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E01.PROCEDURE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PR1 import PR1
from ..segments.ROL import ROL

_NTE = NTE
_PR1 = PR1
_ROL = ROL


class EHC_E01_PROCEDURE(BaseModel):
    """HL7 v2 EHC_E01.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        NTE (Optional[List[NTE]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
