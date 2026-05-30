"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z88.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class RSP_Z88_OBSERVATION(HL7Model):
    """HL7 v2 RSP_Z88.OBSERVATION group.

    Attributes:
        OBX (Optional[OBX]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: Optional[_OBX] = Field(
        default=None,
        title="OBX",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
