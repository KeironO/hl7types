"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.CLINICAL_HISTORY_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .CCR_I16_CLINICAL_HISTORY_OBJECT import CCR_I16_CLINICAL_HISTORY_OBJECT
from .CCR_I16_CLINICAL_HISTORY_OBSERVATION import CCR_I16_CLINICAL_HISTORY_OBSERVATION

_CCR_I16_CLINICAL_HISTORY_OBJECT = CCR_I16_CLINICAL_HISTORY_OBJECT
_CCR_I16_CLINICAL_HISTORY_OBSERVATION = CCR_I16_CLINICAL_HISTORY_OBSERVATION


class CCR_I16_CLINICAL_HISTORY_DETAIL(BaseModel):
    """HL7 v2 CCR_I16.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCR_I16_CLINICAL_HISTORY_OBJECT): required
        CLINICAL_HISTORY_OBSERVATION (Optional[List[CCR_I16_CLINICAL_HISTORY_OBSERVATION]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCR_I16_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    CLINICAL_HISTORY_OBSERVATION: list[_CCR_I16_CLINICAL_HISTORY_OBSERVATION] | None = Field(
        default=None,
        title="CLINICAL_HISTORY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
