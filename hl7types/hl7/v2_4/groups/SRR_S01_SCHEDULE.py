"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SRR_S01.SCHEDULE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.SCH import SCH

from .SRR_S01_PATIENT import SRR_S01_PATIENT
from .SRR_S01_RESOURCES import SRR_S01_RESOURCES

_NTE = NTE
_SCH = SCH
_SRR_S01_PATIENT = SRR_S01_PATIENT
_SRR_S01_RESOURCES = SRR_S01_RESOURCES


class SRR_S01_SCHEDULE(HL7Model):
    """HL7 v2 SRR_S01.SCHEDULE group.

    Attributes:
        SCH (SCH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[List[SRR_S01_PATIENT]]): optional
        RESOURCES (List[SRR_S01_RESOURCES]): required
    """

    SCH: _SCH = Field(
        title="SCH",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[List[_SRR_S01_PATIENT]] = Field(
        default=None,
        title="PATIENT",
        description="Optional, repeating",
    )

    RESOURCES: List[_SRR_S01_RESOURCES] = Field(
        min_length=1,
        title="RESOURCES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
