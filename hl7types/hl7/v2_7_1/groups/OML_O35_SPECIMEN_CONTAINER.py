"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O35.SPECIMEN_CONTAINER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from .OML_O35_ORDER import OML_O35_ORDER

_OML_O35_ORDER = OML_O35_ORDER
_SAC = SAC


class OML_O35_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 OML_O35.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        ORDER (List[OML_O35_ORDER]): required
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    ORDER: list[_OML_O35_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
