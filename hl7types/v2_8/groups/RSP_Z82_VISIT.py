"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_Z82.VISIT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_AL1 = AL1
_PV1 = PV1
_PV2 = PV2


class RSP_Z82_VISIT(BaseModel):
    """HL7 v2 RSP_Z82.VISIT group.

    Attributes:
        AL1 (List[AL1]): required
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
    """

    AL1: List[_AL1] = Field(
        default=...,
        title="AL1",
        description="Required, repeating",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
