"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EVN
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.HD import HD
from ..datatypes.XCN import XCN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class EVN(HL7Model):
    """Event Type (S3.4.1).

    Attributes
    ----------
    evn_2 : str
        EVN.2 - Recorded Date/Time (DTM) R S3.4.1.2

    evn_3 : str | None
        EVN.3 - Date/Time Planned Event (DTM) O S3.4.1.3

    evn_4 : CWE | None
        EVN.4 - Event Reason Code (CWE) O S3.4.1.4 | 0062 - Event Reason

    evn_5 : list[XCN] | None
        EVN.5 - Operator ID (XCN) O rep S3.4.1.5 | 0188 - Operator ID

    evn_6 : str | None
        EVN.6 - Event Occurred (DTM) O S3.4.1.6

    evn_7 : HD | None
        EVN.7 - Event Facility (HD) O S3.4.1.7
    """

    evn_2: str = Field(
        validation_alias=AliasChoices(
            "evn_2",
            "recorded_date_time",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="Recorded Date/Time",
        description="R | Item #00100",
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
        description="O | Item #00101",
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
        description="O | Item #00102 | Table 0062 - Event Reason",
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

    evn_6: Optional[str] = Field(
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

    @field_validator("evn_2", "evn_3", "evn_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
