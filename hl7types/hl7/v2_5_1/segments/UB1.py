"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: UB1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.OCD import OCD
from ..datatypes.UVC import UVC


class UB1(HL7Model):
    """UB82 (S6.5.10).

    Attributes
    ----------
    ub1_1 : str | None
        UB1.1 - Set ID - UB1 (SI) O S6.5.10.1

    ub1_2 : str | None
        UB1.2 - Blood Deductible  (43) (NM) O S6.5.10.2

    ub1_3 : str | None
        UB1.3 - Blood Furnished-Pints Of (40) (NM) O S6.5.10.3

    ub1_4 : str | None
        UB1.4 - Blood Replaced-Pints (41) (NM) O S6.5.10.4

    ub1_5 : str | None
        UB1.5 - Blood Not Replaced-Pints(42) (NM) O S6.5.10.5

    ub1_6 : str | None
        UB1.6 - Co-Insurance Days (25) (NM) O S6.5.10.6

    ub1_7 : list[str] | None
        UB1.7 - Condition Code (35-39) (IS) O rep S6.5.10.7 | 0043 - Condition Code

    ub1_8 : str | None
        UB1.8 - Covered Days - (23) (NM) O S6.5.10.8

    ub1_9 : str | None
        UB1.9 - Non Covered Days - (24) (NM) O S6.5.10.9

    ub1_10 : list[UVC] | None
        UB1.10 - Value Amount & Code (46-49) (UVC) O rep S6.5.10.10

    ub1_11 : str | None
        UB1.11 - Number Of Grace Days (90) (NM) O S6.5.10.11

    ub1_12 : CE | None
        UB1.12 - Special Program Indicator (44) (CE) O S6.5.10.12 | 0348 - Special Program Indicator

    ub1_13 : CE | None
        UB1.13 - PSRO/UR Approval Indicator (87) (CE) O S6.5.10.13 | 0349 - PSRO/UR Approval Indicator

    ub1_14 : str | None
        UB1.14 - PSRO/UR Approved Stay-Fm (88) (DT) O S6.5.10.14

    ub1_15 : str | None
        UB1.15 - PSRO/UR Approved Stay-To (89) (DT) O S6.5.10.15

    ub1_16 : list[OCD] | None
        UB1.16 - Occurrence (28-32) (OCD) O rep S6.5.10.16

    ub1_17 : CE | None
        UB1.17 - Occurrence Span (33) (CE) O S6.5.10.17 | 0351 - Occurrence span

    ub1_18 : str | None
        UB1.18 - Occur Span Start Date(33) (DT) O S6.5.10.18

    ub1_19 : str | None
        UB1.19 - Occur Span End Date (33) (DT) O S6.5.10.19

    ub1_20 : str | None
        UB1.20 - UB-82 Locator 2 (ST) O S6.5.10.20

    ub1_21 : str | None
        UB1.21 - UB-82 Locator 9 (ST) O S6.5.10.21

    ub1_22 : str | None
        UB1.22 - UB-82 Locator 27 (ST) O S6.5.10.22

    ub1_23 : str | None
        UB1.23 - UB-82 Locator 45 (ST) O S6.5.10.23
    """

    ub1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_1",
            "set_id_ub1",
            "UB1.1",
        ),
        serialization_alias="UB1.1",
        title="Set ID - UB1",
        description="O | Item #00530 | LEN:4",
    )

    ub1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_2",
            "blood_deductible_43",
            "UB1.2",
        ),
        serialization_alias="UB1.2",
        title="Blood Deductible  (43)",
        description="O | Item #00531 | LEN:1",
    )

    ub1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_3",
            "blood_furnished_pints_of_40",
            "UB1.3",
        ),
        serialization_alias="UB1.3",
        title="Blood Furnished-Pints Of (40)",
        description="O | Item #00532 | LEN:2",
    )

    ub1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_4",
            "blood_replaced_pints_41",
            "UB1.4",
        ),
        serialization_alias="UB1.4",
        title="Blood Replaced-Pints (41)",
        description="O | Item #00533 | LEN:2",
    )

    ub1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_5",
            "blood_not_replaced_pints_42",
            "UB1.5",
        ),
        serialization_alias="UB1.5",
        title="Blood Not Replaced-Pints(42)",
        description="O | Item #00534 | LEN:2",
    )

    ub1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_6",
            "co_insurance_days_25",
            "UB1.6",
        ),
        serialization_alias="UB1.6",
        title="Co-Insurance Days (25)",
        description="O | Item #00535 | LEN:2",
    )

    ub1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_7",
            "condition_code_35_39",
            "UB1.7",
        ),
        serialization_alias="UB1.7",
        title="Condition Code (35-39)",
        description="O | Item #00536 | Table 0043 - Condition Code | LEN:14",
    )

    ub1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_8",
            "covered_days_23",
            "UB1.8",
        ),
        serialization_alias="UB1.8",
        title="Covered Days - (23)",
        description="O | Item #00537 | LEN:3",
    )

    ub1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_9",
            "non_covered_days_24",
            "UB1.9",
        ),
        serialization_alias="UB1.9",
        title="Non Covered Days - (24)",
        description="O | Item #00538 | LEN:3",
    )

    ub1_10: Optional[List[UVC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_10",
            "value_amount_code_46_49",
            "UB1.10",
        ),
        serialization_alias="UB1.10",
        title="Value Amount & Code (46-49)",
        description="O | Item #00539",
    )

    ub1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_11",
            "number_of_grace_days_90",
            "UB1.11",
        ),
        serialization_alias="UB1.11",
        title="Number Of Grace Days (90)",
        description="O | Item #00540 | LEN:2",
    )

    ub1_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_12",
            "special_program_indicator_44",
            "UB1.12",
        ),
        serialization_alias="UB1.12",
        title="Special Program Indicator (44)",
        description="O | Item #00541 | Table 0348 - Special Program Indicator",
    )

    ub1_13: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_13",
            "psro_ur_approval_indicator_87",
            "UB1.13",
        ),
        serialization_alias="UB1.13",
        title="PSRO/UR Approval Indicator (87)",
        description="O | Item #00542 | Table 0349 - PSRO/UR Approval Indicator",
    )

    ub1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_14",
            "psro_ur_approved_stay_fm_88",
            "UB1.14",
        ),
        serialization_alias="UB1.14",
        title="PSRO/UR Approved Stay-Fm (88)",
        description="O | Item #00543 | LEN:8",
    )

    ub1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_15",
            "psro_ur_approved_stay_to_89",
            "UB1.15",
        ),
        serialization_alias="UB1.15",
        title="PSRO/UR Approved Stay-To (89)",
        description="O | Item #00544 | LEN:8",
    )

    ub1_16: Optional[List[OCD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_16",
            "occurrence_28_32",
            "UB1.16",
        ),
        serialization_alias="UB1.16",
        title="Occurrence (28-32)",
        description="O | Item #00545",
    )

    ub1_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_17",
            "occurrence_span_33",
            "UB1.17",
        ),
        serialization_alias="UB1.17",
        title="Occurrence Span (33)",
        description="O | Item #00546 | Table 0351 - Occurrence span",
    )

    ub1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_18",
            "occur_span_start_date_33",
            "UB1.18",
        ),
        serialization_alias="UB1.18",
        title="Occur Span Start Date(33)",
        description="O | Item #00547 | LEN:8",
    )

    ub1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_19",
            "occur_span_end_date_33",
            "UB1.19",
        ),
        serialization_alias="UB1.19",
        title="Occur Span End Date (33)",
        description="O | Item #00548 | LEN:8",
    )

    ub1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_20",
            "ub_82_locator_2",
            "UB1.20",
        ),
        serialization_alias="UB1.20",
        title="UB-82 Locator 2",
        description="O | Item #00549 | LEN:30",
    )

    ub1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_21",
            "ub_82_locator_9",
            "UB1.21",
        ),
        serialization_alias="UB1.21",
        title="UB-82 Locator 9",
        description="O | Item #00550 | LEN:7",
    )

    ub1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_22",
            "ub_82_locator_27",
            "UB1.22",
        ),
        serialization_alias="UB1.22",
        title="UB-82 Locator 27",
        description="O | Item #00551 | LEN:8",
    )

    ub1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_23",
            "ub_82_locator_45",
            "UB1.23",
        ),
        serialization_alias="UB1.23",
        title="UB-82 Locator 45",
        description="O | Item #00552 | LEN:17",
    )

    @field_validator("ub1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ub1_2", "ub1_3", "ub1_4", "ub1_5", "ub1_6", "ub1_8", "ub1_9", "ub1_11", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("ub1_14", "ub1_15", "ub1_18", "ub1_19", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
