"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RQA_I08.AUTCTD_SUPPGRP2
Type: Group
"""

from __future__ import annotations

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

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
