"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.CLINICAL_HISTORY
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CCI_I22_CLINICAL_HISTORY_DETAIL import CCI_I22_CLINICAL_HISTORY_DETAIL
from .CCI_I22_ROLE_CLINICAL_HISTORY import CCI_I22_ROLE_CLINICAL_HISTORY

_CCI_I22_CLINICAL_HISTORY_DETAIL = CCI_I22_CLINICAL_HISTORY_DETAIL
_CCI_I22_ROLE_CLINICAL_HISTORY = CCI_I22_ROLE_CLINICAL_HISTORY
_CTI = CTI
_ORC = ORC


class CCI_I22_CLINICAL_HISTORY(BaseModel):
    """HL7 v2 CCI_I22.CLINICAL_HISTORY group.

    Attributes:
        ORC (ORC): required
        CLINICAL_HISTORY_DETAIL (Optional[List[CCI_I22_CLINICAL_HISTORY_DETAIL]]): optional
        ROLE_CLINICAL_HISTORY (Optional[List[CCI_I22_ROLE_CLINICAL_HISTORY]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    CLINICAL_HISTORY_DETAIL: Optional[List[_CCI_I22_CLINICAL_HISTORY_DETAIL]] = Field(
        default=None,
        title="CLINICAL_HISTORY_DETAIL",
        description="Optional, repeating",
    )

    ROLE_CLINICAL_HISTORY: Optional[List[_CCI_I22_ROLE_CLINICAL_HISTORY]] = Field(
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
