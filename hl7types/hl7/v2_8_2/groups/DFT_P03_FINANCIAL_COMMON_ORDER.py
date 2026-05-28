"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P03.FINANCIAL_COMMON_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .DFT_P03_FINANCIAL_OBSERVATION import DFT_P03_FINANCIAL_OBSERVATION
from .DFT_P03_FINANCIAL_ORDER import DFT_P03_FINANCIAL_ORDER
from .DFT_P03_FINANCIAL_TIMING_QUANTITY import DFT_P03_FINANCIAL_TIMING_QUANTITY

_DFT_P03_FINANCIAL_OBSERVATION = DFT_P03_FINANCIAL_OBSERVATION
_DFT_P03_FINANCIAL_ORDER = DFT_P03_FINANCIAL_ORDER
_DFT_P03_FINANCIAL_TIMING_QUANTITY = DFT_P03_FINANCIAL_TIMING_QUANTITY
_ORC = ORC


class DFT_P03_FINANCIAL_COMMON_ORDER(BaseModel):
    """HL7 v2 DFT_P03.FINANCIAL_COMMON_ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        FINANCIAL_TIMING_QUANTITY (Optional[List[DFT_P03_FINANCIAL_TIMING_QUANTITY]]): optional
        FINANCIAL_ORDER (Optional[DFT_P03_FINANCIAL_ORDER]): optional
        FINANCIAL_OBSERVATION (Optional[List[DFT_P03_FINANCIAL_OBSERVATION]]): optional
    """

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    FINANCIAL_TIMING_QUANTITY: list[_DFT_P03_FINANCIAL_TIMING_QUANTITY] | None = Field(
        default=None,
        title="FINANCIAL_TIMING_QUANTITY",
        description="Optional, repeating",
    )

    FINANCIAL_ORDER: _DFT_P03_FINANCIAL_ORDER | None = Field(
        default=None,
        title="FINANCIAL_ORDER",
        description="Optional",
    )

    FINANCIAL_OBSERVATION: list[_DFT_P03_FINANCIAL_OBSERVATION] | None = Field(
        default=None,
        title="FINANCIAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
