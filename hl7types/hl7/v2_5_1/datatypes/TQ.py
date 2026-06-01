"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: TQ
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CE import CE
from .CQ import CQ
from .OSD import OSD
from .RI import RI
from .TS import TS
from .TX import TX


class TQ(HL7Model):
    """HL7 v2 TQ data type.

    Attributes
    ----------
    tq_1 : CQ | None
        TQ.1 (opt) - Quantity (CQ)

    tq_2 : RI | None
        TQ.2 (opt) - Interval (RI)

    tq_3 : str | None
        TQ.3 (opt) - Duration (ST)

    tq_4 : TS | None
        TQ.4 (opt) - Start Date/Time (TS)

    tq_5 : TS | None
        TQ.5 (opt) - End Date/Time (TS)

    tq_6 : str | None
        TQ.6 (opt) - Priority (ST)

    tq_7 : str | None
        TQ.7 (opt) - Condition (ST)

    tq_8 : TX | None
        TQ.8 (opt) - Text (TX)

    tq_9 : str | None
        TQ.9 (opt) - Conjunction (ID)

    tq_10 : OSD | None
        TQ.10 (opt) - Order Sequencing (OSD)

    tq_11 : CE | None
        TQ.11 (opt) - Occurrence Duration (CE)

    tq_12 : str | None
        TQ.12 (opt) - Total Occurrences (NM)
    """

    tq_1: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_1",
            "quantity",
            "TQ.1",
        ),
        serialization_alias="TQ.1",
        title="Quantity",
    )

    tq_2: Optional[RI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_2",
            "interval",
            "TQ.2",
        ),
        serialization_alias="TQ.2",
        title="Interval",
    )

    tq_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_3",
            "duration",
            "TQ.3",
        ),
        serialization_alias="TQ.3",
        title="Duration",
    )

    tq_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_4",
            "start_date_time",
            "TQ.4",
        ),
        serialization_alias="TQ.4",
        title="Start Date/Time",
    )

    tq_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_5",
            "end_date_time",
            "TQ.5",
        ),
        serialization_alias="TQ.5",
        title="End Date/Time",
    )

    tq_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_6",
            "priority",
            "TQ.6",
        ),
        serialization_alias="TQ.6",
        title="Priority",
    )

    tq_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_7",
            "condition",
            "TQ.7",
        ),
        serialization_alias="TQ.7",
        title="Condition",
    )

    tq_8: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_8",
            "text",
            "TQ.8",
        ),
        serialization_alias="TQ.8",
        title="Text",
    )

    tq_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_9",
            "conjunction",
            "TQ.9",
        ),
        serialization_alias="TQ.9",
        title="Conjunction",
    )

    tq_10: Optional[OSD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_10",
            "order_sequencing",
            "TQ.10",
        ),
        serialization_alias="TQ.10",
        title="Order Sequencing",
    )

    tq_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_11",
            "occurrence_duration",
            "TQ.11",
        ),
        serialization_alias="TQ.11",
        title="Occurrence Duration",
    )

    tq_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_12",
            "total_occurrences",
            "TQ.12",
        ),
        serialization_alias="TQ.12",
        title="Total Occurrences",
    )

    @field_validator("tq_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
