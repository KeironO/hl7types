"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORU_R01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH

from ..groups.ORU_R01_RESPONSE import ORU_R01_RESPONSE

_DSC = DSC
_MSH = MSH
_ORU_R01_RESPONSE = ORU_R01_RESPONSE


class ORU_R01(HL7Model):
    """ORU/ACK - Unsolicited transmission of an observation.

    Attributes:
        MSH (MSH): Message header segment, required
        RESPONSE (List[ORU_R01_RESPONSE]): required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    RESPONSE: List[_ORU_R01_RESPONSE] = Field(
        min_length=1,
        title="RESPONSE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
