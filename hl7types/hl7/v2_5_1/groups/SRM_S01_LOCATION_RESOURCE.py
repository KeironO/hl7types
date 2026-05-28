"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SRM_S01.LOCATION_RESOURCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIL import AIL
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIL = AIL
_APR = APR
_NTE = NTE


class SRM_S01_LOCATION_RESOURCE(BaseModel):
    """HL7 v2 SRM_S01.LOCATION_RESOURCE group.

    Attributes:
        AIL (AIL): required
        APR (Optional[APR]): optional
        NTE (Optional[List[NTE]]): optional
    """

    AIL: _AIL = Field(
        default=...,
        title="AIL",
        description="Required",
    )

    APR: _APR | None = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
