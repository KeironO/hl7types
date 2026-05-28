"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCM_I21.MEDICATION_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CCM_I21_MEDICATION_ADMINISTRATION_DETAIL import CCM_I21_MEDICATION_ADMINISTRATION_DETAIL
from .CCM_I21_MEDICATION_ENCODING_DETAIL import CCM_I21_MEDICATION_ENCODING_DETAIL
from .CCM_I21_MEDICATION_ORDER_DETAIL import CCM_I21_MEDICATION_ORDER_DETAIL

_CCM_I21_MEDICATION_ADMINISTRATION_DETAIL = CCM_I21_MEDICATION_ADMINISTRATION_DETAIL
_CCM_I21_MEDICATION_ENCODING_DETAIL = CCM_I21_MEDICATION_ENCODING_DETAIL
_CCM_I21_MEDICATION_ORDER_DETAIL = CCM_I21_MEDICATION_ORDER_DETAIL
_CTI = CTI
_ORC = ORC


class CCM_I21_MEDICATION_HISTORY(BaseModel):
    """HL7 v2 CCM_I21.MEDICATION_HISTORY group.

    Attributes:
        ORC (ORC): required
        MEDICATION_ORDER_DETAIL (Optional[CCM_I21_MEDICATION_ORDER_DETAIL]): optional
        MEDICATION_ENCODING_DETAIL (Optional[CCM_I21_MEDICATION_ENCODING_DETAIL]): optional
        MEDICATION_ADMINISTRATION_DETAIL (Optional[List[CCM_I21_MEDICATION_ADMINISTRATION_DETAIL]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    MEDICATION_ORDER_DETAIL: Optional[_CCM_I21_MEDICATION_ORDER_DETAIL] = Field(
        default=None,
        title="MEDICATION_ORDER_DETAIL",
        description="Optional",
    )

    MEDICATION_ENCODING_DETAIL: Optional[_CCM_I21_MEDICATION_ENCODING_DETAIL] = Field(
        default=None,
        title="MEDICATION_ENCODING_DETAIL",
        description="Optional",
    )

    MEDICATION_ADMINISTRATION_DETAIL: Optional[List[_CCM_I21_MEDICATION_ADMINISTRATION_DETAIL]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_DETAIL",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
