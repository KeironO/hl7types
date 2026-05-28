"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORG_O20.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .ORG_O20_OBSERVATION_GROUP import ORG_O20_OBSERVATION_GROUP
from .ORG_O20_SPECIMEN import ORG_O20_SPECIMEN
from .ORG_O20_TIMING import ORG_O20_TIMING

_CTI = CTI
_NTE = NTE
_ORC = ORC
_ORG_O20_OBSERVATION_GROUP = ORG_O20_OBSERVATION_GROUP
_ORG_O20_SPECIMEN = ORG_O20_SPECIMEN
_ORG_O20_TIMING = ORG_O20_TIMING
_PRT = PRT


class ORG_O20_ORDER(BaseModel):
    """HL7 v2 ORG_O20.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[ORG_O20_TIMING]]): optional
        OBSERVATION_GROUP (Optional[ORG_O20_OBSERVATION_GROUP]): optional
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
        SPECIMEN (Optional[List[ORG_O20_SPECIMEN]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_ORG_O20_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBSERVATION_GROUP: Optional[_ORG_O20_OBSERVATION_GROUP] = Field(
        default=None,
        title="OBSERVATION_GROUP",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    SPECIMEN: Optional[List[_ORG_O20_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
