"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EVN
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.HD import HD
from ..datatypes.XCN import XCN


class EVN(HL7Model):
    """HL7 v2 EVN segment.

    Attributes
    ----------
    evn_2 : str
        EVN.2 (req) - Recorded Date/Time (DTM)

    evn_3 : str | None
        EVN.3 (opt) - Date/Time Planned Event (DTM)

    evn_4 : CWE | None
        EVN.4 (opt) - Event Reason Code (CWE)

    evn_5 : list[XCN] | None
        EVN.5 (opt, rep) - Operator ID (XCN)

    evn_6 : str | None
        EVN.6 (opt) - Event Occurred (DTM)

    evn_7 : HD | None
        EVN.7 (opt) - Event Facility (HD)
    """

    evn_2: str = Field(
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

    evn_3: Optional[str] = Field(
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

    evn_4: Optional[CWE] = Field(
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

    evn_6: Optional[str] = Field(
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

    evn_7: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_7",
            "event_facility",
            "EVN.7",
        ),
        serialization_alias="EVN.7",
        title="Event Facility",
        description="Item #1534",
    )

    @field_validator("evn_2", "evn_3", "evn_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
