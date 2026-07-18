"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SRR_S01.SCHEDULE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.SCH import SCH
from ..segments.TQ1 import TQ1

from .SRR_S01_PATIENT import SRR_S01_PATIENT
from .SRR_S01_RESOURCES import SRR_S01_RESOURCES

_NTE = NTE
_SCH = SCH
_SRR_S01_PATIENT = SRR_S01_PATIENT
_SRR_S01_RESOURCES = SRR_S01_RESOURCES
_TQ1 = TQ1


class SRR_S01_SCHEDULE(HL7Model):
    """HL7 v2 SRR_S01.SCHEDULE group.

    Attributes:
        SCH (SCH): Scheduling Activity Information, required
        TQ1 (Optional[List[TQ1]]): Timing/Quantity, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[List[SRR_S01_PATIENT]]): optional
        RESOURCES (List[SRR_S01_RESOURCES]): required
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

    PATIENT: Optional[List[_SRR_S01_PATIENT]] = Field(
        default=None,
        title="PATIENT",
    )

    RESOURCES: List[_SRR_S01_RESOURCES] = Field(
        min_length=1,
        title="RESOURCES",
    )

    model_config = ConfigDict(populate_by_name=True)
