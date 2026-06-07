"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R21.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC
from ..segments.SID import SID

_SAC = SAC
_SID = SID


class OUL_R21_CONTAINER(HL7Model):
    """HL7 v2 OUL_R21.CONTAINER group.

    Attributes:
        SAC (SAC): required
        SID (Optional[SID]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Required",
    )

    SID: Optional[_SID] = Field(
        default=None,
        title="SID",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
