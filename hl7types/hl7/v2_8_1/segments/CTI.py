"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CTI
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class CTI(BaseModel):
    """HL7 v2 CTI segment."""

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

    cti_2: CWE | None = Field(
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

    cti_3: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cti_3",
            "study_scheduled_time_point",
            "CTI.3",
        ),
        serialization_alias="CTI.3",
        title="Study Scheduled Time Point",
        description="Item #1055 | Table HL79999",
    )

    model_config = {"populate_by_name": True}
