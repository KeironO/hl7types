"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SRM_S01.SERVICE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
