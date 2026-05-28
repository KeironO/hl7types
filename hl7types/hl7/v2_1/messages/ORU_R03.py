"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORU_R03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ORU_R03_PATIENT_RESULT import ORU_R03_PATIENT_RESULT
from ..segments.DSC import DSC
from ..segments.MSH import MSH

_DSC = DSC
_MSH = MSH
_ORU_R03_PATIENT_RESULT = ORU_R03_PATIENT_RESULT


class ORU_R03(BaseModel):
    """HL7 v2 ORU_R03 message.

    Attributes:
        MSH (MSH): required
        PATIENT_RESULT (List[ORU_R03_PATIENT_RESULT]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    PATIENT_RESULT: list[_ORU_R03_PATIENT_RESULT] = Field(
        default=...,
        title="PATIENT_RESULT",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
