"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: TS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class TS(HL7Model):
    """HL7 v2 TS data type.

    Attributes
    ----------
    ts_1 : str | None
        TS.1 (opt) - Time (DTM)

    ts_2 : str | None
        TS.2 (opt) - Degree of Precision (ID)
    """

    ts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_1",
            "time",
            "TS.1",
        ),
        serialization_alias="TS.1",
        title="Time",
    )

    ts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_2",
            "degree_of_precision",
            "TS.2",
        ),
        serialization_alias="TS.2",
        title="Degree of Precision",
    )

    @field_validator("ts_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
