"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SQM_S25.REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.APR import APR
from ..segments.ARQ import ARQ
from ..segments.PID import PID

from .SQM_S25_RESOURCES import SQM_S25_RESOURCES

_APR = APR
_ARQ = ARQ
_PID = PID
_SQM_S25_RESOURCES = SQM_S25_RESOURCES


class SQM_S25_REQUEST(BaseModel):
    """HL7 v2 SQM_S25.REQUEST group.

    Attributes:
        ARQ (ARQ): required
        APR (Optional[APR]): optional
        PID (Optional[PID]): optional
        RESOURCES (List[SQM_S25_RESOURCES]): required
    """

    ARQ: _ARQ = Field(
        default=...,
        title="ARQ",
        description="Required",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    RESOURCES: List[_SQM_S25_RESOURCES] = Field(
        default=...,
        title="RESOURCES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
