"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DFT_P11.FINANCIAL_COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .DFT_P11_FINANCIAL_OBSERVATION import DFT_P11_FINANCIAL_OBSERVATION
from .DFT_P11_FINANCIAL_ORDER import DFT_P11_FINANCIAL_ORDER

_DFT_P11_FINANCIAL_OBSERVATION = DFT_P11_FINANCIAL_OBSERVATION
_DFT_P11_FINANCIAL_ORDER = DFT_P11_FINANCIAL_ORDER
_ORC = ORC


class DFT_P11_FINANCIAL_COMMON_ORDER(HL7Model):
    """HL7 v2 DFT_P11.FINANCIAL_COMMON_ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        FINANCIAL_ORDER (Optional[DFT_P11_FINANCIAL_ORDER]): optional
        FINANCIAL_OBSERVATION (Optional[List[DFT_P11_FINANCIAL_OBSERVATION]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    FINANCIAL_ORDER: Optional[_DFT_P11_FINANCIAL_ORDER] = Field(
        default=None,
        title="FINANCIAL_ORDER",
        description="Optional",
    )

    FINANCIAL_OBSERVATION: Optional[List[_DFT_P11_FINANCIAL_OBSERVATION]] = Field(
        default=None,
        title="FINANCIAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
