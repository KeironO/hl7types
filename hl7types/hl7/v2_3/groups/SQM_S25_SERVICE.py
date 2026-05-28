"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SQM_S25.SERVICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIS import AIS
from ..segments.APR import APR

_AIS = AIS
_APR = APR


class SQM_S25_SERVICE(BaseModel):
    """HL7 v2 SQM_S25.SERVICE group.

    Attributes:
        AIS (AIS): required
        APR (Optional[APR]): optional
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

    model_config = {"populate_by_name": True}
