"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R21.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC
from ..segments.SID import SID

_SAC = SAC
_SID = SID


class OUL_R21_CONTAINER(HL7Model):
    """HL7 v2 OUL_R21.CONTAINER group.

    Attributes:
        SAC (SAC): Specimen Container detail, required
        SID (Optional[SID]): Substance Identifier, optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen Container detail",
    )

    SID: Optional[_SID] = Field(
        default=None,
        title="SID",
        description="Substance Identifier",
    )

    model_config = ConfigDict(populate_by_name=True)
