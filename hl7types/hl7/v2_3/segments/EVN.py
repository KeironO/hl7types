"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: EVN
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CN import CN
from ..datatypes.TS import TS


class EVN(HL7Model):
    """Event type (S3.3.1).

    Attributes
    ----------
    evn_1 : str
        EVN.1 - Event Type Code (ID) R S3.3.1.1 | 0003 - Event Type

    evn_2 : TS | None
        EVN.2 - Recorded Date/Time (TS) NA S3.3.1.2

    evn_3 : TS | None
        EVN.3 - Date/Time Planned Event (TS) NA S3.3.1.3

    evn_4 : str | None
        EVN.4 - Event Reason Code (ID) O S3.3.1.4 | 0062 - Event Reason

    evn_5 : CN | None
        EVN.5 - Operator ID (CN) O S3.3.1.5 | 0188 - Operator ID

    evn_6 : TS | None
        EVN.6 - Event occured (TS) O S3.3.1.6
    """

    evn_1: str = Field(
        validation_alias=AliasChoices(
            "evn_1",
            "event_type_code",
            "EVN.1",
        ),
        serialization_alias="EVN.1",
        title="Event Type Code",
        description="R | Item #00099 | Table 0003 - Event Type | LEN:3",
    )

    evn_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_2",
            "recorded_date_time",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="Recorded Date/Time",
        description="NA | Item #00100",
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
        description="NA | Item #00101",
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
        description="O | Item #00102 | Table 0062 - Event Reason | LEN:3",
    )

    evn_5: Optional[CN] = Field(
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
            "event_occured",
            "EVN.6",
        ),
        serialization_alias="EVN.6",
        title="Event occured",
        description="O | Item #01278",
    )

    model_config = {"populate_by_name": True}
