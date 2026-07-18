"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: UB1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class UB1(HL7Model):
    """UB82 DATA (S6.4.9).

    Attributes
    ----------
    ub1_1 : str | None
        UB1.1 - Set ID - UB82 (SI) NA S6.4.9.1

    ub1_2 : str | None
        UB1.2 - Blood deductible (43) (NM) NA S6.4.6.21 | 0136 - Y/N Indicator

    ub1_3 : str | None
        UB1.3 - Blood furnished pints of (40) (NM) NA S6-30

    ub1_4 : str | None
        UB1.4 - Blood replaced pints (41) (NM) NA S6.4.9.4

    ub1_5 : str | None
        UB1.5 - Blood not replaced pints (42) (NM) NA S6.4.9.5

    ub1_6 : str | None
        UB1.6 - Co-insurance days (25) (NM) NA S6.4.9.6

    ub1_7 : list[str] | None
        UB1.7 - Condition code (35-39) (ID) NA rep S6.4.9.7 | 0043 - CONDITION CODE

    ub1_8 : str | None
        UB1.8 - Covered days (23) (NM) NA S6.4.9.8

    ub1_9 : str | None
        UB1.9 - Non-covered days (24) (NM) NA S6.4.9.9

    ub1_10 : list[str] | None
        UB1.10 - Value amount and code (46-49) (CM) NA rep S6.4.9.10 | 0153 - VALUE CODE

    ub1_11 : str | None
        UB1.11 - Number of grace days (90) (NM) NA S6-31

    ub1_12 : str | None
        UB1.12 - Special program indicator (44) (ID) NA S6.4.9.12

    ub1_13 : str | None
        UB1.13 - PSRO / UR approval indicator (87) (ID) NA S6.4.9.13

    ub1_14 : str | None
        UB1.14 - PSRO / UR approved stay - from (88) (DT) NA S6.4.9.14

    ub1_15 : str | None
        UB1.15 - PSRO / UR approved stay - to (89) (DT) NA S6.4.9.15

    ub1_16 : list[str] | None
        UB1.16 - Occurrence (28-32) (CM) NA rep S6.4.9.16

    ub1_17 : str | None
        UB1.17 - Occurrence span (33) (ID) NA S6.4.9.17

    ub1_18 : str | None
        UB1.18 - Occurrence span start date (33) (DT) NA S6.4.9.18

    ub1_19 : str | None
        UB1.19 - Occurrence span end date (33) (DT) NA S6.4.9.19

    ub1_20 : str | None
        UB1.20 - UB-82 locator 2 (ST) NA S6.4.9.20

    ub1_21 : str | None
        UB1.21 - UB-82 locator 9 (ST) NA S6.4.9.21

    ub1_22 : str | None
        UB1.22 - UB-82 locator 27 (ST) NA S6.4.9.22

    ub1_23 : str | None
        UB1.23 - UB-82 locator 45 (ST) NA S6.4.9.23
    """

    ub1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_1",
            "set_id_ub82",
            "UB1.1",
        ),
        serialization_alias="UB1.1",
        title="Set ID - UB82",
        description="NA | Item #00530 | LEN:4",
    )

    ub1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_2",
            "blood_deductible_43",
            "UB1.2",
        ),
        serialization_alias="UB1.2",
        title="Blood deductible (43)",
        description="NA | Item #00492 | Table 0136 - Y/N Indicator | LEN:1",
    )

    ub1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_3",
            "blood_furnished_pints_of_40",
            "UB1.3",
        ),
        serialization_alias="UB1.3",
        title="Blood furnished pints of (40)",
        description="NA | Item #00532 | LEN:2",
    )

    ub1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_4",
            "blood_replaced_pints_41",
            "UB1.4",
        ),
        serialization_alias="UB1.4",
        title="Blood replaced pints (41)",
        description="NA | Item #00533 | LEN:2",
    )

    ub1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_5",
            "blood_not_replaced_pints_42",
            "UB1.5",
        ),
        serialization_alias="UB1.5",
        title="Blood not replaced pints (42)",
        description="NA | Item #00534 | LEN:2",
    )

    ub1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_6",
            "co_insurance_days_25",
            "UB1.6",
        ),
        serialization_alias="UB1.6",
        title="Co-insurance days (25)",
        description="NA | Item #00535 | LEN:2",
    )

    ub1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_7",
            "condition_code_35_39",
            "UB1.7",
        ),
        serialization_alias="UB1.7",
        title="Condition code (35-39)",
        description="NA | Item #00536 | Table 0043 - CONDITION CODE | LEN:2",
    )

    ub1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_8",
            "covered_days_23",
            "UB1.8",
        ),
        serialization_alias="UB1.8",
        title="Covered days (23)",
        description="NA | Item #00537 | LEN:3",
    )

    ub1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_9",
            "non_covered_days_24",
            "UB1.9",
        ),
        serialization_alias="UB1.9",
        title="Non-covered days (24)",
        description="NA | Item #00538 | LEN:3",
    )

    ub1_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_10",
            "value_amount_and_code_46_49",
            "UB1.10",
        ),
        serialization_alias="UB1.10",
        title="Value amount and code (46-49)",
        description="NA | Item #00539 | Table 0153 - VALUE CODE",
    )

    ub1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_11",
            "number_of_grace_days_90",
            "UB1.11",
        ),
        serialization_alias="UB1.11",
        title="Number of grace days (90)",
        description="NA | Item #00540 | LEN:2",
    )

    ub1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_12",
            "special_program_indicator_44",
            "UB1.12",
        ),
        serialization_alias="UB1.12",
        title="Special program indicator (44)",
        description="NA | Item #00541 | LEN:2",
    )

    ub1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_13",
            "psro_ur_approval_indicator_87",
            "UB1.13",
        ),
        serialization_alias="UB1.13",
        title="PSRO / UR approval indicator (87)",
        description="NA | Item #00542 | LEN:1",
    )

    ub1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_14",
            "psro_ur_approved_stay_from_88",
            "UB1.14",
        ),
        serialization_alias="UB1.14",
        title="PSRO / UR approved stay - from (88)",
        description="NA | Item #00543 | LEN:8",
    )

    ub1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_15",
            "psro_ur_approved_stay_to_89",
            "UB1.15",
        ),
        serialization_alias="UB1.15",
        title="PSRO / UR approved stay - to (89)",
        description="NA | Item #00544 | LEN:8",
    )

    ub1_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_16",
            "occurrence_28_32",
            "UB1.16",
        ),
        serialization_alias="UB1.16",
        title="Occurrence (28-32)",
        description="NA | Item #00545",
    )

    ub1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_17",
            "occurrence_span_33",
            "UB1.17",
        ),
        serialization_alias="UB1.17",
        title="Occurrence span (33)",
        description="NA | Item #00546 | LEN:2",
    )

    ub1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_18",
            "occurrence_span_start_date_33",
            "UB1.18",
        ),
        serialization_alias="UB1.18",
        title="Occurrence span start date (33)",
        description="NA | Item #00547 | LEN:8",
    )

    ub1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_19",
            "occurrence_span_end_date_33",
            "UB1.19",
        ),
        serialization_alias="UB1.19",
        title="Occurrence span end date (33)",
        description="NA | Item #00548 | LEN:8",
    )

    ub1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_20",
            "ub_82_locator_2",
            "UB1.20",
        ),
        serialization_alias="UB1.20",
        title="UB-82 locator 2",
        description="NA | Item #00549 | LEN:30",
    )

    ub1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_21",
            "ub_82_locator_9",
            "UB1.21",
        ),
        serialization_alias="UB1.21",
        title="UB-82 locator 9",
        description="NA | Item #00550 | LEN:7",
    )

    ub1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_22",
            "ub_82_locator_27",
            "UB1.22",
        ),
        serialization_alias="UB1.22",
        title="UB-82 locator 27",
        description="NA | Item #00551 | LEN:8",
    )

    ub1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_23",
            "ub_82_locator_45",
            "UB1.23",
        ),
        serialization_alias="UB1.23",
        title="UB-82 locator 45",
        description="NA | Item #00552 | LEN:17",
    )

    @field_validator("ub1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ub1_2", "ub1_3", "ub1_4", "ub1_5", "ub1_6", "ub1_8", "ub1_9", "ub1_11", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("ub1_14", "ub1_15", "ub1_18", "ub1_19", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
