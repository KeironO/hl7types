"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCU_I20.CLINICAL_HISTORY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from .CCU_I20_CLINICAL_HISTORY_DETAIL import CCU_I20_CLINICAL_HISTORY_DETAIL
from .CCU_I20_ROLE_CLINICAL_HISTORY import CCU_I20_ROLE_CLINICAL_HISTORY

_CCU_I20_CLINICAL_HISTORY_DETAIL = CCU_I20_CLINICAL_HISTORY_DETAIL
_CCU_I20_ROLE_CLINICAL_HISTORY = CCU_I20_ROLE_CLINICAL_HISTORY
_CTI = CTI
_ORC = ORC


class CCU_I20_CLINICAL_HISTORY(BaseModel):
    """HL7 v2 CCU_I20.CLINICAL_HISTORY group.

    Attributes:
        ORC (ORC): required
        CLINICAL_HISTORY_DETAIL (Optional[List[CCU_I20_CLINICAL_HISTORY_DETAIL]]): optional
        ROLE_CLINICAL_HISTORY (Optional[List[CCU_I20_ROLE_CLINICAL_HISTORY]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    CLINICAL_HISTORY_DETAIL: list[_CCU_I20_CLINICAL_HISTORY_DETAIL] | None = Field(
        default=None,
        title="CLINICAL_HISTORY_DETAIL",
        description="Optional, repeating",
    )

    ROLE_CLINICAL_HISTORY: list[_CCU_I20_ROLE_CLINICAL_HISTORY] | None = Field(
        default=None,
        title="ROLE_CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
