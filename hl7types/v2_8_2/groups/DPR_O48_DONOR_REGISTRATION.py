"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DPR_O48.DONOR_REGISTRATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PV1 import PV1

_NTE = NTE
_PV1 = PV1


class DPR_O48_DONOR_REGISTRATION(BaseModel):
    """HL7 v2 DPR_O48.DONOR_REGISTRATION group.

    Attributes:
        PV1 (Optional[PV1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
