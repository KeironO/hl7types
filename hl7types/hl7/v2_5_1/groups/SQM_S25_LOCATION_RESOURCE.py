"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SQM_S25.LOCATION_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.AIL import AIL
from ..segments.APR import APR

_AIL = AIL
_APR = APR


class SQM_S25_LOCATION_RESOURCE(BaseModel):
    """HL7 v2 SQM_S25.LOCATION_RESOURCE group.

    Attributes:
        AIL (AIL): required
        APR (Optional[APR]): optional
    """

    AIL: _AIL = Field(
        default=...,
        title="AIL",
        description="Required",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
