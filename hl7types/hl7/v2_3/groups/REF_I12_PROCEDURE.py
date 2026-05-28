"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: REF_I12.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.PR1 import PR1

from .REF_I12_AUTCTD_SUPPGRP2 import REF_I12_AUTCTD_SUPPGRP2

_PR1 = PR1
_REF_I12_AUTCTD_SUPPGRP2 = REF_I12_AUTCTD_SUPPGRP2


class REF_I12_PROCEDURE(BaseModel):
    """HL7 v2 REF_I12.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTCTD_SUPPGRP2 (Optional[REF_I12_AUTCTD_SUPPGRP2]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTCTD_SUPPGRP2: Optional[_REF_I12_AUTCTD_SUPPGRP2] = Field(
        default=None,
        title="AUTCTD_SUPPGRP2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
