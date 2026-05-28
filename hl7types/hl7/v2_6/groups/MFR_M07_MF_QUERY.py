"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFR_M07.MF_QUERY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CM0 import CM0
from ..segments.CM2 import CM2
from ..segments.MFE import MFE

_CM0 = CM0
_CM2 = CM2
_MFE = MFE


class MFR_M07_MF_QUERY(BaseModel):
    """HL7 v2 MFR_M07.MF_QUERY group.

    Attributes:
        MFE (MFE): required
        CM0 (CM0): required
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

    CM2: list[_CM2] | None = Field(
        default=None,
        title="CM2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
