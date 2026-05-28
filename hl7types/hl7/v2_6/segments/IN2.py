"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: IN2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DDI import DDI
from ..datatypes.JCC import JCC
from ..datatypes.PTA import PTA
from ..datatypes.RMC import RMC
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class IN2(BaseModel):
    """HL7 v2 IN2 segment."""

    in2_1: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_1",
            "insured_s_employee_id",
            "IN2.1",
        ),
        serialization_alias="IN2.1",
        title="Insured's Employee ID",
        description="Item #472",
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
        description="Item #473",
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
        description="Item #474",
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
        description="Item #475 | Table HL70139",
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
        description="Item #476 | Table HL70137",
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
        description="Item #477",
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
        description="Item #478",
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
        description="Item #479",
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
        description="Item #480",
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
        description="Item #481",
    )

    in2_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_11",
            "dependent_of_military_recipient",
            "IN2.11",
        ),
        serialization_alias="IN2.11",
        title="Dependent Of Military Recipient",
        description="Item #482 | Table HL70342",
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
        description="Item #483",
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
        description="Item #484",
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
        description="Item #485 | Table HL70140",
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
        description="Item #486 | Table HL70141",
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
        description="Item #487 | Table HL70142",
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
        description="Item #488",
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
        description="Item #489 | Table HL70136",
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
        description="Item #490 | Table HL70136",
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
        description="Item #491 | Table HL70136",
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
        description="Item #492",
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
        description="Item #493",
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
        description="Item #494",
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
        description="Item #495 | Table HL70143",
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
        description="Item #496",
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
        description="Item #497",
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
        description="Item #498 | Table HL70144",
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
        description="Item #499",
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
        description="Item #500",
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
        description="Item #501",
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
        description="Item #755 | Table HL70223",
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
        description="Item #145 | Table HL70009",
    )

    in2_33: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_33",
            "citizenship",
            "IN2.33",
        ),
        serialization_alias="IN2.33",
        title="Citizenship",
        description="Item #129 | Table HL70171",
    )

    in2_34: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_34",
            "primary_language",
            "IN2.34",
        ),
        serialization_alias="IN2.34",
        title="Primary Language",
        description="Item #118 | Table HL70296",
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
        description="Item #742 | Table HL70220",
    )

    in2_36: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_36",
            "publicity_code",
            "IN2.36",
        ),
        serialization_alias="IN2.36",
        title="Publicity Code",
        description="Item #743 | Table HL70215",
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
        description="Item #744 | Table HL70136",
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
        description="Item #745 | Table HL70231",
    )

    in2_39: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_39",
            "religion",
            "IN2.39",
        ),
        serialization_alias="IN2.39",
        title="Religion",
        description="Item #120 | Table HL70006",
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
        description="Item #109",
    )

    in2_41: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_41",
            "nationality",
            "IN2.41",
        ),
        serialization_alias="IN2.41",
        title="Nationality",
        description="Item #739 | Table HL70212",
    )

    in2_42: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_42",
            "ethnic_group",
            "IN2.42",
        ),
        serialization_alias="IN2.42",
        title="Ethnic Group",
        description="Item #125 | Table HL70189",
    )

    in2_43: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_43",
            "marital_status",
            "IN2.43",
        ),
        serialization_alias="IN2.43",
        title="Marital Status",
        description="Item #119 | Table HL70002",
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
        description="Item #787",
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
        description="Item #783",
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
        description="Item #785",
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
        description="Item #786",
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
        description="Item #752 | Table HL70311",
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
        description="Item #789",
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
        description="Item #790",
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
        description="Item #791 | Table HL70222",
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
        description="Item #792",
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
        description="Item #793",
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
        description="Item #794 | Table HL70222",
    )

    in2_55: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_55",
            "relationship_to_the_patient_start_date",
            "IN2.55",
        ),
        serialization_alias="IN2.55",
        title="Relationship to the Patient Start Date",
        description="Item #795",
    )

    in2_56: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_56",
            "relationship_to_the_patient_stop_date",
            "IN2.56",
        ),
        serialization_alias="IN2.56",
        title="Relationship to the Patient Stop Date",
        description="Item #796",
    )

    in2_57: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_57",
            "insurance_co_contact_reason",
            "IN2.57",
        ),
        serialization_alias="IN2.57",
        title="Insurance Co Contact Reason",
        description="Item #797 | Table HL70232",
    )

    in2_58: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_58",
            "insurance_co_contact_phone_number",
            "IN2.58",
        ),
        serialization_alias="IN2.58",
        title="Insurance Co Contact Phone Number",
        description="Item #798",
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
        description="Item #799 | Table HL70312",
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
        description="Item #800 | Table HL70313",
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
        description="Item #801",
    )

    in2_62: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_62",
            "guarantor_s_relationship_to_insured",
            "IN2.62",
        ),
        serialization_alias="IN2.62",
        title="Guarantor's Relationship to Insured",
        description="Item #802 | Table HL70063",
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
        description="Item #803",
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
        description="Item #804",
    )

    in2_65: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_65",
            "military_handicapped_program",
            "IN2.65",
        ),
        serialization_alias="IN2.65",
        title="Military Handicapped Program",
        description="Item #805 | Table HL70343",
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
        description="Item #806 | Table HL70136",
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
        description="Item #807 | Table HL70136",
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
        description="Item #808 | Table HL70136",
    )

    in2_69: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_69",
            "insured_organization_name_and_id",
            "IN2.69",
        ),
        serialization_alias="IN2.69",
        title="Insured Organization Name and ID",
        description="Item #809",
    )

    in2_70: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_70",
            "insured_employer_organization_name_and_id",
            "IN2.70",
        ),
        serialization_alias="IN2.70",
        title="Insured Employer Organization Name and ID",
        description="Item #810",
    )

    in2_71: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_71",
            "race",
            "IN2.71",
        ),
        serialization_alias="IN2.71",
        title="Race",
        description="Item #113 | Table HL70005",
    )

    in2_72: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_72",
            "patient_s_relationship_to_insured",
            "IN2.72",
        ),
        serialization_alias="IN2.72",
        title="Patient's Relationship to Insured",
        description="Item #811 | Table HL70344",
    )

    model_config = {"populate_by_name": True}
