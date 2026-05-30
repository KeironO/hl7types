"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SRM_S01.PERSONNEL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIP import AIP
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIP = AIP
_APR = APR
_NTE = NTE


class SRM_S01_PERSONNEL_RESOURCE(HL7Model):
    """HL7 v2 SRM_S01.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): required
        APR (Optional[APR]): optional
        NTE (Optional[List[NTE]]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
