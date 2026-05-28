"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z86.OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class RSP_Z86_OBSERVATION(BaseModel):
    """HL7 v2 RSP_Z86.OBSERVATION group.

    Attributes:
        OBX (Optional[OBX]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX | None = Field(
        default=None,
        title="OBX",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
