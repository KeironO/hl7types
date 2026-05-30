"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16.APPOINTMENT_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SCH import SCH

from .CCR_I16_RESOURCES import CCR_I16_RESOURCES

_CCR_I16_RESOURCES = CCR_I16_RESOURCES
_SCH = SCH


class CCR_I16_APPOINTMENT_HISTORY(HL7Model):
    """HL7 v2 CCR_I16.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): required
        RESOURCES (Optional[List[CCR_I16_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        default=...,
        title="SCH",
        description="Required",
    )

    RESOURCES: Optional[List[_CCR_I16_RESOURCES]] = Field(
        default=None,
        title="RESOURCES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
