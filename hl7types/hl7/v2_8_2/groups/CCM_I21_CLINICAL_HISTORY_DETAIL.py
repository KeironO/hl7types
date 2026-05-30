"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCM_I21.CLINICAL_HISTORY_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .CCM_I21_CLINICAL_HISTORY_OBJECT import CCM_I21_CLINICAL_HISTORY_OBJECT
from .CCM_I21_CLINICAL_HISTORY_OBSERVATION import CCM_I21_CLINICAL_HISTORY_OBSERVATION

_CCM_I21_CLINICAL_HISTORY_OBJECT = CCM_I21_CLINICAL_HISTORY_OBJECT
_CCM_I21_CLINICAL_HISTORY_OBSERVATION = CCM_I21_CLINICAL_HISTORY_OBSERVATION


class CCM_I21_CLINICAL_HISTORY_DETAIL(HL7Model):
    """HL7 v2 CCM_I21.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCM_I21_CLINICAL_HISTORY_OBJECT): required
        CLINICAL_HISTORY_OBSERVATION (Optional[List[CCM_I21_CLINICAL_HISTORY_OBSERVATION]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCM_I21_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    CLINICAL_HISTORY_OBSERVATION: Optional[List[_CCM_I21_CLINICAL_HISTORY_OBSERVATION]] = Field(
        default=None,
        title="CLINICAL_HISTORY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
