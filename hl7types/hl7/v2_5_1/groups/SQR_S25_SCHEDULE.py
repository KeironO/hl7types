"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SQR_S25.SCHEDULE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.SCH import SCH
from ..segments.TQ1 import TQ1
from .SQR_S25_PATIENT import SQR_S25_PATIENT
from .SQR_S25_RESOURCES import SQR_S25_RESOURCES

_NTE = NTE
_SCH = SCH
_SQR_S25_PATIENT = SQR_S25_PATIENT
_SQR_S25_RESOURCES = SQR_S25_RESOURCES
_TQ1 = TQ1


class SQR_S25_SCHEDULE(BaseModel):
    """HL7 v2 SQR_S25.SCHEDULE group.

    Attributes:
        SCH (SCH): required
        TQ1 (Optional[List[TQ1]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[SQR_S25_PATIENT]): optional
        RESOURCES (List[SQR_S25_RESOURCES]): required
    """

    SCH: _SCH = Field(
        default=...,
        title="SCH",
        description="Required",
    )

    TQ1: list[_TQ1] | None = Field(
        default=None,
        title="TQ1",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _SQR_S25_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    RESOURCES: list[_SQR_S25_RESOURCES] = Field(
        default=...,
        title="RESOURCES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
