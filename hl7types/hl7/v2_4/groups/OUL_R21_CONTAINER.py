"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OUL_R21.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SID import SID

_OBX = OBX
_SAC = SAC
_SID = SID


class OUL_R21_CONTAINER(HL7Model):
    """HL7 v2 OUL_R21.CONTAINER group.

    Attributes:
        SAC (SAC): Specimen and container detail, required
        SID (Optional[SID]): Substance Identifier, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen and container detail",
    )

    SID: Optional[_SID] = Field(
        default=None,
        title="SID",
        description="Substance Identifier",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
