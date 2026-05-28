"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.APPOINTMENT_HISTORY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SCH import SCH
from .CCM_I21_RESOURCES import CCM_I21_RESOURCES

_CCM_I21_RESOURCES = CCM_I21_RESOURCES
_SCH = SCH


class CCM_I21_APPOINTMENT_HISTORY(BaseModel):
    """HL7 v2 CCM_I21.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): required
        RESOURCES (Optional[List[CCM_I21_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        default=...,
        title="SCH",
        description="Required",
    )

    RESOURCES: list[_CCM_I21_RESOURCES] | None = Field(
        default=None,
        title="RESOURCES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
