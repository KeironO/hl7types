"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P11.VISIT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.PV2 import PV2
from ..segments.ROL import ROL

_PRT = PRT
_PV2 = PV2
_ROL = ROL


class DFT_P11_VISIT(BaseModel):
    """HL7 v2 DFT_P11.VISIT group.

    Attributes:
        PV2 (PV2): required
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PV2: _PV2 = Field(
        default=...,
        title="PV2",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
