"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SAC import SAC

_OBX = OBX
_SAC = SAC


class ORL_O22_CONTAINER(HL7Model):
    """HL7 v2 ORL_O22.CONTAINER group.

    Attributes:
        SAC (SAC): Specimen and container detail, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen and container detail",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)
