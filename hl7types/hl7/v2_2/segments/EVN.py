"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: EVN
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class EVN(HL7Model):
    """EVENT TYPE (S3.3.1).

    Attributes
    ----------
    evn_1 : str
        EVN.1 - Event Type Code (ID) R S3.3.1.1 | 0003 - EVENT TYPE CODE

    evn_2 : TS
        EVN.2 - Date / time of event (TS) R S3.3.1.2

    evn_3 : TS | None
        EVN.3 - Date / time planned event (TS) NA S3.3.1.3

    evn_4 : str | None
        EVN.4 - Event Reason Code (ID) NA S3.3.1.4 | 0062 - EVENT REASON

    evn_5 : str | None
        EVN.5 - Operator ID (ID) NA S3.3.1.5 | 0188 - Operator ID
    """

    evn_1: str = Field(
        validation_alias=AliasChoices(
            "evn_1",
            "event_type_code",
            "EVN.1",
        ),
        serialization_alias="EVN.1",
        title="Event Type Code",
        description="R | Item #00099 | Table 0003 - EVENT TYPE CODE | LEN:3",
    )

    evn_2: TS = Field(
        validation_alias=AliasChoices(
            "evn_2",
            "date_time_of_event",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="Date / time of event",
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
        title="Date / time planned event",
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
        description="NA | Item #00102 | Table 0062 - EVENT REASON | LEN:3",
    )

    evn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_5",
            "operator_id",
            "EVN.5",
        ),
        serialization_alias="EVN.5",
        title="Operator ID",
        description="NA | Item #00103 | Table 0188 - Operator ID | LEN:5",
    )

    model_config = ConfigDict(populate_by_name=True)
