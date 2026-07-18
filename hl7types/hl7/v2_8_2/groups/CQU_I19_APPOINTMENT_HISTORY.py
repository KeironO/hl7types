"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.APPOINTMENT_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SCH import SCH

from .CQU_I19_RESOURCES import CQU_I19_RESOURCES

_CQU_I19_RESOURCES = CQU_I19_RESOURCES
_SCH = SCH


class CQU_I19_APPOINTMENT_HISTORY(HL7Model):
    """HL7 v2 CQU_I19.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): Scheduling Activity Information, required
        RESOURCES (Optional[List[CQU_I19_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        title="SCH",
        description="Scheduling Activity Information",
    )

    RESOURCES: Optional[List[_CQU_I19_RESOURCES]] = Field(
        default=None,
        title="RESOURCES",
    )

    model_config = ConfigDict(populate_by_name=True)
