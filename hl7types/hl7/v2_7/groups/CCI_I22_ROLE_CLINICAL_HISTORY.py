"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.ROLE_CLINICAL_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.VAR import VAR

from .CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT import CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT

_CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT = CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT
_VAR = VAR


class CCI_I22_ROLE_CLINICAL_HISTORY(BaseModel):
    """HL7 v2 CCI_I22.ROLE_CLINICAL_HISTORY group.

    Attributes:
        ROLE_CLINICAL_HISTORY_OBJECT (CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_CLINICAL_HISTORY_OBJECT: _CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="ROLE_CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
