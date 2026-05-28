"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: TQ1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.RPT import RPT
from ..datatypes.TX import TX


class TQ1(BaseModel):
    """HL7 v2 TQ1 segment."""

    tq1_1: str | None = Field(
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

    tq1_2: CQ | None = Field(
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

    tq1_3: list[RPT] | None = Field(
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

    tq1_4: list[str] | None = Field(
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

    tq1_5: list[CQ] | None = Field(
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

    tq1_6: CQ | None = Field(
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

    tq1_7: str | None = Field(
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

    tq1_8: str | None = Field(
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

    tq1_9: list[CWE] | None = Field(
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

    tq1_10: TX | None = Field(
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

    tq1_11: TX | None = Field(
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

    tq1_12: str | None = Field(
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

    tq1_13: CQ | None = Field(
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

    tq1_14: str | None = Field(
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

    model_config = {"populate_by_name": True}
