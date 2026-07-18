"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PV1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DLD import DLD
from ..datatypes.FC import FC
from ..datatypes.PL import PL
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PV1(HL7Model):
    """Patient Visit (S3.4.3).

    Attributes
    ----------
    pv1_1 : str | None
        PV1.1 - Set ID - PV1 (SI) O S3.4.3.1

    pv1_2 : CWE
        PV1.2 - Patient Class (CWE) R S3.4.3.2 | 0004 - Patient Class

    pv1_3 : PL | None
        PV1.3 - Assigned Patient Location (PL) O S3.4.3.3

    pv1_4 : CWE | None
        PV1.4 - Admission Type (CWE) O S3.4.3.4 | 0007 - Admission Type

    pv1_5 : CX | None
        PV1.5 - Preadmit Number (CX) O S3.4.3.5

    pv1_6 : PL | None
        PV1.6 - Prior Patient Location (PL) O S3.4.3.6

    pv1_7 : list[XCN] | None
        PV1.7 - Attending Doctor (XCN) O rep S17.7.4.34 | 0010 - Physician ID

    pv1_8 : list[XCN] | None
        PV1.8 - Referring Doctor (XCN) O rep S3.4.3.8 | 0010 - Physician ID

    pv1_9 : list[XCN] | None
        PV1.9 - Consulting Doctor (XCN) O rep S3.4.3.9

    pv1_10 : CWE | None
        PV1.10 - Hospital Service (CWE) O S3.4.3.10 | 0069 - Hospital Service

    pv1_11 : PL | None
        PV1.11 - Temporary Location (PL) O S3.4.3.11

    pv1_12 : CWE | None
        PV1.12 - Preadmit Test Indicator (CWE) O S3.4.3.12 | 0087 - Pre-Admit Test Indicator

    pv1_13 : CWE | None
        PV1.13 - Re-admission Indicator (CWE) O S3.4.3.13 | 0092 - Re-Admission Indicator

    pv1_14 : CWE | None
        PV1.14 - Admit Source (CWE) O S3.4.3.14 | 0023 - Admit Source

    pv1_15 : list[CWE] | None
        PV1.15 - Ambulatory Status (CWE) O rep S3.4.3.15 | 0009 - Ambulatory Status

    pv1_16 : CWE | None
        PV1.16 - VIP Indicator (CWE) O S3.4.3.16 | 0099 - VIP Indicator

    pv1_17 : list[XCN] | None
        PV1.17 - Admitting Doctor (XCN) O rep S3.4.3.17 | 0010 - Physician ID

    pv1_18 : CWE | None
        PV1.18 - Patient Type (CWE) O S3.4.3.18 | 0018 - Patient Type

    pv1_19 : CX | None
        PV1.19 - Visit Number (CX) O S3.4.3.19

    pv1_20 : list[FC] | None
        PV1.20 - Financial Class (FC) O rep S3.4.3.20 | 0064 - Financial Class

    pv1_21 : CWE | None
        PV1.21 - Charge Price Indicator (CWE) O S3.4.3.21 | 0032 - Charge/Price Indicator

    pv1_22 : CWE | None
        PV1.22 - Courtesy Code (CWE) O S3.4.3.22 | 0045 - Courtesy Code

    pv1_23 : CWE | None
        PV1.23 - Credit Rating (CWE) O S3.4.3.23 | 0046 - Credit Rating

    pv1_24 : list[CWE] | None
        PV1.24 - Contract Code (CWE) O rep S3.4.3.24 | 0044 - Contract Code

    pv1_25 : list[str] | None
        PV1.25 - Contract Effective Date (DT) O rep S3.4.3.25

    pv1_26 : list[str] | None
        PV1.26 - Contract Amount (NM) O rep S3.4.3.26

    pv1_27 : list[str] | None
        PV1.27 - Contract Period (NM) O rep S3.4.3.27

    pv1_28 : CWE | None
        PV1.28 - Interest Code (CWE) O S3.4.3.28 | 0073 - Interest Rate Code

    pv1_29 : CWE | None
        PV1.29 - Transfer to Bad Debt Code (CWE) O S3.4.3.29 | 0110 - Transfer to Bad Debt Code

    pv1_30 : str | None
        PV1.30 - Transfer to Bad Debt Date (DT) O S3.4.3.30

    pv1_31 : CWE | None
        PV1.31 - Bad Debt Agency Code (CWE) O S3.4.3.31 | 0021 - Bad Debt Agency Code

    pv1_32 : str | None
        PV1.32 - Bad Debt Transfer Amount (NM) O S3.4.3.32

    pv1_33 : str | None
        PV1.33 - Bad Debt Recovery Amount (NM) O S3.4.3.33

    pv1_34 : CWE | None
        PV1.34 - Delete Account Indicator (CWE) O S3.4.3.34 | 0111 - Delete Account Code

    pv1_35 : str | None
        PV1.35 - Delete Account Date (DT) O S3.4.3.35

    pv1_36 : CWE | None
        PV1.36 - Discharge Disposition (CWE) O S3.4.3.36 | 0112 - Discharge Disposition

    pv1_37 : DLD | None
        PV1.37 - Discharged to Location (DLD) O S3.4.3.37 | 0113 - Discharged to Location

    pv1_38 : CWE | None
        PV1.38 - Diet Type (CWE) O S3.4.3.38 | 0114 - Diet Type

    pv1_39 : CWE | None
        PV1.39 - Servicing Facility (CWE) O S3.4.3.39 | 0115 - Servicing Facilities

    pv1_41 : CWE | None
        PV1.41 - Account Status (CWE) O S3.4.3.41 | 0117 - Account Status

    pv1_42 : PL | None
        PV1.42 - Pending Location (PL) O S3.4.3.42

    pv1_43 : PL | None
        PV1.43 - Prior Temporary Location (PL) O S3.4.3.43

    pv1_44 : str | None
        PV1.44 - Admit Date/Time (DTM) O S3.4.3.44

    pv1_45 : str | None
        PV1.45 - Discharge Date/Time (DTM) O S3.4.3.45

    pv1_46 : str | None
        PV1.46 - Current Patient Balance (NM) O S3.4.3.46

    pv1_47 : str | None
        PV1.47 - Total Charges (NM) O S3.4.3.47

    pv1_48 : str | None
        PV1.48 - Total Adjustments (NM) O S3.4.3.48

    pv1_49 : str | None
        PV1.49 - Total Payments (NM) O S3.4.3.49

    pv1_50 : list[CX] | None
        PV1.50 - Alternate Visit ID (CX) O rep S3.4.3.50 | 0203 - Identifier Type

    pv1_51 : CWE | None
        PV1.51 - Visit Indicator (CWE) O S3.4.3.51 | 0326 - Visit Indicator

    pv1_53 : str | None
        PV1.53 - Service Episode Description (ST) O S3.4.3.53

    pv1_54 : CX | None
        PV1.54 - Service Episode Identifier (CX) O S3.4.3.54
    """

    pv1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_1",
            "set_id_pv1",
            "PV1.1",
        ),
        serialization_alias="PV1.1",
        title="Set ID - PV1",
        description="O | Item #00131 | LEN:4",
    )

    pv1_2: CWE = Field(
        validation_alias=AliasChoices(
            "pv1_2",
            "patient_class",
            "PV1.2",
        ),
        serialization_alias="PV1.2",
        title="Patient Class",
        description="R | Item #00132 | Table 0004 - Patient Class",
    )

    pv1_3: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_3",
            "assigned_patient_location",
            "PV1.3",
        ),
        serialization_alias="PV1.3",
        title="Assigned Patient Location",
        description="O | Item #00133",
    )

    pv1_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_4",
            "admission_type",
            "PV1.4",
        ),
        serialization_alias="PV1.4",
        title="Admission Type",
        description="O | Item #00134 | Table 0007 - Admission Type",
    )

    pv1_5: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_5",
            "preadmit_number",
            "PV1.5",
        ),
        serialization_alias="PV1.5",
        title="Preadmit Number",
        description="O | Item #00135",
    )

    pv1_6: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_6",
            "prior_patient_location",
            "PV1.6",
        ),
        serialization_alias="PV1.6",
        title="Prior Patient Location",
        description="O | Item #00136",
    )

    pv1_7: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_7",
            "attending_doctor",
            "PV1.7",
        ),
        serialization_alias="PV1.7",
        title="Attending Doctor",
        description="O | Item #00137 | Table 0010 - Physician ID",
    )

    pv1_8: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_8",
            "referring_doctor",
            "PV1.8",
        ),
        serialization_alias="PV1.8",
        title="Referring Doctor",
        description="O | Item #00138 | Table 0010 - Physician ID",
    )

    pv1_9: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_9",
            "consulting_doctor",
            "PV1.9",
        ),
        serialization_alias="PV1.9",
        title="Consulting Doctor",
        description="O | Item #00139",
    )

    pv1_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_10",
            "hospital_service",
            "PV1.10",
        ),
        serialization_alias="PV1.10",
        title="Hospital Service",
        description="O | Item #00140 | Table 0069 - Hospital Service",
    )

    pv1_11: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_11",
            "temporary_location",
            "PV1.11",
        ),
        serialization_alias="PV1.11",
        title="Temporary Location",
        description="O | Item #00141",
    )

    pv1_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_12",
            "preadmit_test_indicator",
            "PV1.12",
        ),
        serialization_alias="PV1.12",
        title="Preadmit Test Indicator",
        description="O | Item #00142 | Table 0087 - Pre-Admit Test Indicator",
    )

    pv1_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_13",
            "re_admission_indicator",
            "PV1.13",
        ),
        serialization_alias="PV1.13",
        title="Re-admission Indicator",
        description="O | Item #00143 | Table 0092 - Re-Admission Indicator",
    )

    pv1_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_14",
            "admit_source",
            "PV1.14",
        ),
        serialization_alias="PV1.14",
        title="Admit Source",
        description="O | Item #00144 | Table 0023 - Admit Source",
    )

    pv1_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_15",
            "ambulatory_status",
            "PV1.15",
        ),
        serialization_alias="PV1.15",
        title="Ambulatory Status",
        description="O | Item #00145 | Table 0009 - Ambulatory Status",
    )

    pv1_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_16",
            "vip_indicator",
            "PV1.16",
        ),
        serialization_alias="PV1.16",
        title="VIP Indicator",
        description="O | Item #00146 | Table 0099 - VIP Indicator",
    )

    pv1_17: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_17",
            "admitting_doctor",
            "PV1.17",
        ),
        serialization_alias="PV1.17",
        title="Admitting Doctor",
        description="O | Item #00147 | Table 0010 - Physician ID",
    )

    pv1_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_18",
            "patient_type",
            "PV1.18",
        ),
        serialization_alias="PV1.18",
        title="Patient Type",
        description="O | Item #00148 | Table 0018 - Patient Type",
    )

    pv1_19: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_19",
            "visit_number",
            "PV1.19",
        ),
        serialization_alias="PV1.19",
        title="Visit Number",
        description="O | Item #00149",
    )

    pv1_20: Optional[List[FC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_20",
            "financial_class",
            "PV1.20",
        ),
        serialization_alias="PV1.20",
        title="Financial Class",
        description="O | Item #00150 | Table 0064 - Financial Class",
    )

    pv1_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_21",
            "charge_price_indicator",
            "PV1.21",
        ),
        serialization_alias="PV1.21",
        title="Charge Price Indicator",
        description="O | Item #00151 | Table 0032 - Charge/Price Indicator",
    )

    pv1_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_22",
            "courtesy_code",
            "PV1.22",
        ),
        serialization_alias="PV1.22",
        title="Courtesy Code",
        description="O | Item #00152 | Table 0045 - Courtesy Code",
    )

    pv1_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_23",
            "credit_rating",
            "PV1.23",
        ),
        serialization_alias="PV1.23",
        title="Credit Rating",
        description="O | Item #00153 | Table 0046 - Credit Rating",
    )

    pv1_24: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_24",
            "contract_code",
            "PV1.24",
        ),
        serialization_alias="PV1.24",
        title="Contract Code",
        description="O | Item #00154 | Table 0044 - Contract Code",
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
        description="O | Item #00155",
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
        description="O | Item #00156",
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
        description="O | Item #00157",
    )

    pv1_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_28",
            "interest_code",
            "PV1.28",
        ),
        serialization_alias="PV1.28",
        title="Interest Code",
        description="O | Item #00158 | Table 0073 - Interest Rate Code",
    )

    pv1_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_29",
            "transfer_to_bad_debt_code",
            "PV1.29",
        ),
        serialization_alias="PV1.29",
        title="Transfer to Bad Debt Code",
        description="O | Item #00159 | Table 0110 - Transfer to Bad Debt Code",
    )

    pv1_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_30",
            "transfer_to_bad_debt_date",
            "PV1.30",
        ),
        serialization_alias="PV1.30",
        title="Transfer to Bad Debt Date",
        description="O | Item #00160",
    )

    pv1_31: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_31",
            "bad_debt_agency_code",
            "PV1.31",
        ),
        serialization_alias="PV1.31",
        title="Bad Debt Agency Code",
        description="O | Item #00161 | Table 0021 - Bad Debt Agency Code",
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
        description="O | Item #00162",
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
        description="O | Item #00163",
    )

    pv1_34: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_34",
            "delete_account_indicator",
            "PV1.34",
        ),
        serialization_alias="PV1.34",
        title="Delete Account Indicator",
        description="O | Item #00164 | Table 0111 - Delete Account Code",
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
        description="O | Item #00165",
    )

    pv1_36: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_36",
            "discharge_disposition",
            "PV1.36",
        ),
        serialization_alias="PV1.36",
        title="Discharge Disposition",
        description="O | Item #00166 | Table 0112 - Discharge Disposition",
    )

    pv1_37: Optional[DLD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_37",
            "discharged_to_location",
            "PV1.37",
        ),
        serialization_alias="PV1.37",
        title="Discharged to Location",
        description="O | Item #00167 | Table 0113 - Discharged to Location",
    )

    pv1_38: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_38",
            "diet_type",
            "PV1.38",
        ),
        serialization_alias="PV1.38",
        title="Diet Type",
        description="O | Item #00168 | Table 0114 - Diet Type",
    )

    pv1_39: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_39",
            "servicing_facility",
            "PV1.39",
        ),
        serialization_alias="PV1.39",
        title="Servicing Facility",
        description="O | Item #00169 | Table 0115 - Servicing Facilities",
    )

    pv1_41: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_41",
            "account_status",
            "PV1.41",
        ),
        serialization_alias="PV1.41",
        title="Account Status",
        description="O | Item #00171 | Table 0117 - Account Status",
    )

    pv1_42: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_42",
            "pending_location",
            "PV1.42",
        ),
        serialization_alias="PV1.42",
        title="Pending Location",
        description="O | Item #00172",
    )

    pv1_43: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_43",
            "prior_temporary_location",
            "PV1.43",
        ),
        serialization_alias="PV1.43",
        title="Prior Temporary Location",
        description="O | Item #00173",
    )

    pv1_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_44",
            "admit_date_time",
            "PV1.44",
        ),
        serialization_alias="PV1.44",
        title="Admit Date/Time",
        description="O | Item #00174",
    )

    pv1_45: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_45",
            "discharge_date_time",
            "PV1.45",
        ),
        serialization_alias="PV1.45",
        title="Discharge Date/Time",
        description="O | Item #00175",
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
        description="O | Item #00176",
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
        description="O | Item #00177",
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
        description="O | Item #00178",
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
        description="O | Item #00179",
    )

    pv1_50: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_50",
            "alternate_visit_id",
            "PV1.50",
        ),
        serialization_alias="PV1.50",
        title="Alternate Visit ID",
        description="O | Item #00180 | Table 0203 - Identifier Type",
    )

    pv1_51: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_51",
            "visit_indicator",
            "PV1.51",
        ),
        serialization_alias="PV1.51",
        title="Visit Indicator",
        description="O | Item #01226 | Table 0326 - Visit Indicator",
    )

    pv1_53: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_53",
            "service_episode_description",
            "PV1.53",
        ),
        serialization_alias="PV1.53",
        title="Service Episode Description",
        description="O | Item #02290",
    )

    pv1_54: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_54",
            "service_episode_identifier",
            "PV1.54",
        ),
        serialization_alias="PV1.54",
        title="Service Episode Identifier",
        description="O | Item #02291",
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

    @field_validator("pv1_44", "pv1_45", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
