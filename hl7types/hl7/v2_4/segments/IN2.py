"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: IN2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.DDI import DDI
from ..datatypes.JCC import JCC
from ..datatypes.PTA import PTA
from ..datatypes.RMC import RMC
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class IN2(HL7Model):
    """Insurance Additional Information (S6.5.7).

    Attributes
    ----------
    in2_1 : list[CX] | None
        IN2.1 - Insured's Employee ID (CX) O rep S6.5.7.1

    in2_2 : str | None
        IN2.2 - Insured's Social Security Number (ST) O S6.5.7.2

    in2_3 : list[XCN] | None
        IN2.3 - Insured's Employer's Name and ID (XCN) O rep S6.5.7.3

    in2_4 : str | None
        IN2.4 - Employer Information Data (IS) O S6.5.7.4 | 0139 - Employer information data

    in2_5 : list[str] | None
        IN2.5 - Mail Claim Party (IS) O rep S6.5.7.5 | 0137 - Mail claim party

    in2_6 : str | None
        IN2.6 - Medicare Health Ins Card Number (ST) O S6.5.7.6

    in2_7 : list[XPN] | None
        IN2.7 - Medicaid Case Name (XPN) O rep S6.5.7.7

    in2_8 : str | None
        IN2.8 - Medicaid Case Number (ST) O S6.5.7.8

    in2_9 : list[XPN] | None
        IN2.9 - Military Sponsor Name (XPN) O rep S6.5.7.9

    in2_10 : str | None
        IN2.10 - Military ID Number (ST) O S6.5.7.10

    in2_11 : CE | None
        IN2.11 - Dependent Of Military Recipient (CE) O S6.5.7.11 | 0342 - Military recipient

    in2_12 : str | None
        IN2.12 - Military Organization (ST) O S6.5.7.12

    in2_13 : str | None
        IN2.13 - Military Station (ST) O S6.5.7.13

    in2_14 : str | None
        IN2.14 - Military Service (IS) O S6.5.7.14 | 0140 - Military service

    in2_15 : str | None
        IN2.15 - Military Rank/Grade (IS) O S6.5.7.15 | 0141 - Military rank/grade

    in2_16 : str | None
        IN2.16 - Military Status (IS) O S6.5.7.16 | 0142 - Military status

    in2_17 : str | None
        IN2.17 - Military Retire Date (DT) O S6.5.7.17

    in2_18 : str | None
        IN2.18 - Military Non-Avail Cert On File (ID) O S6.5.7.18 | 0136 - Yes/no indicator

    in2_19 : str | None
        IN2.19 - Baby Coverage (ID) O S6.5.7.19 | 0136 - Yes/no indicator

    in2_20 : str | None
        IN2.20 - Combine Baby Bill (ID) O S6.5.7.20 | 0136 - Yes/no indicator

    in2_21 : str | None
        IN2.21 - Blood Deductible (ST) O S6.5.7.21

    in2_22 : list[XPN] | None
        IN2.22 - Special Coverage Approval Name (XPN) O rep S6.5.7.22

    in2_23 : str | None
        IN2.23 - Special Coverage Approval Title (ST) O S6.5.7.23

    in2_24 : list[str] | None
        IN2.24 - Non-Covered Insurance Code (IS) O rep S6.5.7.24 | 0143 - Non-covered insurance code

    in2_25 : list[CX] | None
        IN2.25 - Payor ID (CX) O rep S6.5.7.25

    in2_26 : list[CX] | None
        IN2.26 - Payor Subscriber ID (CX) O rep S6.5.7.26

    in2_27 : str | None
        IN2.27 - Eligibility Source (IS) O S6.5.7.27 | 0144 - Eligibility source

    in2_28 : list[RMC] | None
        IN2.28 - Room Coverage Type/Amount (RMC) O rep S6.5.7.28 | 0145 - Room type

    in2_29 : list[PTA] | None
        IN2.29 - Policy Type/Amount (PTA) O rep S6.5.7.29 | 0147 - Policy type

    in2_30 : DDI | None
        IN2.30 - Daily Deductible (DDI) O S6.5.7.30

    in2_31 : str | None
        IN2.31 - Living Dependency (IS) O S6.5.7.31 | 0223 - Living dependency

    in2_32 : list[str] | None
        IN2.32 - Ambulatory Status (IS) O rep S6.5.7.32 | 0009 - Ambulatory status

    in2_33 : list[CE] | None
        IN2.33 - Citizenship (CE) O rep S6.5.7.33 | 0171 - Citizenship

    in2_34 : CE | None
        IN2.34 - Primary Language (CE) O S6.5.7.34 | 0296 - Primary language

    in2_35 : str | None
        IN2.35 - Living Arrangement (IS) O S6.5.7.35 | 0220 - Living arrangement

    in2_36 : CE | None
        IN2.36 - Publicity Code (CE) O S6.5.7.36 | 0215 - Publicity code

    in2_37 : str | None
        IN2.37 - Protection Indicator (ID) O S6.5.7.37 | 0136 - Yes/no indicator

    in2_38 : str | None
        IN2.38 - Student Indicator (IS) O S6.5.7.38 | 0231 - Student status

    in2_39 : CE | None
        IN2.39 - Religion (CE) O S6.5.7.39 | 0006 - Religion

    in2_40 : list[XPN] | None
        IN2.40 - Mother's Maiden Name (XPN) O rep S6.5.7.40

    in2_41 : CE | None
        IN2.41 - Nationality (CE) O S6.5.7.41 | 0212 - Nationality

    in2_42 : list[CE] | None
        IN2.42 - Ethnic Group (CE) O rep S15.4.6.28 | 0189 - Ethnic group

    in2_43 : list[CE] | None
        IN2.43 - Marital Status (CE) O rep S15.4.6.17 | 0002 - Marital status

    in2_44 : str | None
        IN2.44 - Insured's Employment Start Date (DT) O S6.5.7.44

    in2_45 : str | None
        IN2.45 - Employment Stop Date (DT) O S6.5.7.45

    in2_46 : str | None
        IN2.46 - Job Title (ST) O S15.4.6.18

    in2_47 : JCC | None
        IN2.47 - Job Code/Class (JCC) O S15.4.6.19 | 0327 - Job code/class

    in2_48 : str | None
        IN2.48 - Job Status (IS) O S6.5.7.48 | 0311 - Job status

    in2_49 : list[XPN] | None
        IN2.49 - Employer Contact Person Name (XPN) O rep S6.5.7.49

    in2_50 : list[XTN] | None
        IN2.50 - Employer Contact Person Phone Number (XTN) O rep S6.5.7.50

    in2_51 : str | None
        IN2.51 - Employer Contact Reason (IS) O S6.5.7.51 | 0222 - Contact reason

    in2_52 : list[XPN] | None
        IN2.52 - Insured's Contact Person's Name (XPN) O rep S6.5.7.52

    in2_53 : list[XTN] | None
        IN2.53 - Insured's Contact Person Phone Number (XTN) O rep S6.5.7.53

    in2_54 : list[str] | None
        IN2.54 - Insured's Contact Person Reason (IS) O rep S6.5.7.54 | 0222 - Contact reason

    in2_55 : str | None
        IN2.55 - Relationship To The Patient Start Date (DT) O S6.5.7.55

    in2_56 : list[str] | None
        IN2.56 - Relationship To The Patient Stop Date (DT) O rep S6.5.7.56

    in2_57 : str | None
        IN2.57 - Insurance Co. Contact Reason (IS) O S6.5.7.57 | 0232 - Insurance company contact reason

    in2_58 : XTN | None
        IN2.58 - Insurance Co Contact Phone Number (XTN) O S6.5.7.58

    in2_59 : str | None
        IN2.59 - Policy Scope (IS) O S6.5.7.59 | 0312 - Policy scope

    in2_60 : str | None
        IN2.60 - Policy Source (IS) O S6.5.7.60 | 0313 - Policy source

    in2_61 : CX | None
        IN2.61 - Patient Member Number (CX) O S6.5.7.61

    in2_62 : CE | None
        IN2.62 - Guarantor's Relationship To Insured (CE) O S6.5.7.62 | 0063 - Relationship

    in2_63 : list[XTN] | None
        IN2.63 - Insured's Phone Number - Home (XTN) O rep S6.5.7.63

    in2_64 : list[XTN] | None
        IN2.64 - Insured's Employer Phone Number (XTN) O rep S6.5.7.64

    in2_65 : CE | None
        IN2.65 - Military Handicapped Program (CE) O S6.5.7.65 | 0343 - Military handicapped program code

    in2_66 : str | None
        IN2.66 - Suspend Flag (ID) O S6.5.7.66 | 0136 - Yes/no indicator

    in2_67 : str | None
        IN2.67 - Copay Limit Flag (ID) O S6.5.7.67 | 0136 - Yes/no indicator

    in2_68 : str | None
        IN2.68 - Stoploss Limit Flag (ID) O S6.5.7.68 | 0136 - Yes/no indicator

    in2_69 : list[XON] | None
        IN2.69 - Insured Organization Name And ID (XON) O rep S6.5.7.69

    in2_70 : list[XON] | None
        IN2.70 - Insured Employer Organization Name And ID (XON) O rep S6.5.7.70

    in2_71 : list[CE] | None
        IN2.71 - Race (CE) O rep S15.4.6.27 | 0005 - Race

    in2_72 : CE | None
        IN2.72 - HCFA Patient's Relationship to Insured (CE) O S6.5.7.72 | 0344 - Patient's relationship to insured
    """

    in2_1: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_1",
            "insured_s_employee_id",
            "IN2.1",
        ),
        serialization_alias="IN2.1",
        title="Insured's Employee ID",
        description="O | Item #00472",
    )

    in2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_2",
            "insured_s_social_security_number",
            "IN2.2",
        ),
        serialization_alias="IN2.2",
        title="Insured's Social Security Number",
        description="O | Item #00473 | LEN:11",
    )

    in2_3: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_3",
            "insured_s_employer_s_name_and_id",
            "IN2.3",
        ),
        serialization_alias="IN2.3",
        title="Insured's Employer's Name and ID",
        description="O | Item #00474",
    )

    in2_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_4",
            "employer_information_data",
            "IN2.4",
        ),
        serialization_alias="IN2.4",
        title="Employer Information Data",
        description=(
            "O | Item #00475 | Table 0139 - Employer information data | LEN:1"
        ),
    )

    in2_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_5",
            "mail_claim_party",
            "IN2.5",
        ),
        serialization_alias="IN2.5",
        title="Mail Claim Party",
        description="O | Item #00476 | Table 0137 - Mail claim party | LEN:1",
    )

    in2_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_6",
            "medicare_health_ins_card_number",
            "IN2.6",
        ),
        serialization_alias="IN2.6",
        title="Medicare Health Ins Card Number",
        description="O | Item #00477 | LEN:15",
    )

    in2_7: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_7",
            "medicaid_case_name",
            "IN2.7",
        ),
        serialization_alias="IN2.7",
        title="Medicaid Case Name",
        description="O | Item #00478",
    )

    in2_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_8",
            "medicaid_case_number",
            "IN2.8",
        ),
        serialization_alias="IN2.8",
        title="Medicaid Case Number",
        description="O | Item #00479 | LEN:15",
    )

    in2_9: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_9",
            "military_sponsor_name",
            "IN2.9",
        ),
        serialization_alias="IN2.9",
        title="Military Sponsor Name",
        description="O | Item #00480",
    )

    in2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_10",
            "military_id_number",
            "IN2.10",
        ),
        serialization_alias="IN2.10",
        title="Military ID Number",
        description="O | Item #00481 | LEN:20",
    )

    in2_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_11",
            "dependent_of_military_recipient",
            "IN2.11",
        ),
        serialization_alias="IN2.11",
        title="Dependent Of Military Recipient",
        description="O | Item #00482 | Table 0342 - Military recipient",
    )

    in2_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_12",
            "military_organization",
            "IN2.12",
        ),
        serialization_alias="IN2.12",
        title="Military Organization",
        description="O | Item #00483 | LEN:25",
    )

    in2_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_13",
            "military_station",
            "IN2.13",
        ),
        serialization_alias="IN2.13",
        title="Military Station",
        description="O | Item #00484 | LEN:25",
    )

    in2_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_14",
            "military_service",
            "IN2.14",
        ),
        serialization_alias="IN2.14",
        title="Military Service",
        description="O | Item #00485 | Table 0140 - Military service | LEN:14",
    )

    in2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_15",
            "military_rank_grade",
            "IN2.15",
        ),
        serialization_alias="IN2.15",
        title="Military Rank/Grade",
        description=(
            "O | Item #00486 | Table 0141 - Military rank/grade | LEN:2"
        ),
    )

    in2_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_16",
            "military_status",
            "IN2.16",
        ),
        serialization_alias="IN2.16",
        title="Military Status",
        description="O | Item #00487 | Table 0142 - Military status | LEN:3",
    )

    in2_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_17",
            "military_retire_date",
            "IN2.17",
        ),
        serialization_alias="IN2.17",
        title="Military Retire Date",
        description="O | Item #00488 | LEN:8",
    )

    in2_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_18",
            "military_non_avail_cert_on_file",
            "IN2.18",
        ),
        serialization_alias="IN2.18",
        title="Military Non-Avail Cert On File",
        description="O | Item #00489 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_19",
            "baby_coverage",
            "IN2.19",
        ),
        serialization_alias="IN2.19",
        title="Baby Coverage",
        description="O | Item #00490 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_20",
            "combine_baby_bill",
            "IN2.20",
        ),
        serialization_alias="IN2.20",
        title="Combine Baby Bill",
        description="O | Item #00491 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_21",
            "blood_deductible",
            "IN2.21",
        ),
        serialization_alias="IN2.21",
        title="Blood Deductible",
        description="O | Item #00492 | LEN:1",
    )

    in2_22: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_22",
            "special_coverage_approval_name",
            "IN2.22",
        ),
        serialization_alias="IN2.22",
        title="Special Coverage Approval Name",
        description="O | Item #00493",
    )

    in2_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_23",
            "special_coverage_approval_title",
            "IN2.23",
        ),
        serialization_alias="IN2.23",
        title="Special Coverage Approval Title",
        description="O | Item #00494 | LEN:30",
    )

    in2_24: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_24",
            "non_covered_insurance_code",
            "IN2.24",
        ),
        serialization_alias="IN2.24",
        title="Non-Covered Insurance Code",
        description=(
            "O | Item #00495 | Table 0143 - Non-covered insurance code | LEN:8"
        ),
    )

    in2_25: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_25",
            "payor_id",
            "IN2.25",
        ),
        serialization_alias="IN2.25",
        title="Payor ID",
        description="O | Item #00496",
    )

    in2_26: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_26",
            "payor_subscriber_id",
            "IN2.26",
        ),
        serialization_alias="IN2.26",
        title="Payor Subscriber ID",
        description="O | Item #00497",
    )

    in2_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_27",
            "eligibility_source",
            "IN2.27",
        ),
        serialization_alias="IN2.27",
        title="Eligibility Source",
        description="O | Item #00498 | Table 0144 - Eligibility source | LEN:1",
    )

    in2_28: Optional[List[RMC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_28",
            "room_coverage_type_amount",
            "IN2.28",
        ),
        serialization_alias="IN2.28",
        title="Room Coverage Type/Amount",
        description="O | Item #00499 | Table 0145 - Room type",
    )

    in2_29: Optional[List[PTA]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_29",
            "policy_type_amount",
            "IN2.29",
        ),
        serialization_alias="IN2.29",
        title="Policy Type/Amount",
        description="O | Item #00500 | Table 0147 - Policy type",
    )

    in2_30: Optional[DDI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_30",
            "daily_deductible",
            "IN2.30",
        ),
        serialization_alias="IN2.30",
        title="Daily Deductible",
        description="O | Item #00501",
    )

    in2_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_31",
            "living_dependency",
            "IN2.31",
        ),
        serialization_alias="IN2.31",
        title="Living Dependency",
        description="O | Item #00755 | Table 0223 - Living dependency | LEN:2",
    )

    in2_32: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_32",
            "ambulatory_status",
            "IN2.32",
        ),
        serialization_alias="IN2.32",
        title="Ambulatory Status",
        description="O | Item #00145 | Table 0009 - Ambulatory status | LEN:2",
    )

    in2_33: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_33",
            "citizenship",
            "IN2.33",
        ),
        serialization_alias="IN2.33",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Citizenship",
    )

    in2_34: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_34",
            "primary_language",
            "IN2.34",
        ),
        serialization_alias="IN2.34",
        title="Primary Language",
        description="O | Item #00118 | Table 0296 - Primary language",
    )

    in2_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_35",
            "living_arrangement",
            "IN2.35",
        ),
        serialization_alias="IN2.35",
        title="Living Arrangement",
        description="O | Item #00742 | Table 0220 - Living arrangement | LEN:2",
    )

    in2_36: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_36",
            "publicity_code",
            "IN2.36",
        ),
        serialization_alias="IN2.36",
        title="Publicity Code",
        description="O | Item #00743 | Table 0215 - Publicity code",
    )

    in2_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_37",
            "protection_indicator",
            "IN2.37",
        ),
        serialization_alias="IN2.37",
        title="Protection Indicator",
        description="O | Item #00744 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_38",
            "student_indicator",
            "IN2.38",
        ),
        serialization_alias="IN2.38",
        title="Student Indicator",
        description="O | Item #00745 | Table 0231 - Student status | LEN:2",
    )

    in2_39: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_39",
            "religion",
            "IN2.39",
        ),
        serialization_alias="IN2.39",
        title="Religion",
        description="O | Item #00120 | Table 0006 - Religion",
    )

    in2_40: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_40",
            "mother_s_maiden_name",
            "IN2.40",
        ),
        serialization_alias="IN2.40",
        title="Mother's Maiden Name",
        description="O | Item #00109",
    )

    in2_41: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_41",
            "nationality",
            "IN2.41",
        ),
        serialization_alias="IN2.41",
        title="Nationality",
        description="O | Item #00739 | Table 0212 - Nationality",
    )

    in2_42: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_42",
            "ethnic_group",
            "IN2.42",
        ),
        serialization_alias="IN2.42",
        title="Ethnic Group",
        description="O | Item #00125 | Table 0189 - Ethnic group",
    )

    in2_43: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_43",
            "marital_status",
            "IN2.43",
        ),
        serialization_alias="IN2.43",
        title="Marital Status",
        description="O | Item #00119 | Table 0002 - Marital status",
    )

    in2_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_44",
            "insured_s_employment_start_date",
            "IN2.44",
        ),
        serialization_alias="IN2.44",
        title="Insured's Employment Start Date",
        description="O | Item #00787 | LEN:8",
    )

    in2_45: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_45",
            "employment_stop_date",
            "IN2.45",
        ),
        serialization_alias="IN2.45",
        title="Employment Stop Date",
        description="O | Item #00783 | LEN:8",
    )

    in2_46: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_46",
            "job_title",
            "IN2.46",
        ),
        serialization_alias="IN2.46",
        title="Job Title",
        description="O | Item #00785 | LEN:20",
    )

    in2_47: Optional[JCC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_47",
            "job_code_class",
            "IN2.47",
        ),
        serialization_alias="IN2.47",
        title="Job Code/Class",
        description="O | Item #00786 | Table 0327 - Job code/class",
    )

    in2_48: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_48",
            "job_status",
            "IN2.48",
        ),
        serialization_alias="IN2.48",
        title="Job Status",
        description="O | Item #00752 | Table 0311 - Job status | LEN:2",
    )

    in2_49: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_49",
            "employer_contact_person_name",
            "IN2.49",
        ),
        serialization_alias="IN2.49",
        title="Employer Contact Person Name",
        description="O | Item #00789",
    )

    in2_50: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_50",
            "employer_contact_person_phone_number",
            "IN2.50",
        ),
        serialization_alias="IN2.50",
        title="Employer Contact Person Phone Number",
        description="O | Item #00790",
    )

    in2_51: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_51",
            "employer_contact_reason",
            "IN2.51",
        ),
        serialization_alias="IN2.51",
        title="Employer Contact Reason",
        description="O | Item #00791 | Table 0222 - Contact reason | LEN:2",
    )

    in2_52: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_52",
            "insured_s_contact_person_s_name",
            "IN2.52",
        ),
        serialization_alias="IN2.52",
        title="Insured's Contact Person's Name",
        description="O | Item #00792",
    )

    in2_53: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_53",
            "insured_s_contact_person_phone_number",
            "IN2.53",
        ),
        serialization_alias="IN2.53",
        title="Insured's Contact Person Phone Number",
        description="O | Item #00793",
    )

    in2_54: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_54",
            "insured_s_contact_person_reason",
            "IN2.54",
        ),
        serialization_alias="IN2.54",
        title="Insured's Contact Person Reason",
        description="O | Item #00794 | Table 0222 - Contact reason | LEN:2",
    )

    in2_55: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_55",
            "relationship_to_the_patient_start_date",
            "IN2.55",
        ),
        serialization_alias="IN2.55",
        title="Relationship To The Patient Start Date",
        description="O | Item #00795 | LEN:8",
    )

    in2_56: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_56",
            "relationship_to_the_patient_stop_date",
            "IN2.56",
        ),
        serialization_alias="IN2.56",
        title="Relationship To The Patient Stop Date",
        description="O | Item #00796 | LEN:8",
    )

    in2_57: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_57",
            "insurance_co_contact_reason",
            "IN2.57",
        ),
        serialization_alias="IN2.57",
        title="Insurance Co. Contact Reason",
        description=(
            "O | Item #00797 | Table 0232 - Insurance company contact reason | "
            "LEN:2"
        ),
    )

    in2_58: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_58",
            "insurance_co_contact_phone_number",
            "IN2.58",
        ),
        serialization_alias="IN2.58",
        title="Insurance Co Contact Phone Number",
        description="O | Item #00798",
    )

    in2_59: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_59",
            "policy_scope",
            "IN2.59",
        ),
        serialization_alias="IN2.59",
        title="Policy Scope",
        description="O | Item #00799 | Table 0312 - Policy scope | LEN:2",
    )

    in2_60: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_60",
            "policy_source",
            "IN2.60",
        ),
        serialization_alias="IN2.60",
        title="Policy Source",
        description="O | Item #00800 | Table 0313 - Policy source | LEN:2",
    )

    in2_61: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_61",
            "patient_member_number",
            "IN2.61",
        ),
        serialization_alias="IN2.61",
        title="Patient Member Number",
        description="O | Item #00801",
    )

    in2_62: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_62",
            "guarantor_s_relationship_to_insured",
            "IN2.62",
        ),
        serialization_alias="IN2.62",
        title="Guarantor's Relationship To Insured",
        description="O | Item #00802 | Table 0063 - Relationship",
    )

    in2_63: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_63",
            "insured_s_phone_number_home",
            "IN2.63",
        ),
        serialization_alias="IN2.63",
        title="Insured's Phone Number - Home",
        description="O | Item #00803",
    )

    in2_64: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_64",
            "insured_s_employer_phone_number",
            "IN2.64",
        ),
        serialization_alias="IN2.64",
        title="Insured's Employer Phone Number",
        description="O | Item #00804",
    )

    in2_65: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_65",
            "military_handicapped_program",
            "IN2.65",
        ),
        serialization_alias="IN2.65",
        title="Military Handicapped Program",
        description=(
            "O | Item #00805 | Table 0343 - Military handicapped program code"
        ),
    )

    in2_66: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_66",
            "suspend_flag",
            "IN2.66",
        ),
        serialization_alias="IN2.66",
        title="Suspend Flag",
        description="O | Item #00806 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_67: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_67",
            "copay_limit_flag",
            "IN2.67",
        ),
        serialization_alias="IN2.67",
        title="Copay Limit Flag",
        description="O | Item #00807 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_68: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_68",
            "stoploss_limit_flag",
            "IN2.68",
        ),
        serialization_alias="IN2.68",
        title="Stoploss Limit Flag",
        description="O | Item #00808 | Table 0136 - Yes/no indicator | LEN:1",
    )

    in2_69: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_69",
            "insured_organization_name_and_id",
            "IN2.69",
        ),
        serialization_alias="IN2.69",
        title="Insured Organization Name And ID",
        description="O | Item #00809",
    )

    in2_70: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_70",
            "insured_employer_organization_name_and_id",
            "IN2.70",
        ),
        serialization_alias="IN2.70",
        title="Insured Employer Organization Name And ID",
        description="O | Item #00810",
    )

    in2_71: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_71",
            "race",
            "IN2.71",
        ),
        serialization_alias="IN2.71",
        title="Race",
        description="O | Item #00113 | Table 0005 - Race",
    )

    in2_72: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_72",
            "hcfa_patient_s_relationship_to_insured",
            "IN2.72",
        ),
        serialization_alias="IN2.72",
        title="HCFA Patient's Relationship to Insured",
        description=(
            "O | Item #00811 | Table 0344 - Patient's relationship to insured"
        ),
    )

    @field_validator("in2_17", "in2_44", "in2_45", "in2_55", "in2_56", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
