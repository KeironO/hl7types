"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P03.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR

_NTE = NTE
_OBR = OBR


class DFT_P03_ORDER(BaseModel):
    """HL7 v2 DFT_P03.ORDER group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
