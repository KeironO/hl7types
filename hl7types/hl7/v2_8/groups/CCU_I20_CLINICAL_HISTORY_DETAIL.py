"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCU_I20.CLINICAL_HISTORY_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .CCU_I20_CLINICAL_HISTORY_OBJECT import CCU_I20_CLINICAL_HISTORY_OBJECT
from .CCU_I20_CLINICAL_HISTORY_OBSERVATION import CCU_I20_CLINICAL_HISTORY_OBSERVATION

_CCU_I20_CLINICAL_HISTORY_OBJECT = CCU_I20_CLINICAL_HISTORY_OBJECT
_CCU_I20_CLINICAL_HISTORY_OBSERVATION = CCU_I20_CLINICAL_HISTORY_OBSERVATION


class CCU_I20_CLINICAL_HISTORY_DETAIL(HL7Model):
    """HL7 v2 CCU_I20.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCU_I20_CLINICAL_HISTORY_OBJECT): required
        CLINICAL_HISTORY_OBSERVATION (Optional[List[CCU_I20_CLINICAL_HISTORY_OBSERVATION]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCU_I20_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    CLINICAL_HISTORY_OBSERVATION: Optional[List[_CCU_I20_CLINICAL_HISTORY_OBSERVATION]] = Field(
        default=None,
        title="CLINICAL_HISTORY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
