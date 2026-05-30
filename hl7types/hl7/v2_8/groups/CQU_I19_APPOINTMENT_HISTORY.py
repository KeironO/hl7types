"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CQU_I19.APPOINTMENT_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SCH import SCH

from .CQU_I19_RESOURCES import CQU_I19_RESOURCES

_CQU_I19_RESOURCES = CQU_I19_RESOURCES
_SCH = SCH


class CQU_I19_APPOINTMENT_HISTORY(HL7Model):
    """HL7 v2 CQU_I19.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): required
        RESOURCES (Optional[List[CQU_I19_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        default=...,
        title="SCH",
        description="Required",
    )

    RESOURCES: Optional[List[_CQU_I19_RESOURCES]] = Field(
        default=None,
        title="RESOURCES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
