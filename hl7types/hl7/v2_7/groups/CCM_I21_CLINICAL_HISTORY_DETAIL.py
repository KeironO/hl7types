"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCM_I21.CLINICAL_HISTORY_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from .CCM_I21_CLINICAL_HISTORY_OBJECT import CCM_I21_CLINICAL_HISTORY_OBJECT

_CCM_I21_CLINICAL_HISTORY_OBJECT = CCM_I21_CLINICAL_HISTORY_OBJECT
_OBX = OBX


class CCM_I21_CLINICAL_HISTORY_DETAIL(BaseModel):
    """HL7 v2 CCM_I21.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCM_I21_CLINICAL_HISTORY_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCM_I21_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
