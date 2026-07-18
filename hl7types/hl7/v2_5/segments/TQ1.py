"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: TQ1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.RPT import RPT
from ..datatypes.TS import TS

_RE_SI = re.compile(r'\d*')
_RE_TM = re.compile(r'([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class TQ1(HL7Model):
    """Timing/Quantity (S4.5.4).

    Attributes
    ----------
    tq1_1 : str | None
        TQ1.1 - Set ID - TQ1 (SI) O S4.5.4.1

    tq1_2 : CQ | None
        TQ1.2 - Quantity (CQ) O S4.5.4.2

    tq1_3 : list[RPT] | None
        TQ1.3 - Repeat Pattern (RPT) O rep S4.5.4.3 | 0335 - Repeat pattern

    tq1_4 : list[str] | None
        TQ1.4 - Explicit Time (TM) O rep S4.5.4.4

    tq1_5 : list[CQ] | None
        TQ1.5 - Relative Time and Units (CQ) O rep S4.5.4.5

    tq1_6 : CQ | None
        TQ1.6 - Service Duration (CQ) O S4.5.4.6

    tq1_7 : TS | None
        TQ1.7 - Start date/time (TS) O S4.5.4.7

    tq1_8 : TS | None
        TQ1.8 - End date/time (TS) O S4.5.4.8

    tq1_9 : list[CWE] | None
        TQ1.9 - Priority (CWE) O rep S4.5.4.9 | 0485 - Extended Priority Codes

    tq1_10 : str | None
        TQ1.10 - Condition text (TX) O S4.5.4.10

    tq1_11 : str | None
        TQ1.11 - Text instruction (TX) O S4.5.4.11

    tq1_12 : str | None
        TQ1.12 - Conjunction (ID) C S4.5.4.12 | 0427 - Risk Management Incident Code

    tq1_13 : CQ | None
        TQ1.13 - Occurrence duration (CQ) O S4.5.4.13

    tq1_14 : str | None
        TQ1.14 - Total occurrence's (NM) O S4.5.4.14
    """

    tq1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_1",
            "set_id_tq1",
            "TQ1.1",
        ),
        serialization_alias="TQ1.1",
        title="Set ID - TQ1",
        description="O | Item #01627 | LEN:4",
    )

    tq1_2: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_2",
            "quantity",
            "TQ1.2",
        ),
        serialization_alias="TQ1.2",
        title="Quantity",
        description="O | Item #01628",
    )

    tq1_3: Optional[List[RPT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_3",
            "repeat_pattern",
            "TQ1.3",
        ),
        serialization_alias="TQ1.3",
        title="Repeat Pattern",
        description="O | Item #01629 | Table 0335 - Repeat pattern",
    )

    tq1_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_4",
            "explicit_time",
            "TQ1.4",
        ),
        serialization_alias="TQ1.4",
        title="Explicit Time",
        description="O | Item #01630 | LEN:20",
    )

    tq1_5: Optional[List[CQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_5",
            "relative_time_and_units",
            "TQ1.5",
        ),
        serialization_alias="TQ1.5",
        title="Relative Time and Units",
        description="O | Item #01631",
    )

    tq1_6: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_6",
            "service_duration",
            "TQ1.6",
        ),
        serialization_alias="TQ1.6",
        title="Service Duration",
        description="O | Item #01632",
    )

    tq1_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_7",
            "start_date_time",
            "TQ1.7",
        ),
        serialization_alias="TQ1.7",
        title="Start date/time",
        description="O | Item #01633",
    )

    tq1_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_8",
            "end_date_time",
            "TQ1.8",
        ),
        serialization_alias="TQ1.8",
        title="End date/time",
        description="O | Item #01634",
    )

    tq1_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_9",
            "priority",
            "TQ1.9",
        ),
        serialization_alias="TQ1.9",
        title="Priority",
        description="O | Item #01635 | Table 0485 - Extended Priority Codes",
    )

    tq1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_10",
            "condition_text",
            "TQ1.10",
        ),
        serialization_alias="TQ1.10",
        title="Condition text",
        description="O | Item #01636",
    )

    tq1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_11",
            "text_instruction",
            "TQ1.11",
        ),
        serialization_alias="TQ1.11",
        title="Text instruction",
        description="O | Item #01637",
    )

    tq1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_12",
            "conjunction",
            "TQ1.12",
        ),
        serialization_alias="TQ1.12",
        title="Conjunction",
        description=(
            "C | Item #01638 | Table 0427 - Risk Management Incident Code | "
            "LEN:10"
        ),
    )

    tq1_13: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_13",
            "occurrence_duration",
            "TQ1.13",
        ),
        serialization_alias="TQ1.13",
        title="Occurrence duration",
        description="O | Item #01639",
    )

    tq1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_14",
            "total_occurrence_s",
            "TQ1.14",
        ),
        serialization_alias="TQ1.14",
        title="Total occurrence's",
        description="O | Item #01640 | LEN:10",
    )

    @field_validator("tq1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("tq1_4", mode='before')
    @classmethod
    def _validate_tm(cls, v: str) -> str:
        if not _RE_TM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 time")
        return v

    @field_validator("tq1_14", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
