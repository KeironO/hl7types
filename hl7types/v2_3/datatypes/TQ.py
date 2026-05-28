"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: TQ
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CQ import CQ
from .TS import TS
from .TX import TX


class TQ(BaseModel):
    """HL7 v2 TQ data type."""

    tq_1: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_1",
            "quantity",
            "TQ.1",
        ),
        serialization_alias="TQ.1",
        title="quantity",
    )

    tq_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_2",
            "interval",
            "TQ.2",
        ),
        serialization_alias="TQ.2",
        title="interval",
    )

    tq_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_3",
            "duration",
            "TQ.3",
        ),
        serialization_alias="TQ.3",
        title="duration",
    )

    tq_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_4",
            "start_date_time",
            "TQ.4",
        ),
        serialization_alias="TQ.4",
        title="start date/time",
    )

    tq_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_5",
            "end_date_time",
            "TQ.5",
        ),
        serialization_alias="TQ.5",
        title="end date/time",
    )

    tq_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_6",
            "priority",
            "TQ.6",
        ),
        serialization_alias="TQ.6",
        title="priority",
    )

    tq_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_7",
            "condition",
            "TQ.7",
        ),
        serialization_alias="TQ.7",
        title="condition",
    )

    tq_8: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_8",
            "text_tx",
            "TQ.8",
        ),
        serialization_alias="TQ.8",
        title="text (TX)",
    )

    tq_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_9",
            "conjunction",
            "TQ.9",
        ),
        serialization_alias="TQ.9",
        title="conjunction",
    )

    tq_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_10",
            "order_sequencing",
            "TQ.10",
        ),
        serialization_alias="TQ.10",
        title="order sequencing",
    )

    model_config = {"populate_by_name": True}
