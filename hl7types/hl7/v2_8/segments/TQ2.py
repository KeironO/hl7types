"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: TQ2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.EI import EI


class TQ2(HL7Model):
    """Timing/Quantity Relationship (S4.5.5).

    Attributes
    ----------
    tq2_1 : str | None
        TQ2.1 - Set ID - TQ2 (SI) O S4.5.5.1

    tq2_2 : str | None
        TQ2.2 - Sequence/Results Flag (ID) O S4.5.5.2 | 0503 - Sequence/Results Flag

    tq2_3 : list[EI] | None
        TQ2.3 - Related Placer Number (EI) C rep S4.5.5.3

    tq2_4 : list[EI] | None
        TQ2.4 - Related Filler Number (EI) C rep S4.5.5.4

    tq2_5 : list[EI] | None
        TQ2.5 - Related Placer Group Number (EI) C rep S4.5.5.5

    tq2_6 : str | None
        TQ2.6 - Sequence Condition Code (ID) C S4.5.5.6 | 0504 - Sequence Condition Code

    tq2_7 : str | None
        TQ2.7 - Cyclic Entry/Exit Indicator (ID) C S4.5.5.7 | 0505 - Cyclic Entry/Exit Indicator

    tq2_8 : CQ | None
        TQ2.8 - Sequence Condition Time Interval (CQ) O S4.5.5.8

    tq2_9 : str | None
        TQ2.9 - Cyclic Group Maximum Number of Repeats (NM) O S4.5.5.9

    tq2_10 : str | None
        TQ2.10 - Special Service Request Relationship (ID) C S4.5.5.10 | 0506 - Service Request Relationship
    """

    tq2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_1",
            "set_id_tq2",
            "TQ2.1",
        ),
        serialization_alias="TQ2.1",
        title="Set ID - TQ2",
        description="O | Item #01648 | LEN:4",
    )

    tq2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_2",
            "sequence_results_flag",
            "TQ2.2",
        ),
        serialization_alias="TQ2.2",
        title="Sequence/Results Flag",
        description=(
            "O | Item #01649 | Table 0503 - Sequence/Results Flag | LEN:1"
        ),
    )

    tq2_3: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_3",
            "related_placer_number",
            "TQ2.3",
        ),
        serialization_alias="TQ2.3",
        title="Related Placer Number",
        description="C | Item #01650",
    )

    tq2_4: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_4",
            "related_filler_number",
            "TQ2.4",
        ),
        serialization_alias="TQ2.4",
        title="Related Filler Number",
        description="C | Item #01651",
    )

    tq2_5: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_5",
            "related_placer_group_number",
            "TQ2.5",
        ),
        serialization_alias="TQ2.5",
        title="Related Placer Group Number",
        description="C | Item #01652",
    )

    tq2_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_6",
            "sequence_condition_code",
            "TQ2.6",
        ),
        serialization_alias="TQ2.6",
        title="Sequence Condition Code",
        description="C | Item #01653 | Table 0504 - Sequence Condition Code",
    )

    tq2_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_7",
            "cyclic_entry_exit_indicator",
            "TQ2.7",
        ),
        serialization_alias="TQ2.7",
        title="Cyclic Entry/Exit Indicator",
        description=(
            "C | Item #01654 | Table 0505 - Cyclic Entry/Exit Indicator | LEN:1"
        ),
    )

    tq2_8: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_8",
            "sequence_condition_time_interval",
            "TQ2.8",
        ),
        serialization_alias="TQ2.8",
        title="Sequence Condition Time Interval",
        description="O | Item #01655",
    )

    tq2_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_9",
            "cyclic_group_maximum_number_of_repeats",
            "TQ2.9",
        ),
        serialization_alias="TQ2.9",
        title="Cyclic Group Maximum Number of Repeats",
        description="O | Item #01656",
    )

    tq2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tq2_10",
            "special_service_request_relationship",
            "TQ2.10",
        ),
        serialization_alias="TQ2.10",
        title="Special Service Request Relationship",
        description=(
            "C | Item #01657 | Table 0506 - Service Request Relationship | LEN:1"
        ),
    )

    @field_validator("tq2_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("tq2_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
