"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O43.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

from .ORL_O43_ORDER import ORL_O43_ORDER

_ORL_O43_ORDER = ORL_O43_ORDER
_SAC = SAC


class ORL_O43_SPECIMEN_CONTAINER(HL7Model):
    """HL7 v2 ORL_O43.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): Specimen Container detail, required
        ORDER (Optional[List[ORL_O43_ORDER]]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen Container detail",
    )

    ORDER: Optional[List[_ORL_O43_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
