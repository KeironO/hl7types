"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORU_R01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH

from ..groups.ORU_R01_RESPONSE import ORU_R01_RESPONSE

_DSC = DSC
_MSH = MSH
_ORU_R01_RESPONSE = ORU_R01_RESPONSE


class ORU_R01(HL7Model):
    """HL7 v2 ORU_R01 message.

    Attributes:
        MSH (MSH): required
        RESPONSE (List[ORU_R01_RESPONSE]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    RESPONSE: List[_ORU_R01_RESPONSE] = Field(
        min_length=1,
        title="RESPONSE",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
