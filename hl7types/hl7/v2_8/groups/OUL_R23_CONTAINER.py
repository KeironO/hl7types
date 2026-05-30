"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OUL_R23.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.INV import INV
from ..segments.SAC import SAC

from .OUL_R23_ORDER import OUL_R23_ORDER

_INV = INV
_OUL_R23_ORDER = OUL_R23_ORDER
_SAC = SAC


class OUL_R23_CONTAINER(HL7Model):
    """HL7 v2 OUL_R23.CONTAINER group.

    Attributes:
        SAC (SAC): required
        INV (Optional[INV]): optional
        ORDER (List[OUL_R23_ORDER]): required
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

    ORDER: List[_OUL_R23_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
