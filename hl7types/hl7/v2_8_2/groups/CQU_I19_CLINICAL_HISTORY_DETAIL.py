"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.CLINICAL_HISTORY_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .CQU_I19_CLINICAL_HISTORY_OBJECT import CQU_I19_CLINICAL_HISTORY_OBJECT
from .CQU_I19_CLINICAL_HISTORY_OBSERVATION import CQU_I19_CLINICAL_HISTORY_OBSERVATION

_CQU_I19_CLINICAL_HISTORY_OBJECT = CQU_I19_CLINICAL_HISTORY_OBJECT
_CQU_I19_CLINICAL_HISTORY_OBSERVATION = CQU_I19_CLINICAL_HISTORY_OBSERVATION


class CQU_I19_CLINICAL_HISTORY_DETAIL(HL7Model):
    """HL7 v2 CQU_I19.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CQU_I19_CLINICAL_HISTORY_OBJECT): required
        CLINICAL_HISTORY_OBSERVATION (Optional[List[CQU_I19_CLINICAL_HISTORY_OBSERVATION]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CQU_I19_CLINICAL_HISTORY_OBJECT = Field(
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    CLINICAL_HISTORY_OBSERVATION: Optional[List[_CQU_I19_CLINICAL_HISTORY_OBSERVATION]] = Field(
        default=None,
        title="CLINICAL_HISTORY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
