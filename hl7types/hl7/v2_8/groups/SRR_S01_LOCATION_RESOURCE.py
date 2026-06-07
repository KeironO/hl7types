"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SRR_S01.LOCATION_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIL import AIL
from ..segments.NTE import NTE

_AIL = AIL
_NTE = NTE


class SRR_S01_LOCATION_RESOURCE(HL7Model):
    """HL7 v2 SRR_S01.LOCATION_RESOURCE group.

    Attributes:
        AIL (AIL): required
        NTE (Optional[List[NTE]]): optional
    """

    AIL: _AIL = Field(
        title="AIL",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
