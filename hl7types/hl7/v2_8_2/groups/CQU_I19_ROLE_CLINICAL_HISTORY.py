"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.ROLE_CLINICAL_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.VAR import VAR

from .CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT import CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT

_CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT = CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT
_VAR = VAR


class CQU_I19_ROLE_CLINICAL_HISTORY(HL7Model):
    """HL7 v2 CQU_I19.ROLE_CLINICAL_HISTORY group.

    Attributes:
        ROLE_CLINICAL_HISTORY_OBJECT (CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_CLINICAL_HISTORY_OBJECT: _CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT = Field(
        title="ROLE_CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
