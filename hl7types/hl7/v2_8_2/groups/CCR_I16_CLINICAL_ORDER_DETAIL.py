"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.CLINICAL_ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .CCR_I16_CLINICAL_ORDER_OBJECT import CCR_I16_CLINICAL_ORDER_OBJECT
from .CCR_I16_CLINICAL_ORDER_OBSERVATION import CCR_I16_CLINICAL_ORDER_OBSERVATION

_CCR_I16_CLINICAL_ORDER_OBJECT = CCR_I16_CLINICAL_ORDER_OBJECT
_CCR_I16_CLINICAL_ORDER_OBSERVATION = CCR_I16_CLINICAL_ORDER_OBSERVATION


class CCR_I16_CLINICAL_ORDER_DETAIL(BaseModel):
    """HL7 v2 CCR_I16.CLINICAL_ORDER_DETAIL group.

    Attributes:
        CLINICAL_ORDER_OBJECT (CCR_I16_CLINICAL_ORDER_OBJECT): required
        CLINICAL_ORDER_OBSERVATION (Optional[List[CCR_I16_CLINICAL_ORDER_OBSERVATION]]): optional
    """

    CLINICAL_ORDER_OBJECT: _CCR_I16_CLINICAL_ORDER_OBJECT = Field(
        default=...,
        title="CLINICAL_ORDER_OBJECT",
        description="Required",
    )

    CLINICAL_ORDER_OBSERVATION: list[_CCR_I16_CLINICAL_ORDER_OBSERVATION] | None = Field(
        default=None,
        title="CLINICAL_ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
