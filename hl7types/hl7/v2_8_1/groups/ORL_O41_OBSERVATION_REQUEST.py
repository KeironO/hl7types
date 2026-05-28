"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O41.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.PRT import PRT

from .ORL_O41_SPECIMEN import ORL_O41_SPECIMEN

_OBR = OBR
_ORL_O41_SPECIMEN = ORL_O41_SPECIMEN
_PRT = PRT


class ORL_O41_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 ORL_O41.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
        SPECIMEN (Optional[List[ORL_O41_SPECIMEN]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    SPECIMEN: Optional[List[_ORL_O41_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
