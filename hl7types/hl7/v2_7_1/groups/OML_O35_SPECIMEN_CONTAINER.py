"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O35.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

from .OML_O35_ORDER import OML_O35_ORDER

_OML_O35_ORDER = OML_O35_ORDER
_SAC = SAC


class OML_O35_SPECIMEN_CONTAINER(HL7Model):
    """HL7 v2 OML_O35.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): Specimen Container detail, required
        ORDER (List[OML_O35_ORDER]): required
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen Container detail",
    )

    ORDER: List[_OML_O35_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
