"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RPT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CWE import CWE


class RPT(HL7Model):
    """HL7 v2 RPT data type.

    Attributes
    ----------
    rpt_1 : CWE | None
        RPT.1 (opt) - Repeat Pattern Code (CWE)

    rpt_2 : str | None
        RPT.2 (opt) - Calendar Alignment (ID)

    rpt_3 : str | None
        RPT.3 (opt) - Phase Range Begin Value (NM)

    rpt_4 : str | None
        RPT.4 (opt) - Phase Range End Value (NM)

    rpt_5 : str | None
        RPT.5 (opt) - Period Quantity (NM)

    rpt_6 : str | None
        RPT.6 (opt) - Period Units (IS)

    rpt_7 : str | None
        RPT.7 (opt) - Institution Specified Time (ID)

    rpt_8 : str | None
        RPT.8 (opt) - Event (ID)

    rpt_9 : str | None
        RPT.9 (opt) - Event Offset Quantity (NM)

    rpt_10 : str | None
        RPT.10 (opt) - Event Offset Units (IS)

    rpt_11 : str | None
        RPT.11 (opt) - General Timing Specification (GTS)
    """

    rpt_1: Optional[CWE] = Field(
        default=None,
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

    rpt_6: Optional[str] = Field(
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

    rpt_10: Optional[str] = Field(
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
