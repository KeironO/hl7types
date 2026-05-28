"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SQM_S25.PERSONNEL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.AIP import AIP
from ..segments.APR import APR

_AIP = AIP
_APR = APR


class SQM_S25_PERSONNEL_RESOURCE(BaseModel):
    """HL7 v2 SQM_S25.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): required
        APR (Optional[APR]): optional
    """

    AIP: _AIP = Field(
        default=...,
        title="AIP",
        description="Required",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
