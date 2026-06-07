"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORU_R03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH

from ..groups.ORU_R03_PATIENT_RESULT import ORU_R03_PATIENT_RESULT

_DSC = DSC
_MSH = MSH
_ORU_R03_PATIENT_RESULT = ORU_R03_PATIENT_RESULT


class ORU_R03(HL7Model):
    """HL7 v2 ORU_R03 message.

    Attributes:
        MSH (MSH): required
        PATIENT_RESULT (List[ORU_R03_PATIENT_RESULT]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    PATIENT_RESULT: List[_ORU_R03_PATIENT_RESULT] = Field(
        min_length=1,
        title="PATIENT_RESULT",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
