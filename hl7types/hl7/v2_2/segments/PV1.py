"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PV1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PV1(HL7Model):
    """PATIENT VISIT (S3.3.3).

    Attributes
    ----------
    pv1_1 : str | None
        PV1.1 - Set ID - Patient Visit (SI) NA S3.3.3.1

    pv1_2 : str
        PV1.2 - Patient Class (ID) R S3.3.3.2 | 0004 - PATIENT CLASS

    pv1_3 : str | None
        PV1.3 - Assigned Patient Location (CM) NA S3.3.3.3 | 0079 - LOCATION

    pv1_4 : str | None
        PV1.4 - Admission Type (ID) NA S3.3.3.4 | 0007 - ADMISSION TYPE

    pv1_5 : str | None
        PV1.5 - Preadmit Number (ST) NA S3.3.3.5

    pv1_6 : str | None
        PV1.6 - Prior Patient Location (CM) NA S3.3.3.6

    pv1_7 : str | None
        PV1.7 - Attending Doctor (CN) NA S3.3.3.7 | 0010 - PHYSICIAN ID

    pv1_8 : str | None
        PV1.8 - Referring Doctor (CN) NA S3.3.3.8 | 0010 - PHYSICIAN ID

    pv1_9 : list[str] | None
        PV1.9 - Consulting Doctor (CN) NA rep S3.3.3.9 | 0010 - PHYSICIAN ID

    pv1_10 : str | None
        PV1.10 - Hospital Service (ID) NA S3.3.3.10 | 0069 - HOSPITAL SERVICE

    pv1_11 : str | None
        PV1.11 - Temporary Location (CM) NA S3.3.3.11 | 0079 - LOCATION

    pv1_12 : str | None
        PV1.12 - Preadmit Test Indicator (ID) NA S3.3.3.12 | 0087 - PRE-ADMIT TESTING

    pv1_13 : str | None
        PV1.13 - Readmission indicator (ID) NA S3.3.3.13 | 0092 - RE-ADMISSION INDICATOR

    pv1_14 : str | None
        PV1.14 - Admit Source (ID) NA S3.3.3.14 | 0023 - ADMIT SOURCE

    pv1_15 : list[str] | None
        PV1.15 - Ambulatory Status (ID) NA rep S3.3.3.15 | 0009 - AMBULATORY STATUS

    pv1_16 : str | None
        PV1.16 - VIP Indicator (ID) NA S3.3.3.16 | 0099 - VIP INDICATOR

    pv1_17 : str | None
        PV1.17 - Admitting Doctor (CN) NA S3.3.3.17 | 0010 - PHYSICIAN ID

    pv1_18 : str | None
        PV1.18 - Patient type (ID) NA S3.3.3.18 | 0018 - PATIENT TYPE

    pv1_19 : str | None
        PV1.19 - Visit Number (CM) NA S3.3.3.19

    pv1_20 : list[str] | None
        PV1.20 - Financial Class (CM) NA rep S3.3.3.20 | 0064 - FINANCIAL CLASS

    pv1_21 : str | None
        PV1.21 - Charge Price Indicator (ID) NA S3.3.3.21 | 0032 - CHARGE/PRICE INDICATOR

    pv1_22 : str | None
        PV1.22 - Courtesy Code (ID) NA S3.3.3.22 | 0045 - COURTESY CODE

    pv1_23 : str | None
        PV1.23 - Credit Rating (ID) NA S3.3.3.23 | 0046 - CREDIT RATING

    pv1_24 : list[str] | None
        PV1.24 - Contract Code (ID) NA rep S3.3.3.24 | 0044 - CONTRACT CODE

    pv1_25 : list[str] | None
        PV1.25 - Contract Effective Date (DT) NA rep S3.3.3.25

    pv1_26 : list[str] | None
        PV1.26 - Contract Amount (NM) NA rep S3.3.3.26

    pv1_27 : list[str] | None
        PV1.27 - Contract Period (NM) NA rep S3.3.3.27

    pv1_28 : str | None
        PV1.28 - Interest Code (ID) NA S3.3.3.28 | 0073 - INTEREST RATE CODE

    pv1_29 : str | None
        PV1.29 - Transfer to bad debt - code (ID) NA S3.3.3.29 | 0110 - TRANSFER TO BAD DEBT CODE

    pv1_30 : str | None
        PV1.30 - Transfer to bad debt - date (DT) NA S3.3.3.30

    pv1_31 : str | None
        PV1.31 - Bad Debt Agency Code (ID) NA S3.3.3.31 | 0021 - BAD DEBT AGENCY CODE

    pv1_32 : str | None
        PV1.32 - Bad Debt Transfer Amount (NM) NA S3.3.3.32

    pv1_33 : str | None
        PV1.33 - Bad Debt Recovery Amount (NM) NA S3.3.3.33

    pv1_34 : str | None
        PV1.34 - Delete Account Indicator (ID) NA S3.3.3.34 | 0111 - DELETE ACCOUNT CODE

    pv1_35 : str | None
        PV1.35 - Delete Account Date (DT) NA S3.3.3.35

    pv1_36 : str | None
        PV1.36 - Discharge Disposition (ID) NA S3.3.3.36 | 0112 - DISCHARGE DISPOSITION

    pv1_37 : str | None
        PV1.37 - Discharged to Location (CM) NA S3.3.3.37 | 0113 - DISCHARGED TO LOCATION

    pv1_38 : str | None
        PV1.38 - Diet Type (ID) NA S3.3.3.38 | 0114 - DIET TYPE

    pv1_39 : str | None
        PV1.39 - Servicing Facility (ID) NA S3.3.3.39 | 0115 - SERVICING FACILITY

    pv1_40 : str | None
        PV1.40 - Bed Status (ID) NA S3.3.7.2 | 0116 - BED STATUS

    pv1_41 : str | None
        PV1.41 - Account Status (ID) NA S3.3.3.41 | 0117 - ACCOUNT STATUS

    pv1_42 : str | None
        PV1.42 - Pending Location (CM) NA S3.3.3.42

    pv1_43 : str | None
        PV1.43 - Prior Temporary Location (CM) NA S3.3.3.43

    pv1_44 : TS | None
        PV1.44 - Admit date / time (TS) NA S3.3.3.44

    pv1_45 : TS | None
        PV1.45 - Discharge date / time (TS) NA S3.3.3.45

    pv1_46 : str | None
        PV1.46 - Current Patient Balance (NM) NA S3.3.3.46

    pv1_47 : str | None
        PV1.47 - Total Charges (NM) NA S3.3.3.47

    pv1_48 : str | None
        PV1.48 - Total Adjustments (NM) NA S3.3.3.48

    pv1_49 : str | None
        PV1.49 - Total Payments (NM) NA S3.3.3.49

    pv1_50 : str | None
        PV1.50 - Alternate Visit ID (CM) NA S3.3.3.50 | 0192 - Visit Id type
    """

    pv1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_1",
            "set_id_patient_visit",
            "PV1.1",
        ),
        serialization_alias="PV1.1",
        title="Set ID - Patient Visit",
        description="NA | Item #00131 | LEN:4",
    )

    pv1_2: str = Field(
        validation_alias=AliasChoices(
            "pv1_2",
            "patient_class",
            "PV1.2",
        ),
        serialization_alias="PV1.2",
        title="Patient Class",
        description="R | Item #00132 | Table 0004 - PATIENT CLASS | LEN:1",
    )

    pv1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_3",
            "assigned_patient_location",
            "PV1.3",
        ),
        serialization_alias="PV1.3",
        title="Assigned Patient Location",
        description="NA | Item #00133 | Table 0079 - LOCATION",
    )

    pv1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_4",
            "admission_type",
            "PV1.4",
        ),
        serialization_alias="PV1.4",
        title="Admission Type",
        description="NA | Item #00134 | Table 0007 - ADMISSION TYPE | LEN:2",
    )

    pv1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_5",
            "preadmit_number",
            "PV1.5",
        ),
        serialization_alias="PV1.5",
        title="Preadmit Number",
        description="NA | Item #00135 | LEN:20",
    )

    pv1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_6",
            "prior_patient_location",
            "PV1.6",
        ),
        serialization_alias="PV1.6",
        title="Prior Patient Location",
        description="NA | Item #00136",
    )

    pv1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_7",
            "attending_doctor",
            "PV1.7",
        ),
        serialization_alias="PV1.7",
        title="Attending Doctor",
        description="NA | Item #00137 | Table 0010 - PHYSICIAN ID",
    )

    pv1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_8",
            "referring_doctor",
            "PV1.8",
        ),
        serialization_alias="PV1.8",
        title="Referring Doctor",
        description="NA | Item #00138 | Table 0010 - PHYSICIAN ID",
    )

    pv1_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_9",
            "consulting_doctor",
            "PV1.9",
        ),
        serialization_alias="PV1.9",
        title="Consulting Doctor",
        description="NA | Item #00139 | Table 0010 - PHYSICIAN ID",
    )

    pv1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_10",
            "hospital_service",
            "PV1.10",
        ),
        serialization_alias="PV1.10",
        title="Hospital Service",
        description="NA | Item #00140 | Table 0069 - HOSPITAL SERVICE | LEN:3",
    )

    pv1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_11",
            "temporary_location",
            "PV1.11",
        ),
        serialization_alias="PV1.11",
        title="Temporary Location",
        description="NA | Item #00141 | Table 0079 - LOCATION",
    )

    pv1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_12",
            "preadmit_test_indicator",
            "PV1.12",
        ),
        serialization_alias="PV1.12",
        title="Preadmit Test Indicator",
        description="NA | Item #00142 | Table 0087 - PRE-ADMIT TESTING | LEN:2",
    )

    pv1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_13",
            "readmission_indicator",
            "PV1.13",
        ),
        serialization_alias="PV1.13",
        title="Readmission indicator",
        description=(
            "NA | Item #00143 | Table 0092 - RE-ADMISSION INDICATOR | LEN:2"
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
        title="Admit Source",
        description="NA | Item #00144 | Table 0023 - ADMIT SOURCE | LEN:3",
    )

    pv1_15: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_15",
            "ambulatory_status",
            "PV1.15",
        ),
        serialization_alias="PV1.15",
        title="Ambulatory Status",
        description="NA | Item #00145 | Table 0009 - AMBULATORY STATUS | LEN:2",
    )

    pv1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_16",
            "vip_indicator",
            "PV1.16",
        ),
        serialization_alias="PV1.16",
        title="VIP Indicator",
        description="NA | Item #00146 | Table 0099 - VIP INDICATOR | LEN:2",
    )

    pv1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_17",
            "admitting_doctor",
            "PV1.17",
        ),
        serialization_alias="PV1.17",
        title="Admitting Doctor",
        description="NA | Item #00147 | Table 0010 - PHYSICIAN ID",
    )

    pv1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_18",
            "patient_type",
            "PV1.18",
        ),
        serialization_alias="PV1.18",
        title="Patient type",
        description="NA | Item #00148 | Table 0018 - PATIENT TYPE | LEN:2",
    )

    pv1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_19",
            "visit_number",
            "PV1.19",
        ),
        serialization_alias="PV1.19",
        title="Visit Number",
        description="NA | Item #00149",
    )

    pv1_20: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_20",
            "financial_class",
            "PV1.20",
        ),
        serialization_alias="PV1.20",
        title="Financial Class",
        description="NA | Item #00150 | Table 0064 - FINANCIAL CLASS",
    )

    pv1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_21",
            "charge_price_indicator",
            "PV1.21",
        ),
        serialization_alias="PV1.21",
        title="Charge Price Indicator",
        description=(
            "NA | Item #00151 | Table 0032 - CHARGE/PRICE INDICATOR | LEN:2"
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
        title="Courtesy Code",
        description="NA | Item #00152 | Table 0045 - COURTESY CODE | LEN:2",
    )

    pv1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_23",
            "credit_rating",
            "PV1.23",
        ),
        serialization_alias="PV1.23",
        title="Credit Rating",
        description="NA | Item #00153 | Table 0046 - CREDIT RATING | LEN:2",
    )

    pv1_24: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_24",
            "contract_code",
            "PV1.24",
        ),
        serialization_alias="PV1.24",
        title="Contract Code",
        description="NA | Item #00154 | Table 0044 - CONTRACT CODE | LEN:2",
    )

    pv1_25: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_25",
            "contract_effective_date",
            "PV1.25",
        ),
        serialization_alias="PV1.25",
        title="Contract Effective Date",
        description="NA | Item #00155 | LEN:8",
    )

    pv1_26: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_26",
            "contract_amount",
            "PV1.26",
        ),
        serialization_alias="PV1.26",
        title="Contract Amount",
        description="NA | Item #00156 | LEN:12",
    )

    pv1_27: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_27",
            "contract_period",
            "PV1.27",
        ),
        serialization_alias="PV1.27",
        title="Contract Period",
        description="NA | Item #00157 | LEN:3",
    )

    pv1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_28",
            "interest_code",
            "PV1.28",
        ),
        serialization_alias="PV1.28",
        title="Interest Code",
        description=(
            "NA | Item #00158 | Table 0073 - INTEREST RATE CODE | LEN:2"
        ),
    )

    pv1_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_29",
            "transfer_to_bad_debt_code",
            "PV1.29",
        ),
        serialization_alias="PV1.29",
        title="Transfer to bad debt - code",
        description=(
            "NA | Item #00159 | Table 0110 - TRANSFER TO BAD DEBT CODE | LEN:1"
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
        title="Transfer to bad debt - date",
        description="NA | Item #00160 | LEN:8",
    )

    pv1_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_31",
            "bad_debt_agency_code",
            "PV1.31",
        ),
        serialization_alias="PV1.31",
        title="Bad Debt Agency Code",
        description=(
            "NA | Item #00161 | Table 0021 - BAD DEBT AGENCY CODE | LEN:10"
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
        title="Bad Debt Transfer Amount",
        description="NA | Item #00162 | LEN:12",
    )

    pv1_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_33",
            "bad_debt_recovery_amount",
            "PV1.33",
        ),
        serialization_alias="PV1.33",
        title="Bad Debt Recovery Amount",
        description="NA | Item #00163 | LEN:12",
    )

    pv1_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_34",
            "delete_account_indicator",
            "PV1.34",
        ),
        serialization_alias="PV1.34",
        title="Delete Account Indicator",
        description=(
            "NA | Item #00164 | Table 0111 - DELETE ACCOUNT CODE | LEN:1"
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
        title="Delete Account Date",
        description="NA | Item #00165 | LEN:8",
    )

    pv1_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_36",
            "discharge_disposition",
            "PV1.36",
        ),
        serialization_alias="PV1.36",
        title="Discharge Disposition",
        description=(
            "NA | Item #00166 | Table 0112 - DISCHARGE DISPOSITION | LEN:3"
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
        title="Discharged to Location",
        description="NA | Item #00167 | Table 0113 - DISCHARGED TO LOCATION",
    )

    pv1_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_38",
            "diet_type",
            "PV1.38",
        ),
        serialization_alias="PV1.38",
        title="Diet Type",
        description="NA | Item #00168 | Table 0114 - DIET TYPE | LEN:2",
    )

    pv1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_39",
            "servicing_facility",
            "PV1.39",
        ),
        serialization_alias="PV1.39",
        title="Servicing Facility",
        description=(
            "NA | Item #00169 | Table 0115 - SERVICING FACILITY | LEN:4"
        ),
    )

    pv1_40: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_40",
            "bed_status",
            "PV1.40",
        ),
        serialization_alias="PV1.40",
        title="Bed Status",
        description="NA | Item #00170 | Table 0116 - BED STATUS | LEN:1",
    )

    pv1_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_41",
            "account_status",
            "PV1.41",
        ),
        serialization_alias="PV1.41",
        title="Account Status",
        description="NA | Item #00171 | Table 0117 - ACCOUNT STATUS | LEN:2",
    )

    pv1_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_42",
            "pending_location",
            "PV1.42",
        ),
        serialization_alias="PV1.42",
        title="Pending Location",
        description="NA | Item #00172",
    )

    pv1_43: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_43",
            "prior_temporary_location",
            "PV1.43",
        ),
        serialization_alias="PV1.43",
        title="Prior Temporary Location",
        description="NA | Item #00173",
    )

    pv1_44: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_44",
            "admit_date_time",
            "PV1.44",
        ),
        serialization_alias="PV1.44",
        title="Admit date / time",
        description="NA | Item #00174",
    )

    pv1_45: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_45",
            "discharge_date_time",
            "PV1.45",
        ),
        serialization_alias="PV1.45",
        title="Discharge date / time",
        description="NA | Item #00175",
    )

    pv1_46: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_46",
            "current_patient_balance",
            "PV1.46",
        ),
        serialization_alias="PV1.46",
        title="Current Patient Balance",
        description="NA | Item #00176 | LEN:12",
    )

    pv1_47: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_47",
            "total_charges",
            "PV1.47",
        ),
        serialization_alias="PV1.47",
        title="Total Charges",
        description="NA | Item #00177 | LEN:12",
    )

    pv1_48: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_48",
            "total_adjustments",
            "PV1.48",
        ),
        serialization_alias="PV1.48",
        title="Total Adjustments",
        description="NA | Item #00178 | LEN:12",
    )

    pv1_49: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_49",
            "total_payments",
            "PV1.49",
        ),
        serialization_alias="PV1.49",
        title="Total Payments",
        description="NA | Item #00179 | LEN:12",
    )

    pv1_50: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_50",
            "alternate_visit_id",
            "PV1.50",
        ),
        serialization_alias="PV1.50",
        title="Alternate Visit ID",
        description="NA | Item #00180 | Table 0192 - Visit Id type",
    )

    @field_validator("pv1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pv1_25", "pv1_30", "pv1_35", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("pv1_26", "pv1_27", "pv1_32", "pv1_33", "pv1_46", "pv1_47", "pv1_48", "pv1_49", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
