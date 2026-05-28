"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQM_S25.GENERAL_RESOURCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIG import AIG
from ..segments.APR import APR

_AIG = AIG
_APR = APR


class SQM_S25_GENERAL_RESOURCE(BaseModel):
    """HL7 v2 SQM_S25.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): required
        APR (Optional[APR]): optional
    """

    AIG: _AIG = Field(
        default=...,
        title="AIG",
        description="Required",
    )

    APR: _APR | None = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
