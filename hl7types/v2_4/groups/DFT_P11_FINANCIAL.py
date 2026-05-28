"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DFT_P11.FINANCIAL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.FT1 import FT1
from ..segments.GT1 import GT1

from .DFT_P11_FINANCIAL_COMMON_ORDER import DFT_P11_FINANCIAL_COMMON_ORDER
from .DFT_P11_FINANCIAL_INSURANCE import DFT_P11_FINANCIAL_INSURANCE
from .DFT_P11_FINANCIAL_PROCEDURE import DFT_P11_FINANCIAL_PROCEDURE

_DFT_P11_FINANCIAL_COMMON_ORDER = DFT_P11_FINANCIAL_COMMON_ORDER
_DFT_P11_FINANCIAL_INSURANCE = DFT_P11_FINANCIAL_INSURANCE
_DFT_P11_FINANCIAL_PROCEDURE = DFT_P11_FINANCIAL_PROCEDURE
_DG1 = DG1
_DRG = DRG
_FT1 = FT1
_GT1 = GT1


class DFT_P11_FINANCIAL(BaseModel):
    """HL7 v2 DFT_P11.FINANCIAL group.

    Attributes:
        FT1 (FT1): required
        FINANCIAL_PROCEDURE (Optional[List[DFT_P11_FINANCIAL_PROCEDURE]]): optional
        FINANCIAL_COMMON_ORDER (Optional[List[DFT_P11_FINANCIAL_COMMON_ORDER]]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[DRG]): optional
        GT1 (Optional[List[GT1]]): optional
        FINANCIAL_INSURANCE (Optional[List[DFT_P11_FINANCIAL_INSURANCE]]): optional
    """

    FT1: _FT1 = Field(
        default=...,
        title="FT1",
        description="Required",
    )

    FINANCIAL_PROCEDURE: Optional[List[_DFT_P11_FINANCIAL_PROCEDURE]] = Field(
        default=None,
        title="FINANCIAL_PROCEDURE",
        description="Optional, repeating",
    )

    FINANCIAL_COMMON_ORDER: Optional[List[_DFT_P11_FINANCIAL_COMMON_ORDER]] = Field(
        default=None,
        title="FINANCIAL_COMMON_ORDER",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Optional",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    FINANCIAL_INSURANCE: Optional[List[_DFT_P11_FINANCIAL_INSURANCE]] = Field(
        default=None,
        title="FINANCIAL_INSURANCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
