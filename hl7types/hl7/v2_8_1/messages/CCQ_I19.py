"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCQ_I19
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.CCQ_I19_PROVIDER_CONTACT import CCQ_I19_PROVIDER_CONTACT
from ..segments.MSH import MSH
from ..segments.REL import REL
from ..segments.RF1 import RF1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_CCQ_I19_PROVIDER_CONTACT = CCQ_I19_PROVIDER_CONTACT
_MSH = MSH
_REL = REL
_RF1 = RF1
_SFT = SFT
_UAC = UAC


class CCQ_I19(BaseModel):
    """HL7 v2 CCQ_I19 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        RF1 (RF1): required
        PROVIDER_CONTACT (Optional[List[CCQ_I19_PROVIDER_CONTACT]]): optional
        REL (Optional[List[REL]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    RF1: _RF1 = Field(
        default=...,
        title="RF1",
        description="Required",
    )

    PROVIDER_CONTACT: list[_CCQ_I19_PROVIDER_CONTACT] | None = Field(
        default=None,
        title="PROVIDER_CONTACT",
        description="Optional, repeating",
    )

    REL: list[_REL] | None = Field(
        default=None,
        title="REL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
