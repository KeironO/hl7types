"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: UB1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class UB1(BaseModel):
    """HL7 v2 UB1 segment."""

    ub1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_1",
            "set_id_ub82",
            "UB1.1",
        ),
        serialization_alias="UB1.1",
        title="SET ID - UB82",
        description="Item #459",
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
        description="Item #279",
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
        description="Item #396",
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
        description="Item #397",
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
        description="Item #398",
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
        description="Item #399",
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
        description="Item #400 | Table HL70043",
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
        description="Item #405",
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
        description="Item #406",
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
        description="Item #407",
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
        description="Item #424",
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
        description="Item #425",
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
        description="Item #426",
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
        description="Item #427",
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
        description="Item #428",
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
        description="Item #429",
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
        description="Item #435",
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
        description="Item #446",
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
        description="Item #447",
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
        description="Item #448",
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
        description="Item #449",
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
        description="Item #450",
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
        description="Item #451",
    )

    model_config = {"populate_by_name": True}
