"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQM_S25.LOCATION_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AIL import AIL
from ..segments.APR import APR

_AIL = AIL
_APR = APR


class SQM_S25_LOCATION_RESOURCE(HL7Model):
    """HL7 v2 SQM_S25.LOCATION_RESOURCE group.

    Attributes:
        AIL (AIL): AIL - appointment information - location resource segment, required
        APR (Optional[APR]): APR - appointment preferences segment, optional
    """

    AIL: _AIL = Field(
        title="AIL",
        description="AIL - appointment information - location resource segment",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="APR - appointment preferences segment",
    )

    model_config = ConfigDict(populate_by_name=True)
