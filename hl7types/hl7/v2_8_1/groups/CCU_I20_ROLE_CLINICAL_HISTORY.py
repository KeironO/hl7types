"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.ROLE_CLINICAL_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.VAR import VAR

from .CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT import CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT

_CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT = CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT
_VAR = VAR


class CCU_I20_ROLE_CLINICAL_HISTORY(HL7Model):
    """HL7 v2 CCU_I20.ROLE_CLINICAL_HISTORY group.

    Attributes:
        ROLE_CLINICAL_HISTORY_OBJECT (CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_CLINICAL_HISTORY_OBJECT: _CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT = Field(
        title="ROLE_CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
