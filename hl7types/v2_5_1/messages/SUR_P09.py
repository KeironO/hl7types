"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SUR_P09
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH

from ..groups.SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP import SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP

_MSH = MSH
_SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP = SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP


class SUR_P09(BaseModel):
    """HL7 v2 SUR_P09 message.

    Attributes:
        MSH (MSH): required
        FACPSHPDCPSHFACPDCNTEED_SUPPGRP (List[SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    FACPSHPDCPSHFACPDCNTEED_SUPPGRP: List[_SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP] = Field(
        default=...,
        title="FACPSHPDCPSHFACPDCNTEED_SUPPGRP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
