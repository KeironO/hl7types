"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQA_I08.AUTCTD_SUPPGRP2
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.AUT import AUT
from ..segments.CTD import CTD

_AUT = AUT
_CTD = CTD


class RQA_I08_AUTCTD_SUPPGRP2(BaseModel):
    """HL7 v2 RQA_I08.AUTCTD_SUPPGRP2 group.

    Attributes:
        AUT (AUT): required
        CTD (Optional[CTD]): optional
    """

    AUT: _AUT = Field(
        default=...,
        title="AUT",
        description="Required",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
