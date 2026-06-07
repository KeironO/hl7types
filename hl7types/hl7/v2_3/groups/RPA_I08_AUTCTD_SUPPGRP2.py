"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPA_I08.AUTCTD_SUPPGRP2
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AUT import AUT
from ..segments.CTD import CTD

_AUT = AUT
_CTD = CTD


class RPA_I08_AUTCTD_SUPPGRP2(HL7Model):
    """HL7 v2 RPA_I08.AUTCTD_SUPPGRP2 group.

    Attributes:
        AUT (AUT): required
        CTD (Optional[CTD]): optional
    """

    AUT: _AUT = Field(
        title="AUT",
        description="Required",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
