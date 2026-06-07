"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCI_I22.APPOINTMENT_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SCH import SCH

from .CCI_I22_RESOURCES import CCI_I22_RESOURCES

_CCI_I22_RESOURCES = CCI_I22_RESOURCES
_SCH = SCH


class CCI_I22_APPOINTMENT_HISTORY(HL7Model):
    """HL7 v2 CCI_I22.APPOINTMENT_HISTORY group.

    Attributes:
        SCH (SCH): required
        RESOURCES (Optional[List[CCI_I22_RESOURCES]]): optional
    """

    SCH: _SCH = Field(
        title="SCH",
        description="Required",
    )

    RESOURCES: Optional[List[_CCI_I22_RESOURCES]] = Field(
        default=None,
        title="RESOURCES",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
