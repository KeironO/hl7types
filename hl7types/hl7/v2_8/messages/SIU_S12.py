"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SIU_S12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SCH import SCH
from ..segments.TQ1 import TQ1

from ..groups.SIU_S12_PATIENT import SIU_S12_PATIENT
from ..groups.SIU_S12_RESOURCES import SIU_S12_RESOURCES

_MSH = MSH
_NTE = NTE
_SCH = SCH
_SIU_S12_PATIENT = SIU_S12_PATIENT
_SIU_S12_RESOURCES = SIU_S12_RESOURCES
_TQ1 = TQ1


class SIU_S12(HL7Model):
    """SIU/ACK - Notification of new appointment booking (S10.4).

    Attributes:
        MSH (MSH): Message Header, required
        SCH (SCH): Scheduling Activity Information, required
        TQ1 (Optional[List[TQ1]]): Timing/Quantity, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SCH: _SCH = Field(
        title="SCH",
        description="Scheduling Activity Information",
    )

    TQ1: Optional[List[_TQ1]] = Field(
        default=None,
        title="TQ1",
        description="Timing/Quantity",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[List[_SIU_S12_PATIENT]] = Field(
        default=None,
        title="PATIENT",
    )

    RESOURCES: List[_SIU_S12_RESOURCES] = Field(
        min_length=1,
        title="RESOURCES",
    )

    model_config = ConfigDict(populate_by_name=True)
