"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION

_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION


class ORU_R01_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): COMMOM ORDER, optional
        OBR (OBR): OBSERVATION REQUEST, required
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
        OBSERVATION (List[ORU_R01_OBSERVATION]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="COMMOM ORDER",
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

    OBSERVATION: List[_ORU_R01_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
