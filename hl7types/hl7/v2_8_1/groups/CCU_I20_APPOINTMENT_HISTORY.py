"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.APPOINTMENT_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SCH import SCH

from .CCU_I20_RESOURCES import CCU_I20_RESOURCES

_CCU_I20_RESOURCES = CCU_I20_RESOURCES
_SCH = SCH


class CCU_I20_APPOINTMENT_HISTORY(HL7Model):
    """HL7 v2 CCU_I20.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): required
        RESOURCES (Optional[List[CCU_I20_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        default=...,
        title="SCH",
        description="Required",
    )

    RESOURCES: Optional[List[_CCU_I20_RESOURCES]] = Field(
        default=None,
        title="RESOURCES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
