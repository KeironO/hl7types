"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORU_R03.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORU_R03_OBSERVATION import ORU_R03_OBSERVATION

_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R03_OBSERVATION = ORU_R03_OBSERVATION


class ORU_R03_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 ORU_R03.ORDER_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): COMMON ORDER, optional
        OBR (OBR): OBSERVATION REQUEST, required
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
        OBSERVATION (List[ORU_R03_OBSERVATION]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="COMMON ORDER",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="OBSERVATION REQUEST",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    OBSERVATION: List[_ORU_R03_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
