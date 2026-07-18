"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRI_I12.AUTCTD_SUPPGRP2
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AUT import AUT
from ..segments.CTD import CTD

_AUT = AUT
_CTD = CTD


class RRI_I12_AUTCTD_SUPPGRP2(HL7Model):
    """HL7 v2 RRI_I12.AUTCTD_SUPPGRP2 group.

    Attributes:
        AUT (AUT): Authorization Information, required
        CTD (Optional[CTD]): Contact Data, optional
    """

    AUT: _AUT = Field(
        title="AUT",
        description="Authorization Information",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    model_config = ConfigDict(populate_by_name=True)
