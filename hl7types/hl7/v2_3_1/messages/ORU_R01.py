"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORU_R01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH

from ..groups.ORU_R01_PATIENT_RESULT import ORU_R01_PATIENT_RESULT

_DSC = DSC
_MSH = MSH
_ORU_R01_PATIENT_RESULT = ORU_R01_PATIENT_RESULT


class ORU_R01(HL7Model):
    """ORU/ACK - Unsolicited transmission of an observation message.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PATIENT_RESULT (List[ORU_R01_PATIENT_RESULT]): required
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    PATIENT_RESULT: List[_ORU_R01_PATIENT_RESULT] = Field(
        min_length=1,
        title="PATIENT_RESULT",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
