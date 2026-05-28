"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: TQ
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CQ import CQ
from .CWE import CWE
from .OSD import OSD
from .RI import RI
from .TX import TX


class TQ(BaseModel):
    """HL7 v2 TQ data type."""

    tq_1: CQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_1",
            "quantity",
            "TQ.1",
        ),
        serialization_alias="TQ.1",
        title="Quantity",
    )

    tq_2: RI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_2",
            "interval",
            "TQ.2",
        ),
        serialization_alias="TQ.2",
        title="Interval",
    )

    tq_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_3",
            "duration",
            "TQ.3",
        ),
        serialization_alias="TQ.3",
        title="Duration",
    )

    tq_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_4",
            "start_date_time",
            "TQ.4",
        ),
        serialization_alias="TQ.4",
        title="Start Date/Time",
    )

    tq_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_5",
            "end_date_time",
            "TQ.5",
        ),
        serialization_alias="TQ.5",
        title="End Date/Time",
    )

    tq_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_6",
            "priority",
            "TQ.6",
        ),
        serialization_alias="TQ.6",
        title="Priority",
    )

    tq_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_7",
            "condition",
            "TQ.7",
        ),
        serialization_alias="TQ.7",
        title="Condition",
    )

    tq_8: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_8",
            "text",
            "TQ.8",
        ),
        serialization_alias="TQ.8",
        title="Text",
    )

    tq_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_9",
            "conjunction",
            "TQ.9",
        ),
        serialization_alias="TQ.9",
        title="Conjunction",
    )

    tq_10: OSD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_10",
            "order_sequencing",
            "TQ.10",
        ),
        serialization_alias="TQ.10",
        title="Order Sequencing",
    )

    tq_11: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_11",
            "occurrence_duration",
            "TQ.11",
        ),
        serialization_alias="TQ.11",
        title="Occurrence Duration",
    )

    tq_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_12",
            "total_occurrences",
            "TQ.12",
        ),
        serialization_alias="TQ.12",
        title="Total Occurrences",
    )

    model_config = {"populate_by_name": True}
