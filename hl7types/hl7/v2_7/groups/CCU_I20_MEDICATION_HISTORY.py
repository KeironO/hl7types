"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCU_I20.MEDICATION_HISTORY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from .CCU_I20_MEDICATION_ADMINISTRATION_DETAIL import CCU_I20_MEDICATION_ADMINISTRATION_DETAIL
from .CCU_I20_MEDICATION_ENCODING_DETAIL import CCU_I20_MEDICATION_ENCODING_DETAIL
from .CCU_I20_MEDICATION_ORDER_DETAIL import CCU_I20_MEDICATION_ORDER_DETAIL

_CCU_I20_MEDICATION_ADMINISTRATION_DETAIL = CCU_I20_MEDICATION_ADMINISTRATION_DETAIL
_CCU_I20_MEDICATION_ENCODING_DETAIL = CCU_I20_MEDICATION_ENCODING_DETAIL
_CCU_I20_MEDICATION_ORDER_DETAIL = CCU_I20_MEDICATION_ORDER_DETAIL
_CTI = CTI
_ORC = ORC


class CCU_I20_MEDICATION_HISTORY(BaseModel):
    """HL7 v2 CCU_I20.MEDICATION_HISTORY group.

    Attributes:
        ORC (ORC): required
        MEDICATION_ORDER_DETAIL (Optional[CCU_I20_MEDICATION_ORDER_DETAIL]): optional
        MEDICATION_ENCODING_DETAIL (Optional[CCU_I20_MEDICATION_ENCODING_DETAIL]): optional
        MEDICATION_ADMINISTRATION_DETAIL (Optional[List[CCU_I20_MEDICATION_ADMINISTRATION_DETAIL]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    MEDICATION_ORDER_DETAIL: _CCU_I20_MEDICATION_ORDER_DETAIL | None = Field(
        default=None,
        title="MEDICATION_ORDER_DETAIL",
        description="Optional",
    )

    MEDICATION_ENCODING_DETAIL: _CCU_I20_MEDICATION_ENCODING_DETAIL | None = Field(
        default=None,
        title="MEDICATION_ENCODING_DETAIL",
        description="Optional",
    )

    MEDICATION_ADMINISTRATION_DETAIL: list[_CCU_I20_MEDICATION_ADMINISTRATION_DETAIL] | None = (
        Field(
            default=None,
            title="MEDICATION_ADMINISTRATION_DETAIL",
            description="Optional, repeating",
        )
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
