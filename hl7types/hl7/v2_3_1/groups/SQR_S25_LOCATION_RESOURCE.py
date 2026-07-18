"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQR_S25.LOCATION_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AIL import AIL
from ..segments.NTE import NTE

_AIL = AIL
_NTE = NTE


class SQR_S25_LOCATION_RESOURCE(HL7Model):
    """HL7 v2 SQR_S25.LOCATION_RESOURCE group.

    Attributes:
        AIL (AIL): AIL - appointment information - location resource segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    AIL: _AIL = Field(
        title="AIL",
        description="AIL - appointment information - location resource segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
