"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DFT_P03.COMMON_ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .DFT_P03_OBSERVATION import DFT_P03_OBSERVATION
from .DFT_P03_ORDER import DFT_P03_ORDER

_DFT_P03_OBSERVATION = DFT_P03_OBSERVATION
_DFT_P03_ORDER = DFT_P03_ORDER
_ORC = ORC


class DFT_P03_COMMON_ORDER(BaseModel):
    """HL7 v2 DFT_P03.COMMON_ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        ORDER (Optional[DFT_P03_ORDER]): optional
        OBSERVATION (Optional[List[DFT_P03_OBSERVATION]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
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
