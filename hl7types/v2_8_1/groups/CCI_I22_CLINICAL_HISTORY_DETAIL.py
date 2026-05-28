"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.CLINICAL_HISTORY_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .CCI_I22_CLINICAL_HISTORY_OBJECT import CCI_I22_CLINICAL_HISTORY_OBJECT
from .CCI_I22_CLINICAL_HISTORY_OBSERVATION import CCI_I22_CLINICAL_HISTORY_OBSERVATION

_CCI_I22_CLINICAL_HISTORY_OBJECT = CCI_I22_CLINICAL_HISTORY_OBJECT
_CCI_I22_CLINICAL_HISTORY_OBSERVATION = CCI_I22_CLINICAL_HISTORY_OBSERVATION


class CCI_I22_CLINICAL_HISTORY_DETAIL(BaseModel):
    """HL7 v2 CCI_I22.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCI_I22_CLINICAL_HISTORY_OBJECT): required
        CLINICAL_HISTORY_OBSERVATION (Optional[List[CCI_I22_CLINICAL_HISTORY_OBSERVATION]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCI_I22_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    CLINICAL_HISTORY_OBSERVATION: Optional[List[_CCI_I22_CLINICAL_HISTORY_OBSERVATION]] = Field(
        default=None,
        title="CLINICAL_HISTORY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
