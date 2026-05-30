"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PV1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.DLD import DLD
from ..datatypes.FC import FC
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class PV1(HL7Model):
    """HL7 v2 PV1 segment.

    Attributes
    ----------
    pv1_1 : str | None
        PV1.1 (opt) - Set ID - PV1 (SI)

    pv1_2 : str
        PV1.2 (req) - Patient Class (IS)

    pv1_3 : PL | None
        PV1.3 (opt) - Assigned Patient Location (PL)

    pv1_4 : str | None
        PV1.4 (opt) - Admission Type (IS)

    pv1_5 : CX | None
        PV1.5 (opt) - Preadmit Number (CX)

    pv1_6 : PL | None
        PV1.6 (opt) - Prior Patient Location (PL)

    pv1_7 : list[XCN] | None
        PV1.7 (opt, rep) - Attending Doctor (XCN)

    pv1_8 : list[XCN] | None
        PV1.8 (opt, rep) - Referring Doctor (XCN)

    pv1_9 : list[XCN] | None
        PV1.9 (opt, rep) - Consulting Doctor (XCN)

    pv1_10 : str | None
        PV1.10 (opt) - Hospital Service (IS)

    pv1_11 : PL | None
        PV1.11 (opt) - Temporary Location (PL)

    pv1_12 : str | None
        PV1.12 (opt) - Preadmit Test Indicator (IS)

    pv1_13 : str | None
        PV1.13 (opt) - Re-admission Indicator (IS)

    pv1_14 : str | None
        PV1.14 (opt) - Admit Source (IS)

    pv1_15 : list[str] | None
        PV1.15 (opt, rep) - Ambulatory Status (IS)

    pv1_16 : str | None
        PV1.16 (opt) - VIP Indicator (IS)

    pv1_17 : list[XCN] | None
        PV1.17 (opt, rep) - Admitting Doctor (XCN)

    pv1_18 : str | None
        PV1.18 (opt) - Patient Type (IS)

    pv1_19 : CX | None
        PV1.19 (opt) - Visit Number (CX)

    pv1_20 : list[FC] | None
        PV1.20 (opt, rep) - Financial Class (FC)

    pv1_21 : str | None
        PV1.21 (opt) - Charge Price Indicator (IS)

    pv1_22 : str | None
        PV1.22 (opt) - Courtesy Code (IS)

    pv1_23 : str | None
        PV1.23 (opt) - Credit Rating (IS)

    pv1_24 : list[str] | None
        PV1.24 (opt, rep) - Contract Code (IS)

    pv1_25 : list[str] | None
        PV1.25 (opt, rep) - Contract Effective Date (DT)

    pv1_26 : list[str] | None
        PV1.26 (opt, rep) - Contract Amount (NM)

    pv1_27 : list[str] | None
        PV1.27 (opt, rep) - Contract Period (NM)

    pv1_28 : str | None
        PV1.28 (opt) - Interest Code (IS)

    pv1_29 : str | None
        PV1.29 (opt) - Transfer to Bad Debt Code (IS)

    pv1_30 : str | None
        PV1.30 (opt) - Transfer to Bad Debt Date (DT)

    pv1_31 : str | None
        PV1.31 (opt) - Bad Debt Agency Code (IS)

    pv1_32 : str | None
        PV1.32 (opt) - Bad Debt Transfer Amount (NM)

    pv1_33 : str | None
        PV1.33 (opt) - Bad Debt Recovery Amount (NM)

    pv1_34 : str | None
        PV1.34 (opt) - Delete Account Indicator (IS)

    pv1_35 : str | None
        PV1.35 (opt) - Delete Account Date (DT)

    pv1_36 : str | None
        PV1.36 (opt) - Discharge Disposition (IS)

    pv1_37 : DLD | None
        PV1.37 (opt) - Discharged to Location (DLD)

    pv1_38 : CE | None
        PV1.38 (opt) - Diet Type (CE)

    pv1_39 : str | None
        PV1.39 (opt) - Servicing Facility (IS)

    pv1_40 : str | None
        PV1.40 (opt) - Bed Status (IS)

    pv1_41 : str | None
        PV1.41 (opt) - Account Status (IS)

    pv1_42 : PL | None
        PV1.42 (opt) - Pending Location (PL)

    pv1_43 : PL | None
        PV1.43 (opt) - Prior Temporary Location (PL)

    pv1_44 : TS | None
        PV1.44 (opt) - Admit Date/Time (TS)

    pv1_45 : list[TS] | None
        PV1.45 (opt, rep) - Discharge Date/Time (TS)

    pv1_46 : str | None
        PV1.46 (opt) - Current Patient Balance (NM)

    pv1_47 : str | None
        PV1.47 (opt) - Total Charges (NM)

    pv1_48 : str | None
        PV1.48 (opt) - Total Adjustments (NM)

    pv1_49 : str | None
        PV1.49 (opt) - Total Payments (NM)

    pv1_50 : CX | None
        PV1.50 (opt) - Alternate Visit ID (CX)

    pv1_51 : str | None
        PV1.51 (opt) - Visit Indicator (IS)

    pv1_52 : list[XCN] | None
        PV1.52 (opt, rep) - Other Healthcare Provider (XCN)
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
        description="Item #131",
    )

    pv1_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pv1_2",
            "patient_class",
            "PV1.2",
        ),
        serialization_alias="PV1.2",
        title="Patient Class",
        description="Item #132 | Table HL70004",
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
        description="Item #133",
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
        description="Item #134 | Table HL70007",
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
        description="Item #135",
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
        description="Item #136",
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
        description="Item #137 | Table HL70010",
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
        description="Item #138 | Table HL70010",
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
        description="Item #139 | Table HL70010",
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
        description="Item #140 | Table HL70069",
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
        description="Item #141",
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
        description="Item #142 | Table HL70087",
    )

    pv1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_13",
            "re_admission_indicator",
            "PV1.13",
        ),
        serialization_alias="PV1.13",
        title="Re-admission Indicator",
        description="Item #143 | Table HL70092",
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
        description="Item #144 | Table HL70023",
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
        description="Item #145 | Table HL70009",
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
        description="Item #146 | Table HL70099",
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
        description="Item #147 | Table HL70010",
    )

    pv1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_18",
            "patient_type",
            "PV1.18",
        ),
        serialization_alias="PV1.18",
        title="Patient Type",
        description="Item #148 | Table HL70018",
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
        description="Item #149",
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
        description="Item #150 | Table HL70064",
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
        description="Item #151 | Table HL70032",
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
        description="Item #152 | Table HL70045",
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
        description="Item #153 | Table HL70046",
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
        description="Item #154 | Table HL70044",
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
        description="Item #155",
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
        description="Item #156",
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
        description="Item #157",
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
        description="Item #158 | Table HL70073",
    )

    pv1_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_29",
            "transfer_to_bad_debt_code",
            "PV1.29",
        ),
        serialization_alias="PV1.29",
        title="Transfer to Bad Debt Code",
        description="Item #159 | Table HL70110",
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
        description="Item #160",
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
        description="Item #161 | Table HL70021",
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
        description="Item #162",
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
        description="Item #163",
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
        description="Item #164 | Table HL70111",
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
        description="Item #165",
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
        description="Item #166 | Table HL70112",
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
        description="Item #167 | Table HL70113",
    )

    pv1_38: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_38",
            "diet_type",
            "PV1.38",
        ),
        serialization_alias="PV1.38",
        title="Diet Type",
        description="Item #168 | Table HL70114",
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
        description="Item #169 | Table HL70115",
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
        description="Item #170 | Table HL70116",
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
        description="Item #171 | Table HL70117",
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
        description="Item #172",
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
        description="Item #173",
    )

    pv1_44: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_44",
            "admit_date_time",
            "PV1.44",
        ),
        serialization_alias="PV1.44",
        title="Admit Date/Time",
        description="Item #174",
    )

    pv1_45: Optional[List[TS]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_45",
            "discharge_date_time",
            "PV1.45",
        ),
        serialization_alias="PV1.45",
        title="Discharge Date/Time",
        description="Item #175",
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
        description="Item #176",
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
        description="Item #177",
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
        description="Item #178",
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
        description="Item #179",
    )

    pv1_50: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_50",
            "alternate_visit_id",
            "PV1.50",
        ),
        serialization_alias="PV1.50",
        title="Alternate Visit ID",
        description="Item #180 | Table HL70203",
    )

    pv1_51: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_51",
            "visit_indicator",
            "PV1.51",
        ),
        serialization_alias="PV1.51",
        title="Visit Indicator",
        description="Item #1226 | Table HL70326",
    )

    pv1_52: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv1_52",
            "other_healthcare_provider",
            "PV1.52",
        ),
        serialization_alias="PV1.52",
        title="Other Healthcare Provider",
        description="Item #1274 | Table HL70010",
    )

    model_config = {"populate_by_name": True}
