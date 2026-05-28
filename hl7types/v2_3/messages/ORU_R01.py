"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORU_R01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH

from ..groups.ORU_R01_RESPONSE import ORU_R01_RESPONSE

_DSC = DSC
_MSH = MSH
_ORU_R01_RESPONSE = ORU_R01_RESPONSE


class ORU_R01(BaseModel):
    """HL7 v2 ORU_R01 message.

    Attributes:
        MSH (MSH): required
        RESPONSE (List[ORU_R01_RESPONSE]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    RESPONSE: List[_ORU_R01_RESPONSE] = Field(
        default=...,
        title="RESPONSE",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
