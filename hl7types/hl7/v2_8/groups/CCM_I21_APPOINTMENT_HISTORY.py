"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.APPOINTMENT_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SCH import SCH

from .CCM_I21_RESOURCES import CCM_I21_RESOURCES

_CCM_I21_RESOURCES = CCM_I21_RESOURCES
_SCH = SCH


class CCM_I21_APPOINTMENT_HISTORY(HL7Model):
    """HL7 v2 CCM_I21.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): required
        RESOURCES (Optional[List[CCM_I21_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        title="SCH",
        description="Required",
    )

    RESOURCES: Optional[List[_CCM_I21_RESOURCES]] = Field(
        default=None,
        title="RESOURCES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
