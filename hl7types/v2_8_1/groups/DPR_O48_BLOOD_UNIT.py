"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DPR_O48.BLOOD_UNIT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    BUI: Optional[List[_BUI]] = Field(
        default=None,
        title="BUI",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
