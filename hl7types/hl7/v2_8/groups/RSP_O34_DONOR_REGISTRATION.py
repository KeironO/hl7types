"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_O34.DONOR_REGISTRATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PV1 import PV1

_NTE = NTE
_PV1 = PV1


class RSP_O34_DONOR_REGISTRATION(BaseModel):
    """HL7 v2 RSP_O34.DONOR_REGISTRATION group.

    Attributes:
        PV1 (Optional[PV1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
