"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: GT1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.FC import FC
from ..datatypes.JCC import JCC
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class GT1(BaseModel):
    """HL7 v2 GT1 segment."""

    gt1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_gt1",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="Set ID - GT1",
        description="Item #405",
    )

    gt1_2: list[CX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_2",
            "guarantor_number",
            "GT1.2",
        ),
        serialization_alias="GT1.2",
        title="Guarantor Number",
        description="Item #406",
    )

    gt1_3: list[XPN] = Field(
        default=...,
        validation_alias=AliasChoices(
            "gt1_3",
            "guarantor_name",
            "GT1.3",
        ),
        serialization_alias="GT1.3",
        title="Guarantor Name",
        description="Item #407",
    )

    gt1_4: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_4",
            "guarantor_spouse_name",
            "GT1.4",
        ),
        serialization_alias="GT1.4",
        title="Guarantor Spouse Name",
        description="Item #408",
    )

    gt1_5: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_5",
            "guarantor_address",
            "GT1.5",
        ),
        serialization_alias="GT1.5",
        title="Guarantor Address",
        description="Item #409",
    )

    gt1_6: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_6",
            "guarantor_ph_num_home",
            "GT1.6",
        ),
        serialization_alias="GT1.6",
        title="Guarantor Ph Num - Home",
        description="Item #410",
    )

    gt1_7: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_7",
            "guarantor_ph_num_business",
            "GT1.7",
        ),
        serialization_alias="GT1.7",
        title="Guarantor Ph Num - Business",
        description="Item #411",
    )

    gt1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_8",
            "guarantor_date_time_of_birth",
            "GT1.8",
        ),
        serialization_alias="GT1.8",
        title="Guarantor Date/Time Of Birth",
        description="Item #412",
    )

    gt1_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_9",
            "guarantor_administrative_sex",
            "GT1.9",
        ),
        serialization_alias="GT1.9",
        title="Guarantor Administrative Sex",
        description="Item #413 | Table HL70001",
    )

    gt1_10: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_10",
            "guarantor_type",
            "GT1.10",
        ),
        serialization_alias="GT1.10",
        title="Guarantor Type",
        description="Item #414 | Table HL70068",
    )

    gt1_11: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_11",
            "guarantor_relationship",
            "GT1.11",
        ),
        serialization_alias="GT1.11",
        title="Guarantor Relationship",
        description="Item #415 | Table HL70063",
    )

    gt1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_12",
            "guarantor_ssn",
            "GT1.12",
        ),
        serialization_alias="GT1.12",
        title="Guarantor SSN",
        description="Item #416",
    )

    gt1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_13",
            "guarantor_date_begin",
            "GT1.13",
        ),
        serialization_alias="GT1.13",
        title="Guarantor Date - Begin",
        description="Item #417",
    )

    gt1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_14",
            "guarantor_date_end",
            "GT1.14",
        ),
        serialization_alias="GT1.14",
        title="Guarantor Date - End",
        description="Item #418",
    )

    gt1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_15",
            "guarantor_priority",
            "GT1.15",
        ),
        serialization_alias="GT1.15",
        title="Guarantor Priority",
        description="Item #419",
    )

    gt1_16: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_16",
            "guarantor_employer_name",
            "GT1.16",
        ),
        serialization_alias="GT1.16",
        title="Guarantor Employer Name",
        description="Item #420",
    )

    gt1_17: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_17",
            "guarantor_employer_address",
            "GT1.17",
        ),
        serialization_alias="GT1.17",
        title="Guarantor Employer Address",
        description="Item #421",
    )

    gt1_18: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_18",
            "guarantor_employer_phone_number",
            "GT1.18",
        ),
        serialization_alias="GT1.18",
        title="Guarantor Employer Phone Number",
        description="Item #422",
    )

    gt1_19: list[CX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_19",
            "guarantor_employee_id_number",
            "GT1.19",
        ),
        serialization_alias="GT1.19",
        title="Guarantor Employee ID Number",
        description="Item #423",
    )

    gt1_20: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_20",
            "guarantor_employment_status",
            "GT1.20",
        ),
        serialization_alias="GT1.20",
        title="Guarantor Employment Status",
        description="Item #424 | Table HL70066",
    )

    gt1_21: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_21",
            "guarantor_organization_name",
            "GT1.21",
        ),
        serialization_alias="GT1.21",
        title="Guarantor Organization Name",
        description="Item #425",
    )

    gt1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_22",
            "guarantor_billing_hold_flag",
            "GT1.22",
        ),
        serialization_alias="GT1.22",
        title="Guarantor Billing Hold Flag",
        description="Item #773 | Table HL70136",
    )

    gt1_23: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_23",
            "guarantor_credit_rating_code",
            "GT1.23",
        ),
        serialization_alias="GT1.23",
        title="Guarantor Credit Rating Code",
        description="Item #774 | Table HL70341",
    )

    gt1_24: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_24",
            "guarantor_death_date_and_time",
            "GT1.24",
        ),
        serialization_alias="GT1.24",
        title="Guarantor Death Date And Time",
        description="Item #775",
    )

    gt1_25: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_25",
            "guarantor_death_flag",
            "GT1.25",
        ),
        serialization_alias="GT1.25",
        title="Guarantor Death Flag",
        description="Item #776 | Table HL70136",
    )

    gt1_26: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_26",
            "guarantor_charge_adjustment_code",
            "GT1.26",
        ),
        serialization_alias="GT1.26",
        title="Guarantor Charge Adjustment Code",
        description="Item #777 | Table HL70218",
    )

    gt1_27: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_27",
            "guarantor_household_annual_income",
            "GT1.27",
        ),
        serialization_alias="GT1.27",
        title="Guarantor Household Annual Income",
        description="Item #778",
    )

    gt1_28: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_28",
            "guarantor_household_size",
            "GT1.28",
        ),
        serialization_alias="GT1.28",
        title="Guarantor Household Size",
        description="Item #779",
    )

    gt1_29: list[CX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_29",
            "guarantor_employer_id_number",
            "GT1.29",
        ),
        serialization_alias="GT1.29",
        title="Guarantor Employer ID Number",
        description="Item #780",
    )

    gt1_30: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_30",
            "guarantor_marital_status_code",
            "GT1.30",
        ),
        serialization_alias="GT1.30",
        title="Guarantor Marital Status Code",
        description="Item #781 | Table HL70002",
    )

    gt1_31: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_31",
            "guarantor_hire_effective_date",
            "GT1.31",
        ),
        serialization_alias="GT1.31",
        title="Guarantor Hire Effective Date",
        description="Item #782",
    )

    gt1_32: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_32",
            "employment_stop_date",
            "GT1.32",
        ),
        serialization_alias="GT1.32",
        title="Employment Stop Date",
        description="Item #783",
    )

    gt1_33: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_33",
            "living_dependency",
            "GT1.33",
        ),
        serialization_alias="GT1.33",
        title="Living Dependency",
        description="Item #755 | Table HL70223",
    )

    gt1_34: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_34",
            "ambulatory_status",
            "GT1.34",
        ),
        serialization_alias="GT1.34",
        title="Ambulatory Status",
        description="Item #145 | Table HL70009",
    )

    gt1_35: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_35",
            "citizenship",
            "GT1.35",
        ),
        serialization_alias="GT1.35",
        title="Citizenship",
        description="Item #129 | Table HL70171",
    )

    gt1_36: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_36",
            "primary_language",
            "GT1.36",
        ),
        serialization_alias="GT1.36",
        title="Primary Language",
        description="Item #118 | Table HL70296",
    )

    gt1_37: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_37",
            "living_arrangement",
            "GT1.37",
        ),
        serialization_alias="GT1.37",
        title="Living Arrangement",
        description="Item #742 | Table HL70220",
    )

    gt1_38: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_38",
            "publicity_code",
            "GT1.38",
        ),
        serialization_alias="GT1.38",
        title="Publicity Code",
        description="Item #743 | Table HL70215",
    )

    gt1_39: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_39",
            "protection_indicator",
            "GT1.39",
        ),
        serialization_alias="GT1.39",
        title="Protection Indicator",
        description="Item #744 | Table HL70136",
    )

    gt1_40: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_40",
            "student_indicator",
            "GT1.40",
        ),
        serialization_alias="GT1.40",
        title="Student Indicator",
        description="Item #745 | Table HL70231",
    )

    gt1_41: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_41",
            "religion",
            "GT1.41",
        ),
        serialization_alias="GT1.41",
        title="Religion",
        description="Item #120 | Table HL70006",
    )

    gt1_42: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_42",
            "mother_s_maiden_name",
            "GT1.42",
        ),
        serialization_alias="GT1.42",
        title="Mother's Maiden Name",
        description="Item #109",
    )

    gt1_43: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_43",
            "nationality",
            "GT1.43",
        ),
        serialization_alias="GT1.43",
        title="Nationality",
        description="Item #739 | Table HL70212",
    )

    gt1_44: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_44",
            "ethnic_group",
            "GT1.44",
        ),
        serialization_alias="GT1.44",
        title="Ethnic Group",
        description="Item #125 | Table HL70189",
    )

    gt1_45: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_45",
            "contact_person_s_name",
            "GT1.45",
        ),
        serialization_alias="GT1.45",
        title="Contact Person's Name",
        description="Item #748 | Table HL70200",
    )

    gt1_46: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_46",
            "contact_person_s_telephone_number",
            "GT1.46",
        ),
        serialization_alias="GT1.46",
        title="Contact Person's Telephone Number",
        description="Item #749",
    )

    gt1_47: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_47",
            "contact_reason",
            "GT1.47",
        ),
        serialization_alias="GT1.47",
        title="Contact Reason",
        description="Item #747 | Table HL70222",
    )

    gt1_48: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_48",
            "contact_relationship",
            "GT1.48",
        ),
        serialization_alias="GT1.48",
        title="Contact Relationship",
        description="Item #784 | Table HL70063",
    )

    gt1_49: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_49",
            "job_title",
            "GT1.49",
        ),
        serialization_alias="GT1.49",
        title="Job Title",
        description="Item #785",
    )

    gt1_50: JCC | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_50",
            "job_code_class",
            "GT1.50",
        ),
        serialization_alias="GT1.50",
        title="Job Code/Class",
        description="Item #786 | Table HL70327",
    )

    gt1_51: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_51",
            "guarantor_employer_s_organization_name",
            "GT1.51",
        ),
        serialization_alias="GT1.51",
        title="Guarantor Employer's Organization Name",
        description="Item #1299",
    )

    gt1_52: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_52",
            "handicap",
            "GT1.52",
        ),
        serialization_alias="GT1.52",
        title="Handicap",
        description="Item #753 | Table HL70295",
    )

    gt1_53: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_53",
            "job_status",
            "GT1.53",
        ),
        serialization_alias="GT1.53",
        title="Job Status",
        description="Item #752 | Table HL70311",
    )

    gt1_54: FC | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_54",
            "guarantor_financial_class",
            "GT1.54",
        ),
        serialization_alias="GT1.54",
        title="Guarantor Financial Class",
        description="Item #1231",
    )

    gt1_55: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_55",
            "guarantor_race",
            "GT1.55",
        ),
        serialization_alias="GT1.55",
        title="Guarantor Race",
        description="Item #1291 | Table HL70005",
    )

    gt1_56: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_56",
            "guarantor_birth_place",
            "GT1.56",
        ),
        serialization_alias="GT1.56",
        title="Guarantor Birth Place",
        description="Item #1851",
    )

    gt1_57: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_57",
            "vip_indicator",
            "GT1.57",
        ),
        serialization_alias="GT1.57",
        title="VIP Indicator",
        description="Item #146 | Table HL70099",
    )

    model_config = {"populate_by_name": True}
