"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPA_I08.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_NTE = NTE
_PV1 = PV1
_PV2 = PV2


class RPA_I08_VISIT(BaseModel):
    """HL7 v2 RPA_I08.VISIT group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        NTE (Optional[List[NTE]]): optional
    """

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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
