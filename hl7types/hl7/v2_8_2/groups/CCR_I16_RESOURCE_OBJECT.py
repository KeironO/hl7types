"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.RESOURCE_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.AIL import AIL
from ..segments.AIP import AIP
from ..segments.AIS import AIS

_AIG = AIG
_AIL = AIL
_AIP = AIP
_AIS = AIS


class CCR_I16_RESOURCE_OBJECT(HL7Model):
    """HL7 v2 CCR_I16.RESOURCE_OBJECT group.

    Attributes:
        AIS (Optional[AIS]): optional
        AIG (Optional[AIG]): optional
        AIL (Optional[AIL]): optional
        AIP (Optional[AIP]): optional
    """

    AIS: Optional[_AIS] = Field(
        default=None,
        title="AIS",
        description="Optional",
    )

    AIG: Optional[_AIG] = Field(
        default=None,
        title="AIG",
        description="Optional",
    )

    AIL: Optional[_AIL] = Field(
        default=None,
        title="AIL",
        description="Optional",
    )

    AIP: Optional[_AIP] = Field(
        default=None,
        title="AIP",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
