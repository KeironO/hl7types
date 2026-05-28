"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SIU_S12
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SIU_S12_PATIENT import SIU_S12_PATIENT
from ..groups.SIU_S12_RESOURCES import SIU_S12_RESOURCES
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SCH import SCH
from ..segments.TQ1 import TQ1

_MSH = MSH
_NTE = NTE
_SCH = SCH
_SIU_S12_PATIENT = SIU_S12_PATIENT
_SIU_S12_RESOURCES = SIU_S12_RESOURCES
_TQ1 = TQ1


class SIU_S12(BaseModel):
    """HL7 v2 SIU_S12 message.

    Attributes:
        MSH (MSH): required
        SCH (SCH): required
        TQ1 (Optional[List[TQ1]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

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

    PATIENT: list[_SIU_S12_PATIENT] | None = Field(
        default=None,
        title="PATIENT",
        description="Optional, repeating",
    )

    RESOURCES: list[_SIU_S12_RESOURCES] = Field(
        default=...,
        title="RESOURCES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
