"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORF_R04.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORF_R04_OBSERVATION import ORF_R04_OBSERVATION

_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORF_R04_OBSERVATION = ORF_R04_OBSERVATION


class ORF_R04_ORDER(HL7Model):
    """HL7 v2 ORF_R04.ORDER group.

    Attributes:
        ORC (Optional[ORC]): COMMOM ORDER, optional
        OBR (OBR): OBSERVATION REQUEST, required
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
        OBSERVATION (List[ORF_R04_OBSERVATION]): required
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

    OBSERVATION: List[_ORF_R04_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
