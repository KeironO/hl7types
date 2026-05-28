"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DFT_P03.FINANCIAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.ROL import ROL

from .DFT_P03_FINANCIAL_COMMON_ORDER import DFT_P03_FINANCIAL_COMMON_ORDER
from .DFT_P03_FINANCIAL_PROCEDURE import DFT_P03_FINANCIAL_PROCEDURE

_DFT_P03_FINANCIAL_COMMON_ORDER = DFT_P03_FINANCIAL_COMMON_ORDER
_DFT_P03_FINANCIAL_PROCEDURE = DFT_P03_FINANCIAL_PROCEDURE
_FT1 = FT1
_NTE = NTE
_PRT = PRT
_ROL = ROL


class DFT_P03_FINANCIAL(BaseModel):
    """HL7 v2 DFT_P03.FINANCIAL group.

    Attributes:
        FT1 (FT1): required
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
        NTE (Optional[NTE]): optional
        FINANCIAL_PROCEDURE (Optional[List[DFT_P03_FINANCIAL_PROCEDURE]]): optional
        FINANCIAL_COMMON_ORDER (Optional[List[DFT_P03_FINANCIAL_COMMON_ORDER]]): optional
    """

    FT1: _FT1 = Field(
        default=...,
        title="FT1",
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

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    FINANCIAL_PROCEDURE: Optional[List[_DFT_P03_FINANCIAL_PROCEDURE]] = Field(
        default=None,
        title="FINANCIAL_PROCEDURE",
        description="Optional, repeating",
    )

    FINANCIAL_COMMON_ORDER: Optional[List[_DFT_P03_FINANCIAL_COMMON_ORDER]] = Field(
        default=None,
        title="FINANCIAL_COMMON_ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
