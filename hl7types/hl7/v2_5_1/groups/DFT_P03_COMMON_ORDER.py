"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DFT_P03.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .DFT_P03_OBSERVATION import DFT_P03_OBSERVATION
from .DFT_P03_ORDER import DFT_P03_ORDER
from .DFT_P03_TIMING_QUANTITY import DFT_P03_TIMING_QUANTITY

_DFT_P03_OBSERVATION = DFT_P03_OBSERVATION
_DFT_P03_ORDER = DFT_P03_ORDER
_DFT_P03_TIMING_QUANTITY = DFT_P03_TIMING_QUANTITY
_ORC = ORC


class DFT_P03_COMMON_ORDER(BaseModel):
    """HL7 v2 DFT_P03.COMMON_ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        TIMING_QUANTITY (Optional[List[DFT_P03_TIMING_QUANTITY]]): optional
        ORDER (Optional[DFT_P03_ORDER]): optional
        OBSERVATION (Optional[List[DFT_P03_OBSERVATION]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    TIMING_QUANTITY: Optional[List[_DFT_P03_TIMING_QUANTITY]] = Field(
        default=None,
        title="TIMING_QUANTITY",
        description="Optional, repeating",
    )

    ORDER: Optional[_DFT_P03_ORDER] = Field(
        default=None,
        title="ORDER",
        description="Optional",
    )

    OBSERVATION: Optional[List[_DFT_P03_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
