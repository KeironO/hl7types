"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EVN
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.HD import HD
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class EVN(HL7Model):
    """Event Type (S3.4.1).

    Attributes
    ----------
    evn_1 : str | None
        EVN.1 - Event Type Code (ID) O S3.4.1.1 | 0003 - Event type

    evn_2 : TS
        EVN.2 - Recorded Date/Time (TS) R S3.4.1.2

    evn_3 : TS | None
        EVN.3 - Date/Time Planned Event (TS) O S3.4.1.3

    evn_4 : str | None
        EVN.4 - Event Reason Code (IS) O S3.4.1.4 | 0062 - Event reason

    evn_5 : list[XCN] | None
        EVN.5 - Operator ID (XCN) O rep S3.4.1.5 | 0188 - Operator ID

    evn_6 : TS | None
        EVN.6 - Event Occurred (TS) O S3.4.1.6

    evn_7 : HD | None
        EVN.7 - Event Facility (HD) O S3.4.1.7
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
        description="O | Item #00099 | Table 0003 - Event type | LEN:3",
    )

    evn_2: TS = Field(
        validation_alias=AliasChoices(
            "evn_2",
            "recorded_date_time",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="Recorded Date/Time",
        description="R | Item #00100",
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
        description="O | Item #00101",
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
        description="O | Item #00102 | Table 0062 - Event reason | LEN:3",
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
        description="O | Item #00103 | Table 0188 - Operator ID",
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
        description="O | Item #01278",
    )

    evn_7: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_7",
            "event_facility",
            "EVN.7",
        ),
        serialization_alias="EVN.7",
        title="Event Facility",
        description="O | Item #01534",
    )

    model_config = {"populate_by_name": True}
