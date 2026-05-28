"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RPT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class RPT(BaseModel):
    """HL7 v2 RPT data type."""

    rpt_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rpt_1",
            "repeat_pattern_code",
            "RPT.1",
        ),
        serialization_alias="RPT.1",
        title="Repeat Pattern Code",
    )

    rpt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_2",
            "calendar_alignment",
            "RPT.2",
        ),
        serialization_alias="RPT.2",
        title="Calendar Alignment",
    )

    rpt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_3",
            "phase_range_begin_value",
            "RPT.3",
        ),
        serialization_alias="RPT.3",
        title="Phase Range Begin Value",
    )

    rpt_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_4",
            "phase_range_end_value",
            "RPT.4",
        ),
        serialization_alias="RPT.4",
        title="Phase Range End Value",
    )

    rpt_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_5",
            "period_quantity",
            "RPT.5",
        ),
        serialization_alias="RPT.5",
        title="Period Quantity",
    )

    rpt_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_6",
            "period_units",
            "RPT.6",
        ),
        serialization_alias="RPT.6",
        title="Period Units",
    )

    rpt_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_7",
            "institution_specified_time",
            "RPT.7",
        ),
        serialization_alias="RPT.7",
        title="Institution Specified Time",
    )

    rpt_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_8",
            "event",
            "RPT.8",
        ),
        serialization_alias="RPT.8",
        title="Event",
    )

    rpt_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_9",
            "event_offset_quantity",
            "RPT.9",
        ),
        serialization_alias="RPT.9",
        title="Event Offset Quantity",
    )

    rpt_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_10",
            "event_offset_units",
            "RPT.10",
        ),
        serialization_alias="RPT.10",
        title="Event Offset Units",
    )

    rpt_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rpt_11",
            "general_timing_specification",
            "RPT.11",
        ),
        serialization_alias="RPT.11",
        title="General Timing Specification",
    )

    model_config = {"populate_by_name": True}
