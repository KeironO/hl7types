"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPU_R25.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.INV import INV
from ..segments.SAC import SAC

_INV = INV
_SAC = SAC


class OPU_R25_CONTAINER(HL7Model):
    """HL7 v2 OPU_R25.CONTAINER group.

    Attributes:
        SAC (SAC): required
        INV (Optional[INV]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    INV: Optional[_INV] = Field(
        default=None,
        title="INV",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
