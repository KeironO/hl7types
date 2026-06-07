"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: PV1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class PV1(HL7Model):
    """HL7 v2 PV1 segment.

    Attributes
    ----------
    pv1_1 : str | None
        PV1.1 (opt) - SET ID - PATIENT VISIT (SI)

    pv1_2 : str
        PV1.2 (req) - PATIENT CLASS (ID)

    pv1_3 : str
        PV1.3 (req) - ASSIGNED PATIENT LOCATION (ID)

    pv1_4 : str | None
        PV1.4 (opt) - ADMISSION TYPE (ID)

    pv1_5 : str | None
        PV1.5 (opt) - PRE-ADMIT NUMBER (ST)

    pv1_6 : str | None
        PV1.6 (opt) - PRIOR PATIENT LOCATION (ID)

    pv1_7 : str | None
        PV1.7 (opt) - ATTENDING DOCTOR (CN)

    pv1_8 : str | None
        PV1.8 (opt) - REFERRING DOCTOR (CN)

    pv1_9 : list[str] | None
        PV1.9 (opt, rep) - CONSULTING DOCTOR (CN)

    pv1_10 : str | None
        PV1.10 (opt) - HOSPITAL SERVICE (ID)

    pv1_11 : str | None
        PV1.11 (opt) - TEMPORARY LOCATION (ID)

    pv1_12 : str | None
        PV1.12 (opt) - PRE-ADMIT TEST INDICATOR (ID)

    pv1_13 : str | None
        PV1.13 (opt) - RE-ADMISSION INDICATOR (ID)

    pv1_14 : str | None
        PV1.14 (opt) - ADMIT SOURCE (ID)

    pv1_15 : str | None
        PV1.15 (opt) - AMBULATORY STATUS (ID)

    pv1_16 : str | None
        PV1.16 (opt) - VIP INDICATOR (ID)

    pv1_17 : str | None
        PV1.17 (opt) - ADMITTING DOCTOR (CN)

    pv1_18 : str | None
        PV1.18 (opt) - PATIENT TYPE (ID)

    pv1_19 : str | None
        PV1.19 (opt) - VISIT NUMBER (NM)

    pv1_20 : list[str] | None
        PV1.20 (opt, rep) - FINANCIAL CLASS (ID)

    pv1_21 : str | None
        PV1.21 (opt) - CHARGE PRICE INDICATOR (ID)

    pv1_22 : str | None
        PV1.22 (opt) - COURTESY CODE (ID)

    pv1_23 : str | None
        PV1.23 (opt) - CREDIT RATING (ID)

    pv1_24 : list[str] | None
        PV1.24 (opt, rep) - CONTRACT CODE (ID)

    pv1_25 : list[str] | None
        PV1.25 (opt, rep) - CONTRACT EFFECTIVE DATE (DT)

    pv1_26 : list[str] | None
        PV1.26 (opt, rep) - CONTRACT AMOUNT (NM)

    pv1_27 : list[str] | None
        PV1.27 (opt, rep) - CONTRACT PERIOD (NM)

    pv1_28 : str | None
        PV1.28 (opt) - INTEREST CODE (ID)

    pv1_29 : str | None
        PV1.29 (opt) - TRANSFER TO BAD DEBT CODE (ID)

    pv1_30 : str | None
        PV1.30 (opt) - TRANSFER TO BAD DEBT DATE (DT)

    pv1_31 : str | None
        PV1.31 (opt) - BAD DEBT AGENCY CODE (ST)

    pv1_32 : str | None
        PV1.32 (opt) - BAD DEBT TRANSFER AMOUNT (NM)

    pv1_33 : str | None
        PV1.33 (opt) - BAD DEBT RECOVERY AMOUNT (NM)

    pv1_34 : str | None
        PV1.34 (opt) - DELETE ACCOUNT INDICATOR (ID)

    pv1_35 : str | None
        PV1.35 (opt) - DELETE ACCOUNT DATE (DT)

    pv1_36 : str | None
        PV1.36 (opt) - DISCHARGE DISPOSITION (ID)

    pv1_37 : str | None
        PV1.37 (opt) - DISCHARGED TO LOCATION (ID)

    pv1_38 : str | None
        PV1.38 (opt) - DIET TYPE (ID)

    pv1_39 : str | None
        PV1.39 (opt) - SERVICING FACILITY (ID)

    pv1_40 : str | None
        PV1.40 (opt) - BED STATUS (ID)

    pv1_41 : str | None
        PV1.41 (opt) - ACCOUNT STATUS (ID)

    pv1_42 : str | None
        PV1.42 (opt) - PENDING LOCATION (ID)

    pv1_43 : str | None
        PV1.43 (opt) - PRIOR TEMPORARY LOCATION (ID)

    pv1_44 : str | None
        PV1.44 (opt) - ADMIT DATE/TIME (TS)

    pv1_45 : str | None
        PV1.45 (opt) - DISCHARGE DATE/TIME (TS)

    pv1_46 : str | None
        PV1.46 (opt) - CURRENT PATIENT BALANCE (NM)

    pv1_47 : str | None
        PV1.47 (opt) - TOTAL CHARGES (NM)

    pv1_48 : str | None
        PV1.48 (opt) - TOTAL ADJUSTMENTS (NM)

    pv1_49 : str | None
        PV1.49 (opt) - TOTAL PAYMENTS (NM)
    """

    pv1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_1",
            "set_id_patient_visit",
            "PV1.1",
        ),
        serialization_alias="PV1.1",
        title="SET ID - PATIENT VISIT",
        description="Item #458",
    )

    pv1_2: str = Field(
        validation_alias=AliasChoices(
            "pv1_2",
            "patient_class",
            "PV1.2",
        ),
        serialization_alias="PV1.2",
        title="PATIENT CLASS",
        description="Item #52 | Table HL70004",
    )

    pv1_3: str = Field(
        validation_alias=AliasChoices(
            "pv1_3",
            "assigned_patient_location",
            "PV1.3",
        ),
        serialization_alias="PV1.3",
        title="ASSIGNED PATIENT LOCATION",
        description="Item #53 | Table HL70079",
    )

    pv1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_4",
            "admission_type",
            "PV1.4",
        ),
        serialization_alias="PV1.4",
        title="ADMISSION TYPE",
        description="Item #218 | Table HL70007",
    )

    pv1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_5",
            "pre_admit_number",
            "PV1.5",
        ),
        serialization_alias="PV1.5",
        title="PRE-ADMIT NUMBER",
        description="Item #219",
    )

    pv1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_6",
            "prior_patient_location",
            "PV1.6",
        ),
        serialization_alias="PV1.6",
        title="PRIOR PATIENT LOCATION",
        description="Item #56 | Table HL70079",
    )

    pv1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_7",
            "attending_doctor",
            "PV1.7",
        ),
        serialization_alias="PV1.7",
        title="ATTENDING DOCTOR",
        description="Item #57 | Table HL70010",
    )

    pv1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_8",
            "referring_doctor",
            "PV1.8",
        ),
        serialization_alias="PV1.8",
        title="REFERRING DOCTOR",
        description="Item #579 | Table HL70010",
    )

    pv1_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_9",
            "consulting_doctor",
            "PV1.9",
        ),
        serialization_alias="PV1.9",
        title="CONSULTING DOCTOR",
        description="Item #580 | Table HL70010",
    )

    pv1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_10",
            "hospital_service",
            "PV1.10",
        ),
        serialization_alias="PV1.10",
        title="HOSPITAL SERVICE",
        description="Item #59 | Table HL70069",
    )

    pv1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_11",
            "temporary_location",
            "PV1.11",
        ),
        serialization_alias="PV1.11",
        title="TEMPORARY LOCATION",
        description="Item #60 | Table HL70079",
    )

    pv1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_12",
            "pre_admit_test_indicator",
            "PV1.12",
        ),
        serialization_alias="PV1.12",
        title="PRE-ADMIT TEST INDICATOR",
        description="Item #220 | Table HL70087",
    )

    pv1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_13",
            "re_admission_indicator",
            "PV1.13",
        ),
        serialization_alias="PV1.13",
        title="RE-ADMISSION INDICATOR",
        description="Item #221 | Table HL70092",
    )

    pv1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_14",
            "admit_source",
            "PV1.14",
        ),
        serialization_alias="PV1.14",
        title="ADMIT SOURCE",
        description="Item #63 | Table HL70023",
    )

    pv1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_15",
            "ambulatory_status",
            "PV1.15",
        ),
        serialization_alias="PV1.15",
        title="AMBULATORY STATUS",
        description="Item #64 | Table HL70009",
    )

    pv1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_16",
            "vip_indicator",
            "PV1.16",
        ),
        serialization_alias="PV1.16",
        title="VIP INDICATOR",
        description="Item #193 | Table HL70099",
    )

    pv1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_17",
            "admitting_doctor",
            "PV1.17",
        ),
        serialization_alias="PV1.17",
        title="ADMITTING DOCTOR",
        description="Item #189 | Table HL70010",
    )

    pv1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_18",
            "patient_type",
            "PV1.18",
        ),
        serialization_alias="PV1.18",
        title="PATIENT TYPE",
        description="Item #191 | Table HL70018",
    )

    pv1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_19",
            "visit_number",
            "PV1.19",
        ),
        serialization_alias="PV1.19",
        title="VISIT NUMBER",
        description="Item #194",
    )

    pv1_20: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_20",
            "financial_class",
            "PV1.20",
        ),
        serialization_alias="PV1.20",
        title="FINANCIAL CLASS",
        description="Item #195 | Table HL70064",
    )

    pv1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_21",
            "charge_price_indicator",
            "PV1.21",
        ),
        serialization_alias="PV1.21",
        title="CHARGE PRICE INDICATOR",
        description="Item #199 | Table HL70032",
    )

    pv1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_22",
            "courtesy_code",
            "PV1.22",
        ),
        serialization_alias="PV1.22",
        title="COURTESY CODE",
        description="Item #386 | Table HL70045",
    )

    pv1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_23",
            "credit_rating",
            "PV1.23",
        ),
        serialization_alias="PV1.23",
        title="CREDIT RATING",
        description="Item #200 | Table HL70046",
    )

    pv1_24: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_24",
            "contract_code",
            "PV1.24",
        ),
        serialization_alias="PV1.24",
        title="CONTRACT CODE",
        description="Item #201 | Table HL70044",
    )

    pv1_25: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_25",
            "contract_effective_date",
            "PV1.25",
        ),
        serialization_alias="PV1.25",
        title="CONTRACT EFFECTIVE DATE",
        description="Item #202",
    )

    pv1_26: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_26",
            "contract_amount",
            "PV1.26",
        ),
        serialization_alias="PV1.26",
        title="CONTRACT AMOUNT",
        description="Item #203",
    )

    pv1_27: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_27",
            "contract_period",
            "PV1.27",
        ),
        serialization_alias="PV1.27",
        title="CONTRACT PERIOD",
        description="Item #204",
    )

    pv1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_28",
            "interest_code",
            "PV1.28",
        ),
        serialization_alias="PV1.28",
        title="INTEREST CODE",
        description="Item #387 | Table HL70073",
    )

    pv1_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_29",
            "transfer_to_bad_debt_code",
            "PV1.29",
        ),
        serialization_alias="PV1.29",
        title="TRANSFER TO BAD DEBT CODE",
        description="Item #205 | Table HL70110",
    )

    pv1_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_30",
            "transfer_to_bad_debt_date",
            "PV1.30",
        ),
        serialization_alias="PV1.30",
        title="TRANSFER TO BAD DEBT DATE",
        description="Item #388",
    )

    pv1_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_31",
            "bad_debt_agency_code",
            "PV1.31",
        ),
        serialization_alias="PV1.31",
        title="BAD DEBT AGENCY CODE",
        description="Item #206 | Table HL70021",
    )

    pv1_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_32",
            "bad_debt_transfer_amount",
            "PV1.32",
        ),
        serialization_alias="PV1.32",
        title="BAD DEBT TRANSFER AMOUNT",
        description="Item #389",
    )

    pv1_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_33",
            "bad_debt_recovery_amount",
            "PV1.33",
        ),
        serialization_alias="PV1.33",
        title="BAD DEBT RECOVERY AMOUNT",
        description="Item #390",
    )

    pv1_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_34",
            "delete_account_indicator",
            "PV1.34",
        ),
        serialization_alias="PV1.34",
        title="DELETE ACCOUNT INDICATOR",
        description="Item #207 | Table HL70111",
    )

    pv1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_35",
            "delete_account_date",
            "PV1.35",
        ),
        serialization_alias="PV1.35",
        title="DELETE ACCOUNT DATE",
        description="Item #208",
    )

    pv1_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_36",
            "discharge_disposition",
            "PV1.36",
        ),
        serialization_alias="PV1.36",
        title="DISCHARGE DISPOSITION",
        description="Item #613 | Table HL70112",
    )

    pv1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_37",
            "discharged_to_location",
            "PV1.37",
        ),
        serialization_alias="PV1.37",
        title="DISCHARGED TO LOCATION",
        description="Item #614 | Table HL70113",
    )

    pv1_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_38",
            "diet_type",
            "PV1.38",
        ),
        serialization_alias="PV1.38",
        title="DIET TYPE",
        description="Item #615 | Table HL70114",
    )

    pv1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_39",
            "servicing_facility",
            "PV1.39",
        ),
        serialization_alias="PV1.39",
        title="SERVICING FACILITY",
        description="Item #616 | Table HL70115",
    )

    pv1_40: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_40",
            "bed_status",
            "PV1.40",
        ),
        serialization_alias="PV1.40",
        title="BED STATUS",
        description="Item #617 | Table HL70116",
    )

    pv1_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_41",
            "account_status",
            "PV1.41",
        ),
        serialization_alias="PV1.41",
        title="ACCOUNT STATUS",
        description="Item #703 | Table HL70117",
    )

    pv1_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_42",
            "pending_location",
            "PV1.42",
        ),
        serialization_alias="PV1.42",
        title="PENDING LOCATION",
        description="Item #704 | Table HL70079",
    )

    pv1_43: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_43",
            "prior_temporary_location",
            "PV1.43",
        ),
        serialization_alias="PV1.43",
        title="PRIOR TEMPORARY LOCATION",
        description="Item #705 | Table HL70079",
    )

    pv1_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_44",
            "admit_date_time",
            "PV1.44",
        ),
        serialization_alias="PV1.44",
        title="ADMIT DATE/TIME",
        description="Item #775",
    )

    pv1_45: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_45",
            "discharge_date_time",
            "PV1.45",
        ),
        serialization_alias="PV1.45",
        title="DISCHARGE DATE/TIME",
        description="Item #776",
    )

    pv1_46: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_46",
            "current_patient_balance",
            "PV1.46",
        ),
        serialization_alias="PV1.46",
        title="CURRENT PATIENT BALANCE",
        description="Item #777",
    )

    pv1_47: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_47",
            "total_charges",
            "PV1.47",
        ),
        serialization_alias="PV1.47",
        title="TOTAL CHARGES",
        description="Item #778",
    )

    pv1_48: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_48",
            "total_adjustments",
            "PV1.48",
        ),
        serialization_alias="PV1.48",
        title="TOTAL ADJUSTMENTS",
        description="Item #779",
    )

    pv1_49: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_49",
            "total_payments",
            "PV1.49",
        ),
        serialization_alias="PV1.49",
        title="TOTAL PAYMENTS",
        description="Item #780",
    )

    @field_validator("pv1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pv1_19", "pv1_26", "pv1_27", "pv1_32", "pv1_33", "pv1_46", "pv1_47", "pv1_48", "pv1_49", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("pv1_25", "pv1_30", "pv1_35", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
