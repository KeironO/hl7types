"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DPR_O48.BLOOD_UNIT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BUI import BUI
from ..segments.NTE import NTE

_BUI = BUI
_NTE = NTE


class DPR_O48_BLOOD_UNIT(BaseModel):
    """HL7 v2 DPR_O48.BLOOD_UNIT group.

    Attributes:
        BUI (Optional[List[BUI]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    BUI: list[_BUI] | None = Field(
        default=None,
        title="BUI",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
