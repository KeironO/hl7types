"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SRM_S01.GENERAL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIG = AIG
_APR = APR
_NTE = NTE


class SRM_S01_GENERAL_RESOURCE(HL7Model):
    """HL7 v2 SRM_S01.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): required
        APR (Optional[APR]): optional
        NTE (Optional[List[NTE]]): optional
    """

    AIG: _AIG = Field(
        default=...,
        title="AIG",
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
