"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SIU_S12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SCH import SCH

from ..groups.SIU_S12_PATIENT import SIU_S12_PATIENT
from ..groups.SIU_S12_RESOURCES import SIU_S12_RESOURCES

_MSH = MSH
_NTE = NTE
_SCH = SCH
_SIU_S12_PATIENT = SIU_S12_PATIENT
_SIU_S12_RESOURCES = SIU_S12_RESOURCES


class SIU_S12(HL7Model):
    """SIU/ACK - Notification of new appointment booking.

    Attributes:
        MSH (MSH): Message header segment, required
        SCH (SCH): Schedule Activity Information, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    SCH: _SCH = Field(
        title="SCH",
        description="Schedule Activity Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    PATIENT: Optional[List[_SIU_S12_PATIENT]] = Field(
        default=None,
        title="PATIENT",
    )

    RESOURCES: List[_SIU_S12_RESOURCES] = Field(
        min_length=1,
        title="RESOURCES",
    )

    model_config = {"populate_by_name": True}
