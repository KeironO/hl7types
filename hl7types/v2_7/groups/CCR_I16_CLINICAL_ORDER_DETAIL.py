"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.CLINICAL_ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX

from .CCR_I16_CLINICAL_ORDER_OBJECT import CCR_I16_CLINICAL_ORDER_OBJECT

_CCR_I16_CLINICAL_ORDER_OBJECT = CCR_I16_CLINICAL_ORDER_OBJECT
_OBX = OBX


class CCR_I16_CLINICAL_ORDER_DETAIL(BaseModel):
    """HL7 v2 CCR_I16.CLINICAL_ORDER_DETAIL group.

    Attributes:
        CLINICAL_ORDER_OBJECT (CCR_I16_CLINICAL_ORDER_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    CLINICAL_ORDER_OBJECT: _CCR_I16_CLINICAL_ORDER_OBJECT = Field(
        default=...,
        title="CLINICAL_ORDER_OBJECT",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
