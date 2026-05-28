"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DFT_P03.FINANCIAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.FT1 import FT1
from .DFT_P03_FINANCIAL_COMMON_ORDER import DFT_P03_FINANCIAL_COMMON_ORDER
from .DFT_P03_FINANCIAL_PROCEDURE import DFT_P03_FINANCIAL_PROCEDURE

_DFT_P03_FINANCIAL_COMMON_ORDER = DFT_P03_FINANCIAL_COMMON_ORDER
_DFT_P03_FINANCIAL_PROCEDURE = DFT_P03_FINANCIAL_PROCEDURE
_FT1 = FT1


class DFT_P03_FINANCIAL(BaseModel):
    """HL7 v2 DFT_P03.FINANCIAL group.

    Attributes:
        FT1 (FT1): required
        FINANCIAL_PROCEDURE (Optional[List[DFT_P03_FINANCIAL_PROCEDURE]]): optional
        FINANCIAL_COMMON_ORDER (Optional[List[DFT_P03_FINANCIAL_COMMON_ORDER]]): optional
    """

    FT1: _FT1 = Field(
        default=...,
        title="FT1",
        description="Required",
    )

    FINANCIAL_PROCEDURE: list[_DFT_P03_FINANCIAL_PROCEDURE] | None = Field(
        default=None,
        title="FINANCIAL_PROCEDURE",
        description="Optional, repeating",
    )

    FINANCIAL_COMMON_ORDER: list[_DFT_P03_FINANCIAL_COMMON_ORDER] | None = Field(
        default=None,
        title="FINANCIAL_COMMON_ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
