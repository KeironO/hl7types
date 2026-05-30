"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: EVN
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class EVN(HL7Model):
    """HL7 v2 EVN segment.

    Attributes
    ----------
    evn_1 : str | None
        EVN.1 (opt) - Event Type Code (ID)

    evn_2 : TS
        EVN.2 (req) - Recorded Date/Time (TS)

    evn_3 : TS | None
        EVN.3 (opt) - Date/Time Planned Event (TS)

    evn_4 : str | None
        EVN.4 (opt) - Event Reason Code (IS)

    evn_5 : list[XCN] | None
        EVN.5 (opt, rep) - Operator ID (XCN)

    evn_6 : TS | None
        EVN.6 (opt) - Event Occurred (TS)
    """

    evn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_1",
            "event_type_code",
            "EVN.1",
        ),
        serialization_alias="EVN.1",
        title="Event Type Code",
        description="Item #99 | Table HL70003",
    )

    evn_2: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "evn_2",
            "recorded_date_time",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="Recorded Date/Time",
        description="Item #100",
    )

    evn_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_3",
            "date_time_planned_event",
            "EVN.3",
        ),
        serialization_alias="EVN.3",
        title="Date/Time Planned Event",
        description="Item #101",
    )

    evn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_4",
            "event_reason_code",
            "EVN.4",
        ),
        serialization_alias="EVN.4",
        title="Event Reason Code",
        description="Item #102 | Table HL70062",
    )

    evn_5: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_5",
            "operator_id",
            "EVN.5",
        ),
        serialization_alias="EVN.5",
        title="Operator ID",
        description="Item #103 | Table HL70188",
    )

    evn_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_6",
            "event_occurred",
            "EVN.6",
        ),
        serialization_alias="EVN.6",
        title="Event Occurred",
        description="Item #1278",
    )

    model_config = {"populate_by_name": True}
