"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCM_I21.ROLE_CLINICAL_HISTORY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.VAR import VAR
from .CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT import CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT

_CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT = CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT
_VAR = VAR


class CCM_I21_ROLE_CLINICAL_HISTORY(BaseModel):
    """HL7 v2 CCM_I21.ROLE_CLINICAL_HISTORY group.

    Attributes:
        ROLE_CLINICAL_HISTORY_OBJECT (CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_CLINICAL_HISTORY_OBJECT: _CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="ROLE_CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
