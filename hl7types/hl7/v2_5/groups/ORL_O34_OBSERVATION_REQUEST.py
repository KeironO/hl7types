"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORL_O34.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR

from .ORL_O34_SPMSAC_SUPPGRP2 import ORL_O34_SPMSAC_SUPPGRP2

_OBR = OBR
_ORL_O34_SPMSAC_SUPPGRP2 = ORL_O34_SPMSAC_SUPPGRP2


class ORL_O34_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 ORL_O34.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        SPMSAC_SUPPGRP2 (Optional[List[ORL_O34_SPMSAC_SUPPGRP2]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    SPMSAC_SUPPGRP2: Optional[List[_ORL_O34_SPMSAC_SUPPGRP2]] = Field(
        default=None,
        title="SPMSAC_SUPPGRP2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
