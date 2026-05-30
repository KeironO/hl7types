"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQR_S25.GENERAL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.NTE import NTE

_AIG = AIG
_NTE = NTE


class SQR_S25_GENERAL_RESOURCE(HL7Model):
    """HL7 v2 SQR_S25.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): required
        NTE (Optional[List[NTE]]): optional
    """

    AIG: _AIG = Field(
        default=...,
        title="AIG",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
