"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DFT_P11.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .DFT_P11_OBSERVATION import DFT_P11_OBSERVATION
from .DFT_P11_ORDER import DFT_P11_ORDER

_DFT_P11_OBSERVATION = DFT_P11_OBSERVATION
_DFT_P11_ORDER = DFT_P11_ORDER
_ORC = ORC


class DFT_P11_COMMON_ORDER(HL7Model):
    """HL7 v2 DFT_P11.COMMON_ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        ORDER (Optional[DFT_P11_ORDER]): optional
        OBSERVATION (Optional[List[DFT_P11_OBSERVATION]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    ORDER: Optional[_DFT_P11_ORDER] = Field(
        default=None,
        title="ORDER",
        description="Optional",
    )

    OBSERVATION: Optional[List[_DFT_P11_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
