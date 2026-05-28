"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFR_M06.MF_QUERY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CM0 import CM0
from ..segments.CM1 import CM1
from ..segments.CM2 import CM2
from ..segments.MFE import MFE

_CM0 = CM0
_CM1 = CM1
_CM2 = CM2
_MFE = MFE


class MFR_M06_MF_QUERY(BaseModel):
    """HL7 v2 MFR_M06.MF_QUERY group.

    Attributes:
        MFE (MFE): required
        CM0 (CM0): required
        CM1 (Optional[List[CM1]]): optional
        CM2 (Optional[List[CM2]]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    CM0: _CM0 = Field(
        default=...,
        title="CM0",
        description="Required",
    )

    CM1: Optional[List[_CM1]] = Field(
        default=None,
        title="CM1",
        description="Optional, repeating",
    )

    CM2: Optional[List[_CM2]] = Field(
        default=None,
        title="CM2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
