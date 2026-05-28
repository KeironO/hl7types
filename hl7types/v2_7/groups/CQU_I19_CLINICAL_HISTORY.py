"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CQU_I19.CLINICAL_HISTORY
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CQU_I19_CLINICAL_HISTORY_DETAIL import CQU_I19_CLINICAL_HISTORY_DETAIL
from .CQU_I19_ROLE_CLINICAL_HISTORY import CQU_I19_ROLE_CLINICAL_HISTORY

_CQU_I19_CLINICAL_HISTORY_DETAIL = CQU_I19_CLINICAL_HISTORY_DETAIL
_CQU_I19_ROLE_CLINICAL_HISTORY = CQU_I19_ROLE_CLINICAL_HISTORY
_CTI = CTI
_ORC = ORC


class CQU_I19_CLINICAL_HISTORY(BaseModel):
    """HL7 v2 CQU_I19.CLINICAL_HISTORY group.

    Attributes:
        ORC (ORC): required
        CLINICAL_HISTORY_DETAIL (Optional[List[CQU_I19_CLINICAL_HISTORY_DETAIL]]): optional
        ROLE_CLINICAL_HISTORY (Optional[List[CQU_I19_ROLE_CLINICAL_HISTORY]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    CLINICAL_HISTORY_DETAIL: Optional[List[_CQU_I19_CLINICAL_HISTORY_DETAIL]] = Field(
        default=None,
        title="CLINICAL_HISTORY_DETAIL",
        description="Optional, repeating",
    )

    ROLE_CLINICAL_HISTORY: Optional[List[_CQU_I19_ROLE_CLINICAL_HISTORY]] = Field(
        default=None,
        title="ROLE_CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
