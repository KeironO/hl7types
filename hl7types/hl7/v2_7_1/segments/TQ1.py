"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: TQ1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.RPT import RPT


class TQ1(HL7Model):
    """HL7 v2 TQ1 segment.

    Attributes
    ----------
    tq1_1 : str | None
        TQ1.1 (opt) - Set ID - TQ1 (SI)

    tq1_2 : CQ | None
        TQ1.2 (opt) - Quantity (CQ)

    tq1_3 : list[RPT] | None
        TQ1.3 (opt, rep) - Repeat Pattern (RPT)

    tq1_4 : list[str] | None
        TQ1.4 (opt, rep) - Explicit Time (TM)

    tq1_5 : list[CQ] | None
        TQ1.5 (opt, rep) - Relative Time and Units (CQ)

    tq1_6 : CQ | None
        TQ1.6 (opt) - Service Duration (CQ)

    tq1_7 : str | None
        TQ1.7 (opt) - Start date/time (DTM)

    tq1_8 : str | None
        TQ1.8 (opt) - End date/time (DTM)

    tq1_9 : list[CWE] | None
        TQ1.9 (opt, rep) - Priority (CWE)

    tq1_10 : str | None
        TQ1.10 (opt) - Condition text (TX)

    tq1_11 : str | None
        TQ1.11 (opt) - Text instruction (TX)

    tq1_12 : str | None
        TQ1.12 (opt) - Conjunction (ID)

    tq1_13 : CQ | None
        TQ1.13 (opt) - Occurrence duration (CQ)

    tq1_14 : str | None
        TQ1.14 (opt) - Total occurrences (NM)
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
        description="Item #1627",
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
        description="Item #1628",
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
        description="Item #1629",
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
        description="Item #1630",
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
        description="Item #1631",
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
        description="Item #1632",
    )

    tq1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_7",
            "start_date_time",
            "TQ1.7",
        ),
        serialization_alias="TQ1.7",
        title="Start date/time",
        description="Item #1633",
    )

    tq1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_8",
            "end_date_time",
            "TQ1.8",
        ),
        serialization_alias="TQ1.8",
        title="End date/time",
        description="Item #1634",
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
        description="Item #1635 | Table HL70485",
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
        description="Item #1636",
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
        description="Item #1637",
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
        description="Item #1638 | Table HL70472",
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
        description="Item #1639",
    )

    tq1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq1_14",
            "total_occurrences",
            "TQ1.14",
        ),
        serialization_alias="TQ1.14",
        title="Total occurrences",
        description="Item #1640",
    )

    @field_validator("tq1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("tq1_4", mode='before')
    @classmethod
    def _validate_tm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 time")
        return v

    @field_validator("tq1_7", "tq1_8", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("tq1_14", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
