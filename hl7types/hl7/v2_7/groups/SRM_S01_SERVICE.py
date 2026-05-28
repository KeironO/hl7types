"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SRM_S01.SERVICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIS import AIS
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIS = AIS
_APR = APR
_NTE = NTE


class SRM_S01_SERVICE(BaseModel):
    """HL7 v2 SRM_S01.SERVICE group.

    Attributes:
        AIS (AIS): required
        APR (Optional[APR]): optional
        NTE (Optional[List[NTE]]): optional
    """

    AIS: _AIS = Field(
        default=...,
        title="AIS",
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
