"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQR_S25.SCHEDULE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class SQR_S25_SCHEDULE(HL7Model):
    """HL7 v2 SQR_S25.SCHEDULE group.

    Attributes:
        SCH (SCH): Scheduling Activity Information, required
        TQ1 (Optional[List[TQ1]]): Timing/Quantity, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[SQR_S25_PATIENT]): optional
        RESOURCES (List[SQR_S25_RESOURCES]): required
    """

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

    PATIENT: Optional[_SQR_S25_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    RESOURCES: List[_SQR_S25_RESOURCES] = Field(
        min_length=1,
        title="RESOURCES",
    )

    model_config = ConfigDict(populate_by_name=True)
