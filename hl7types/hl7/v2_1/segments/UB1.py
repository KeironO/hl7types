"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: UB1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class UB1(HL7Model):
    """UB82 DATA (S6.3.8).

    Attributes
    ----------
    ub1_1 : str | None
        UB1.1 - SET ID - UB82 (SI) O S6-17

    ub1_2 : str | None
        UB1.2 - BLOOD DEDUCTIBLE (ST) O

    ub1_3 : str | None
        UB1.3 - BLOOD FURN.-PINTS OF (40) (ST) O

    ub1_4 : str | None
        UB1.4 - BLOOD REPLACED-PINTS (41) (ST) O

    ub1_5 : str | None
        UB1.5 - BLOOD NOT RPLCD-PINTS(42) (ST) O

    ub1_6 : str | None
        UB1.6 - CO-INSURANCE DAYS (25) (ST) O

    ub1_7 : list[str] | None
        UB1.7 - CONDITION CODE (ID) O rep | 0043 - CONDITION

    ub1_8 : str | None
        UB1.8 - COVERED DAYS - (23) (ST) O

    ub1_9 : str | None
        UB1.9 - NON COVERED DAYS - (24) (ST) O

    ub1_10 : list[str] | None
        UB1.10 - VALUE AMOUNT & CODE (CM) O rep

    ub1_11 : str | None
        UB1.11 - NUMBER OF GRACE DAYS (90) (ST) O

    ub1_12 : str | None
        UB1.12 - SPEC. PROG. INDICATOR(44) (ID) O

    ub1_13 : str | None
        UB1.13 - PSRO/UR APPROVAL IND. (87) (ID) O

    ub1_14 : str | None
        UB1.14 - PSRO/UR APRVD STAY-FM(88) (DT) O

    ub1_15 : str | None
        UB1.15 - PSRO/UR APRVD STAY-TO(89) (DT) O

    ub1_16 : list[str] | None
        UB1.16 - OCCURRENCE (28-32) (ID) O rep

    ub1_17 : str | None
        UB1.17 - OCCURRENCE SPAN (33) (ID) O

    ub1_18 : str | None
        UB1.18 - OCCURRENCE SPAN START DATE(33) (DT) O

    ub1_19 : str | None
        UB1.19 - OCCUR. SPAN END DATE (33) (DT) O

    ub1_20 : str | None
        UB1.20 - UB-82 LOCATOR 2 (ST) O

    ub1_21 : str | None
        UB1.21 - UB-82 LOCATOR 9 (ST) O

    ub1_22 : str | None
        UB1.22 - UB-82 LOCATOR 27 (ST) O

    ub1_23 : str | None
        UB1.23 - UB-82 LOCATOR 45 (ST) O
    """

    ub1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_1",
            "set_id_ub82",
            "UB1.1",
        ),
        serialization_alias="UB1.1",
        title="SET ID - UB82",
        description="O | Item #00459 | LEN:4",
    )

    ub1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_2",
            "blood_deductible",
            "UB1.2",
        ),
        serialization_alias="UB1.2",
        title="BLOOD DEDUCTIBLE",
        description="O | Item #00279 | LEN:1",
    )

    ub1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_3",
            "blood_furn_pints_of_40",
            "UB1.3",
        ),
        serialization_alias="UB1.3",
        title="BLOOD FURN.-PINTS OF (40)",
        description="O | Item #00396 | LEN:2",
    )

    ub1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_4",
            "blood_replaced_pints_41",
            "UB1.4",
        ),
        serialization_alias="UB1.4",
        title="BLOOD REPLACED-PINTS (41)",
        description="O | Item #00397 | LEN:2",
    )

    ub1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_5",
            "blood_not_rplcd_pints_42",
            "UB1.5",
        ),
        serialization_alias="UB1.5",
        title="BLOOD NOT RPLCD-PINTS(42)",
        description="O | Item #00398 | LEN:2",
    )

    ub1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_6",
            "co_insurance_days_25",
            "UB1.6",
        ),
        serialization_alias="UB1.6",
        title="CO-INSURANCE DAYS (25)",
        description="O | Item #00399 | LEN:2",
    )

    ub1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_7",
            "condition_code",
            "UB1.7",
        ),
        serialization_alias="UB1.7",
        title="CONDITION CODE",
        description="O | Item #00400 | Table 0043 - CONDITION | LEN:2",
    )

    ub1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_8",
            "covered_days_23",
            "UB1.8",
        ),
        serialization_alias="UB1.8",
        title="COVERED DAYS - (23)",
        description="O | Item #00405 | LEN:3",
    )

    ub1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_9",
            "non_covered_days_24",
            "UB1.9",
        ),
        serialization_alias="UB1.9",
        title="NON COVERED DAYS - (24)",
        description="O | Item #00406 | LEN:3",
    )

    ub1_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_10",
            "value_amount_code",
            "UB1.10",
        ),
        serialization_alias="UB1.10",
        title="VALUE AMOUNT & CODE",
        description="O | Item #00407 | LEN:12",
    )

    ub1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_11",
            "number_of_grace_days_90",
            "UB1.11",
        ),
        serialization_alias="UB1.11",
        title="NUMBER OF GRACE DAYS (90)",
        description="O | Item #00424 | LEN:2",
    )

    ub1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_12",
            "spec_prog_indicator_44",
            "UB1.12",
        ),
        serialization_alias="UB1.12",
        title="SPEC. PROG. INDICATOR(44)",
        description="O | Item #00425 | LEN:2",
    )

    ub1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_13",
            "psro_ur_approval_ind_87",
            "UB1.13",
        ),
        serialization_alias="UB1.13",
        title="PSRO/UR APPROVAL IND. (87)",
        description="O | Item #00426 | LEN:1",
    )

    ub1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_14",
            "psro_ur_aprvd_stay_fm_88",
            "UB1.14",
        ),
        serialization_alias="UB1.14",
        title="PSRO/UR APRVD STAY-FM(88)",
        description="O | Item #00427 | LEN:8",
    )

    ub1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_15",
            "psro_ur_aprvd_stay_to_89",
            "UB1.15",
        ),
        serialization_alias="UB1.15",
        title="PSRO/UR APRVD STAY-TO(89)",
        description="O | Item #00428 | LEN:8",
    )

    ub1_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_16",
            "occurrence_28_32",
            "UB1.16",
        ),
        serialization_alias="UB1.16",
        title="OCCURRENCE (28-32)",
        description="O | Item #00429 | LEN:20",
    )

    ub1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_17",
            "occurrence_span_33",
            "UB1.17",
        ),
        serialization_alias="UB1.17",
        title="OCCURRENCE SPAN (33)",
        description="O | Item #00435 | LEN:2",
    )

    ub1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_18",
            "occurrence_span_start_date_33",
            "UB1.18",
        ),
        serialization_alias="UB1.18",
        title="OCCURRENCE SPAN START DATE(33)",
        description="O | Item #00446 | LEN:8",
    )

    ub1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_19",
            "occur_span_end_date_33",
            "UB1.19",
        ),
        serialization_alias="UB1.19",
        title="OCCUR. SPAN END DATE (33)",
        description="O | Item #00447 | LEN:8",
    )

    ub1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_20",
            "ub_82_locator_2",
            "UB1.20",
        ),
        serialization_alias="UB1.20",
        title="UB-82 LOCATOR 2",
        description="O | Item #00448 | LEN:30",
    )

    ub1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_21",
            "ub_82_locator_9",
            "UB1.21",
        ),
        serialization_alias="UB1.21",
        title="UB-82 LOCATOR 9",
        description="O | Item #00449 | LEN:7",
    )

    ub1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_22",
            "ub_82_locator_27",
            "UB1.22",
        ),
        serialization_alias="UB1.22",
        title="UB-82 LOCATOR 27",
        description="O | Item #00450 | LEN:8",
    )

    ub1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_23",
            "ub_82_locator_45",
            "UB1.23",
        ),
        serialization_alias="UB1.23",
        title="UB-82 LOCATOR 45",
        description="O | Item #00451 | LEN:17",
    )

    @field_validator("ub1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ub1_14", "ub1_15", "ub1_18", "ub1_19", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
