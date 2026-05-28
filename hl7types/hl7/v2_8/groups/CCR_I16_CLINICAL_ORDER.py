"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.CLINICAL_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from .CCR_I16_CLINICAL_ORDER_DETAIL import CCR_I16_CLINICAL_ORDER_DETAIL
from .CCR_I16_CLINICAL_ORDER_TIMING import CCR_I16_CLINICAL_ORDER_TIMING

_CCR_I16_CLINICAL_ORDER_DETAIL = CCR_I16_CLINICAL_ORDER_DETAIL
_CCR_I16_CLINICAL_ORDER_TIMING = CCR_I16_CLINICAL_ORDER_TIMING
_CTI = CTI
_ORC = ORC


class CCR_I16_CLINICAL_ORDER(BaseModel):
    """HL7 v2 CCR_I16.CLINICAL_ORDER group.

    Attributes:
        ORC (ORC): required
        CLINICAL_ORDER_TIMING (Optional[List[CCR_I16_CLINICAL_ORDER_TIMING]]): optional
        CLINICAL_ORDER_DETAIL (List[CCR_I16_CLINICAL_ORDER_DETAIL]): required
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    CLINICAL_ORDER_TIMING: list[_CCR_I16_CLINICAL_ORDER_TIMING] | None = Field(
        default=None,
        title="CLINICAL_ORDER_TIMING",
        description="Optional, repeating",
    )

    CLINICAL_ORDER_DETAIL: list[_CCR_I16_CLINICAL_ORDER_DETAIL] = Field(
        default=...,
        title="CLINICAL_ORDER_DETAIL",
        description="Required, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
