"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CTI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI


class CTI(HL7Model):
    """HL7 v2 CTI segment.

    Attributes
    ----------
    cti_1 : EI
        CTI.1 (req) - Sponsor Study ID (EI)

    cti_2 : CE | None
        CTI.2 (opt) - Study Phase Identifier (CE)

    cti_3 : CE | None
        CTI.3 (opt) - Study Scheduled Time Point (CE)
    """

    cti_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "cti_1",
            "sponsor_study_id",
            "CTI.1",
        ),
        serialization_alias="CTI.1",
        title="Sponsor Study ID",
        description="Item #1011",
    )

    cti_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cti_2",
            "study_phase_identifier",
            "CTI.2",
        ),
        serialization_alias="CTI.2",
        title="Study Phase Identifier",
        description="Item #1022",
    )

    cti_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cti_3",
            "study_scheduled_time_point",
            "CTI.3",
        ),
        serialization_alias="CTI.3",
        title="Study Scheduled Time Point",
        description="Item #1055",
    )

    model_config = {"populate_by_name": True}
