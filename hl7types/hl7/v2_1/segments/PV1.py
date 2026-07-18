"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: PV1
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


class PV1(HL7Model):
    """PATIENT VISIT (S3.3.4).

    Attributes
    ----------
    pv1_1 : str | None
        PV1.1 - SET ID - PATIENT VISIT (SI) O S3-18

    pv1_2 : str
        PV1.2 - PATIENT CLASS (ID) R | 0004 - PATIENT CLASS

    pv1_3 : str
        PV1.3 - ASSIGNED PATIENT LOCATION (ID) R | 0079 - LOCATION

    pv1_4 : str | None
        PV1.4 - ADMISSION TYPE (ID) O | 0007 - ADMISSION TYPE

    pv1_5 : str | None
        PV1.5 - PRE-ADMIT NUMBER (ST) O

    pv1_6 : str | None
        PV1.6 - PRIOR PATIENT LOCATION (ID) O | 0079 - LOCATION

    pv1_7 : str | None
        PV1.7 - ATTENDING DOCTOR (CN) O | 0010 - PHYSICIAN ID

    pv1_8 : str | None
        PV1.8 - REFERRING DOCTOR (CN) O | 0010 - PHYSICIAN ID

    pv1_9 : list[str] | None
        PV1.9 - CONSULTING DOCTOR (CN) O rep | 0010 - PHYSICIAN ID

    pv1_10 : str | None
        PV1.10 - HOSPITAL SERVICE (ID) O | 0069 - HOSPITAL SERVICE

    pv1_11 : str | None
        PV1.11 - TEMPORARY LOCATION (ID) O | 0079 - LOCATION

    pv1_12 : str | None
        PV1.12 - PRE-ADMIT TEST INDICATOR (ID) O | 0087 - PRE-ADMIT TESTING

    pv1_13 : str | None
        PV1.13 - RE-ADMISSION INDICATOR (ID) O | 0092 - RE-ADMISSION INDICATOR

    pv1_14 : str | None
        PV1.14 - ADMIT SOURCE (ID) O | 0023 - ADMIT SOURCE

    pv1_15 : str | None
        PV1.15 - AMBULATORY STATUS (ID) O | 0009 - AMBULATORY STATUS

    pv1_16 : str | None
        PV1.16 - VIP INDICATOR (ID) O | 0099 - VIP INDICATOR

    pv1_17 : str | None
        PV1.17 - ADMITTING DOCTOR (CN) O | 0010 - PHYSICIAN ID

    pv1_18 : str | None
        PV1.18 - PATIENT TYPE (ID) O | 0018 - PATIENT TYPE

    pv1_19 : str | None
        PV1.19 - VISIT NUMBER (NM) O

    pv1_20 : list[str] | None
        PV1.20 - FINANCIAL CLASS (ID) O rep | 0064 - FINANCIAL CLASS

    pv1_21 : str | None
        PV1.21 - CHARGE PRICE INDICATOR (ID) O | 0032 - CHARGE/PRICE INDICATOR

    pv1_22 : str | None
        PV1.22 - COURTESY CODE (ID) O | 0045 - COURTESY CODE

    pv1_23 : str | None
        PV1.23 - CREDIT RATING (ID) O | 0046 - CREDIT RATING

    pv1_24 : list[str] | None
        PV1.24 - CONTRACT CODE (ID) O rep | 0044 - CONTRACT CODE

    pv1_25 : list[str] | None
        PV1.25 - CONTRACT EFFECTIVE DATE (DT) O rep

    pv1_26 : list[str] | None
        PV1.26 - CONTRACT AMOUNT (NM) O rep

    pv1_27 : list[str] | None
        PV1.27 - CONTRACT PERIOD (NM) O rep

    pv1_28 : str | None
        PV1.28 - INTEREST CODE (ID) O | 0073 - INTEREST RATE CODE

    pv1_29 : str | None
        PV1.29 - TRANSFER TO BAD DEBT CODE (ID) O | 0110 - TRANSFER TO BAD DEBT CODE

    pv1_30 : str | None
        PV1.30 - TRANSFER TO BAD DEBT DATE (DT) O

    pv1_31 : str | None
        PV1.31 - BAD DEBT AGENCY CODE (ST) O | 0021 - BAD DEBT AGENCY CODE

    pv1_32 : str | None
        PV1.32 - BAD DEBT TRANSFER AMOUNT (NM) O

    pv1_33 : str | None
        PV1.33 - BAD DEBT RECOVERY AMOUNT (NM) O

    pv1_34 : str | None
        PV1.34 - DELETE ACCOUNT INDICATOR (ID) O | 0111 - DELETE ACCOUNT CODE

    pv1_35 : str | None
        PV1.35 - DELETE ACCOUNT DATE (DT) O

    pv1_36 : str | None
        PV1.36 - DISCHARGE DISPOSITION (ID) O | 0112 - DISCHARGED DISPOSITION

    pv1_37 : str | None
        PV1.37 - DISCHARGED TO LOCATION (ID) O | 0113 - DISCHARGED TO LOCATION

    pv1_38 : str | None
        PV1.38 - DIET TYPE (ID) O | 0114 - DIET TYPE

    pv1_39 : str | None
        PV1.39 - SERVICING FACILITY (ID) O | 0115 - SERVICING FACILITY

    pv1_40 : str | None
        PV1.40 - BED STATUS (ID) O | 0116 - BED STATUS

    pv1_41 : str | None
        PV1.41 - ACCOUNT STATUS (ID) O | 0117 - ACCOUNT STATUS

    pv1_42 : str | None
        PV1.42 - PENDING LOCATION (ID) O | 0079 - LOCATION

    pv1_43 : str | None
        PV1.43 - PRIOR TEMPORARY LOCATION (ID) O | 0079 - LOCATION

    pv1_44 : str | None
        PV1.44 - ADMIT DATE/TIME (TS) O

    pv1_45 : str | None
        PV1.45 - DISCHARGE DATE/TIME (TS) O

    pv1_46 : str | None
        PV1.46 - CURRENT PATIENT BALANCE (NM) O

    pv1_47 : str | None
        PV1.47 - TOTAL CHARGES (NM) O

    pv1_48 : str | None
        PV1.48 - TOTAL ADJUSTMENTS (NM) O

    pv1_49 : str | None
        PV1.49 - TOTAL PAYMENTS (NM) O
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
        description="O | Item #00458 | LEN:4",
    )

    pv1_2: str = Field(
        validation_alias=AliasChoices(
            "pv1_2",
            "patient_class",
            "PV1.2",
        ),
        serialization_alias="PV1.2",
        title="PATIENT CLASS",
        description="R | Item #00052 | Table 0004 - PATIENT CLASS | LEN:1",
    )

    pv1_3: str = Field(
        validation_alias=AliasChoices(
            "pv1_3",
            "assigned_patient_location",
            "PV1.3",
        ),
        serialization_alias="PV1.3",
        title="ASSIGNED PATIENT LOCATION",
        description="R | Item #00053 | Table 0079 - LOCATION | LEN:12",
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
        description="O | Item #00218 | Table 0007 - ADMISSION TYPE | LEN:2",
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
        description="O | Item #00219 | LEN:20",
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
        description="O | Item #00056 | Table 0079 - LOCATION | LEN:12",
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
        description="O | Item #00057 | Table 0010 - PHYSICIAN ID | LEN:60",
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
        description="O | Item #00579 | Table 0010 - PHYSICIAN ID | LEN:60",
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
        description="O | Item #00580 | Table 0010 - PHYSICIAN ID | LEN:60",
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
        description="O | Item #00059 | Table 0069 - HOSPITAL SERVICE | LEN:3",
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
        description="O | Item #00060 | Table 0079 - LOCATION | LEN:12",
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
        description="O | Item #00220 | Table 0087 - PRE-ADMIT TESTING | LEN:2",
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
        description=(
            "O | Item #00221 | Table 0092 - RE-ADMISSION INDICATOR | LEN:2"
        ),
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
        description="O | Item #00063 | Table 0023 - ADMIT SOURCE | LEN:3",
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
        description="O | Item #00064 | Table 0009 - AMBULATORY STATUS | LEN:2",
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
        description="O | Item #00193 | Table 0099 - VIP INDICATOR | LEN:2",
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
        description="O | Item #00189 | Table 0010 - PHYSICIAN ID | LEN:60",
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
        description="O | Item #00191 | Table 0018 - PATIENT TYPE | LEN:2",
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
        description="O | Item #00194 | LEN:4",
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
        description="O | Item #00195 | Table 0064 - FINANCIAL CLASS | LEN:11",
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
        description=(
            "O | Item #00199 | Table 0032 - CHARGE/PRICE INDICATOR | LEN:2"
        ),
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
        description="O | Item #00386 | Table 0045 - COURTESY CODE | LEN:2",
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
        description="O | Item #00200 | Table 0046 - CREDIT RATING | LEN:2",
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
        description="O | Item #00201 | Table 0044 - CONTRACT CODE | LEN:2",
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
        description="O | Item #00202 | LEN:8",
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
        description="O | Item #00203 | LEN:12",
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
        description="O | Item #00204 | LEN:3",
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
        description="O | Item #00387 | Table 0073 - INTEREST RATE CODE | LEN:2",
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
        description=(
            "O | Item #00205 | Table 0110 - TRANSFER TO BAD DEBT CODE | LEN:1"
        ),
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
        description="O | Item #00388 | LEN:8",
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
        description=(
            "O | Item #00206 | Table 0021 - BAD DEBT AGENCY CODE | LEN:10"
        ),
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
        description="O | Item #00389 | LEN:12",
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
        description="O | Item #00390 | LEN:12",
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
        description=(
            "O | Item #00207 | Table 0111 - DELETE ACCOUNT CODE | LEN:1"
        ),
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
        description="O | Item #00208 | LEN:8",
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
        description=(
            "O | Item #00613 | Table 0112 - DISCHARGED DISPOSITION | LEN:2"
        ),
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
        description=(
            "O | Item #00614 | Table 0113 - DISCHARGED TO LOCATION | LEN:2"
        ),
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
        description="O | Item #00615 | Table 0114 - DIET TYPE | LEN:2",
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
        description="O | Item #00616 | Table 0115 - SERVICING FACILITY | LEN:2",
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
        description="O | Item #00617 | Table 0116 - BED STATUS | LEN:1",
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
        description="O | Item #00703 | Table 0117 - ACCOUNT STATUS | LEN:2",
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
        description="O | Item #00704 | Table 0079 - LOCATION | LEN:12",
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
        description="O | Item #00705 | Table 0079 - LOCATION | LEN:12",
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
        description="O | Item #00775 | LEN:19",
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
        description="O | Item #00776 | LEN:19",
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
        description="O | Item #00777 | LEN:12",
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
        description="O | Item #00778 | LEN:12",
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
        description="O | Item #00779 | LEN:12",
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
        description="O | Item #00780 | LEN:12",
    )

    @field_validator("pv1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pv1_19", "pv1_26", "pv1_27", "pv1_32", "pv1_33", "pv1_46", "pv1_47", "pv1_48", "pv1_49", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("pv1_25", "pv1_30", "pv1_35", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
