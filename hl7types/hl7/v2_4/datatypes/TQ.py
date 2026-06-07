"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: TQ
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .CE import CE
from .CQ import CQ
from .OSD import OSD
from .RI import RI
from .TS import TS


class TQ(HL7Model):
    """HL7 v2 TQ data type.

    Attributes
    ----------
    tq_1 : CQ | None
        TQ.1 (opt) - quantity (CQ)

    tq_2 : RI | None
        TQ.2 (opt) - interval (RI)

    tq_3 : str | None
        TQ.3 (opt) - duration (ST)

    tq_4 : TS | None
        TQ.4 (opt) - start date/time (TS)

    tq_5 : TS | None
        TQ.5 (opt) - end date/time (TS)

    tq_6 : str | None
        TQ.6 (opt) - priority (ST)

    tq_7 : str | None
        TQ.7 (opt) - condition (ST)

    tq_8 : str | None
        TQ.8 (opt) - text (TX) (TX)

    tq_9 : str | None
        TQ.9 (opt) - conjunction component (ID)

    tq_10 : OSD | None
        TQ.10 (opt) - order sequencing (OSD)

    tq_11 : CE | None
        TQ.11 (opt) - occurrence duration (CE)

    tq_12 : str | None
        TQ.12 (opt) - total occurences (NM)
    """

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

    tq_2: Optional[RI] = Field(
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

    tq_8: Optional[str] = Field(
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
            "conjunction_component",
            "TQ.9",
        ),
        serialization_alias="TQ.9",
        title="conjunction component",
    )

    tq_10: Optional[OSD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_10",
            "order_sequencing",
            "TQ.10",
        ),
        serialization_alias="TQ.10",
        title="order sequencing",
    )

    tq_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_11",
            "occurrence_duration",
            "TQ.11",
        ),
        serialization_alias="TQ.11",
        title="occurrence duration",
    )

    tq_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq_12",
            "total_occurences",
            "TQ.12",
        ),
        serialization_alias="TQ.12",
        title="total occurences",
    )

    @field_validator("tq_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
