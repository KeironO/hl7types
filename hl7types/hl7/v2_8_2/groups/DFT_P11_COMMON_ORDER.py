"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P11.COMMON_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .DFT_P11_OBSERVATION import DFT_P11_OBSERVATION
from .DFT_P11_ORDER import DFT_P11_ORDER
from .DFT_P11_TIMING_QUANTITY import DFT_P11_TIMING_QUANTITY

_DFT_P11_OBSERVATION = DFT_P11_OBSERVATION
_DFT_P11_ORDER = DFT_P11_ORDER
_DFT_P11_TIMING_QUANTITY = DFT_P11_TIMING_QUANTITY
_ORC = ORC


class DFT_P11_COMMON_ORDER(BaseModel):
    """HL7 v2 DFT_P11.COMMON_ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        TIMING_QUANTITY (Optional[List[DFT_P11_TIMING_QUANTITY]]): optional
        ORDER (Optional[DFT_P11_ORDER]): optional
        OBSERVATION (Optional[List[DFT_P11_OBSERVATION]]): optional
    """

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    TIMING_QUANTITY: list[_DFT_P11_TIMING_QUANTITY] | None = Field(
        default=None,
        title="TIMING_QUANTITY",
        description="Optional, repeating",
    )

    ORDER: _DFT_P11_ORDER | None = Field(
        default=None,
        title="ORDER",
        description="Optional",
    )

    OBSERVATION: list[_DFT_P11_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
