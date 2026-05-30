"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPA_I08.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1

from .RPA_I08_AUTCTD_SUPPGRP2 import RPA_I08_AUTCTD_SUPPGRP2

_PR1 = PR1
_RPA_I08_AUTCTD_SUPPGRP2 = RPA_I08_AUTCTD_SUPPGRP2


class RPA_I08_PROCEDURE(HL7Model):
    """HL7 v2 RPA_I08.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTCTD_SUPPGRP2 (Optional[RPA_I08_AUTCTD_SUPPGRP2]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTCTD_SUPPGRP2: Optional[_RPA_I08_AUTCTD_SUPPGRP2] = Field(
        default=None,
        title="AUTCTD_SUPPGRP2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
