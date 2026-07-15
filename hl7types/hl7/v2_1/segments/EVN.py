"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: EVN
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class EVN(HL7Model):
    """EVENT TYPE (S3.3.1).

    Attributes
    ----------
    evn_1 : str
        EVN.1 - EVENT TYPE CODE (ID) R S3-11 | 0003 - EVENT TYPE CODE

    evn_2 : str
        EVN.2 - DATE/TIME OF EVENT (TS) R

    evn_3 : str | None
        EVN.3 - DATE/TIME PLANNED EVENT (TS) O

    evn_4 : str | None
        EVN.4 - EVENT REASON CODE (ID) O | 0062 - EVENT REASON
    """

    evn_1: str = Field(
        validation_alias=AliasChoices(
            "evn_1",
            "event_type_code",
            "EVN.1",
        ),
        serialization_alias="EVN.1",
        title="EVENT TYPE CODE",
        description="R | Item #00029 | Table 0003 - EVENT TYPE CODE | LEN:3",
    )

    evn_2: str = Field(
        validation_alias=AliasChoices(
            "evn_2",
            "date_time_of_event",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="DATE/TIME OF EVENT",
        description="R | Item #00030 | LEN:19",
    )

    evn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_3",
            "date_time_planned_event",
            "EVN.3",
        ),
        serialization_alias="EVN.3",
        title="DATE/TIME PLANNED EVENT",
        description="O | Item #00032 | LEN:19",
    )

    evn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_4",
            "event_reason_code",
            "EVN.4",
        ),
        serialization_alias="EVN.4",
        title="EVENT REASON CODE",
        description="O | Item #00369 | Table 0062 - EVENT REASON | LEN:3",
    )

    model_config = {"populate_by_name": True}
