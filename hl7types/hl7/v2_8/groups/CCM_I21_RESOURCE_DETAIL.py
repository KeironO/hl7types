"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .CCM_I21_RESOURCE_OBJECT import CCM_I21_RESOURCE_OBJECT
from .CCM_I21_RESOURCE_OBSERVATION import CCM_I21_RESOURCE_OBSERVATION

_CCM_I21_RESOURCE_OBJECT = CCM_I21_RESOURCE_OBJECT
_CCM_I21_RESOURCE_OBSERVATION = CCM_I21_RESOURCE_OBSERVATION


class CCM_I21_RESOURCE_DETAIL(HL7Model):
    """HL7 v2 CCM_I21.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCM_I21_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CCM_I21_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CCM_I21_RESOURCE_OBJECT = Field(
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: Optional[List[_CCM_I21_RESOURCE_OBSERVATION]] = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
