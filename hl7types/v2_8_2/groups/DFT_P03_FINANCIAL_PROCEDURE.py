"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P03.FINANCIAL_PROCEDURE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PR1 import PR1
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_PR1 = PR1
_PRT = PRT
_ROL = ROL


class DFT_P03_FINANCIAL_PROCEDURE(BaseModel):
    """HL7 v2 DFT_P03.FINANCIAL_PROCEDURE group.

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
