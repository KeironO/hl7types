"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: TS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class TS(HL7Model):
    """HL7 v2 TS data type.

    Attributes
    ----------
    ts_1 : str | None
        TS.1 (opt) - time of an event (ST)

    ts_2 : str | None
        TS.2 (opt) - degree of precision (ST)
    """

    ts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_1",
            "time_of_an_event",
            "TS.1",
        ),
        serialization_alias="TS.1",
        title="time of an event",
    )

    ts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_2",
            "degree_of_precision",
            "TS.2",
        ),
        serialization_alias="TS.2",
        title="degree of precision",
    )

    model_config = {"populate_by_name": True}
