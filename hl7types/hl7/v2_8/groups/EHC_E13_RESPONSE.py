"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E13.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.TXA import TXA

_NTE = NTE
_OBX = OBX
_TXA = TXA


class EHC_E13_RESPONSE(BaseModel):
    """HL7 v2 EHC_E13.RESPONSE group.

    Attributes:
        OBX (OBX): required
        NTE (Optional[NTE]): optional
        TXA (Optional[TXA]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    NTE: _NTE | None = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    TXA: _TXA | None = Field(
        default=None,
        title="TXA",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
