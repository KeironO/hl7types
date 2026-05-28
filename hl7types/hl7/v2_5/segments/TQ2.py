"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: TQ2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.EI import EI


class TQ2(BaseModel):
    """HL7 v2 TQ2 segment."""

    tq2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_1",
            "set_id_tq2",
            "TQ2.1",
        ),
        serialization_alias="TQ2.1",
        title="Set ID - TQ2",
        description="Item #1648",
    )

    tq2_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_2",
            "sequence_results_flag",
            "TQ2.2",
        ),
        serialization_alias="TQ2.2",
        title="Sequence/Results Flag",
        description="Item #1649 | Table HL70503",
    )

    tq2_3: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_3",
            "related_placer_number",
            "TQ2.3",
        ),
        serialization_alias="TQ2.3",
        title="Related Placer Number",
        description="Item #1650",
    )

    tq2_4: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_4",
            "related_filler_number",
            "TQ2.4",
        ),
        serialization_alias="TQ2.4",
        title="Related Filler Number",
        description="Item #1651",
    )

    tq2_5: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_5",
            "related_placer_group_number",
            "TQ2.5",
        ),
        serialization_alias="TQ2.5",
        title="Related Placer Group Number",
        description="Item #1652",
    )

    tq2_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_6",
            "sequence_condition_code",
            "TQ2.6",
        ),
        serialization_alias="TQ2.6",
        title="Sequence Condition Code",
        description="Item #1653 | Table HL70504",
    )

    tq2_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_7",
            "cyclic_entry_exit_indicator",
            "TQ2.7",
        ),
        serialization_alias="TQ2.7",
        title="Cyclic Entry/Exit Indicator",
        description="Item #1654 | Table HL70505",
    )

    tq2_8: CQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_8",
            "sequence_condition_time_interval",
            "TQ2.8",
        ),
        serialization_alias="TQ2.8",
        title="Sequence Condition Time Interval",
        description="Item #1655",
    )

    tq2_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_9",
            "cyclic_group_maximum_number_of_repeats",
            "TQ2.9",
        ),
        serialization_alias="TQ2.9",
        title="Cyclic Group Maximum Number of Repeats",
        description="Item #1656",
    )

    tq2_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_10",
            "special_service_request_relationship",
            "TQ2.10",
        ),
        serialization_alias="TQ2.10",
        title="Special Service Request Relationship",
        description="Item #1657 | Table HL70506",
    )

    model_config = {"populate_by_name": True}
