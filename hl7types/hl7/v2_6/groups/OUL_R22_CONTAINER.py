"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R22.CONTAINER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.INV import INV
from ..segments.SAC import SAC

_INV = INV
_SAC = SAC


class OUL_R22_CONTAINER(BaseModel):
    """HL7 v2 OUL_R22.CONTAINER group.

    Attributes:
        SAC (SAC): required
        INV (Optional[INV]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    INV: _INV | None = Field(
        default=None,
        title="INV",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
