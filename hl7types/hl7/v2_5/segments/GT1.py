"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: GT1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.CX import CX
from ..datatypes.FC import FC
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class GT1(HL7Model):
    """Guarantor (S6.5.5).

    Attributes
    ----------
    gt1_1 : str
        GT1.1 - Set ID - GT1 (SI) R S6.5.5.1

    gt1_2 : list[CX] | None
        GT1.2 - Guarantor Number (CX) O rep S6.5.5.2

    gt1_3 : list[XPN]
        GT1.3 - Guarantor Name (XPN) R rep S6.5.5.3

    gt1_4 : list[XPN] | None
        GT1.4 - Guarantor Spouse Name (XPN) O rep S6.5.5.4

    gt1_5 : list[XAD] | None
        GT1.5 - Guarantor Address (XAD) O rep S6.5.5.5

    gt1_6 : list[XTN] | None
        GT1.6 - Guarantor Ph Num - Home (XTN) O rep S6.5.5.6

    gt1_7 : list[XTN] | None
        GT1.7 - Guarantor Ph Num - Business (XTN) O rep S6.5.5.7

    gt1_8 : TS | None
        GT1.8 - Guarantor Date/Time Of Birth (TS) O S6.5.5.8

    gt1_9 : str | None
        GT1.9 - Guarantor Administrative Sex (IS) O S6.5.5.9 | 0001 - Administrative Sex

    gt1_10 : str | None
        GT1.10 - Guarantor Type (IS) O S6.5.5.10 | 0068 - Guarantor Type

    gt1_11 : CE | None
        GT1.11 - Guarantor Relationship (CE) O S6.5.5.11 | 0063 - Relationship

    gt1_12 : str | None
        GT1.12 - Guarantor SSN (ST) O S6.5.5.12

    gt1_13 : str | None
        GT1.13 - Guarantor Date - Begin (DT) O S6.5.5.13

    gt1_14 : str | None
        GT1.14 - Guarantor Date - End (DT) O S6.5.5.14

    gt1_15 : str | None
        GT1.15 - Guarantor Priority (NM) O S6.5.5.15

    gt1_16 : list[XPN] | None
        GT1.16 - Guarantor Employer Name (XPN) O rep S6.5.5.16

    gt1_17 : list[XAD] | None
        GT1.17 - Guarantor Employer Address (XAD) O rep S6.5.5.17

    gt1_18 : list[XTN] | None
        GT1.18 - Guarantor Employer Phone Number (XTN) O rep S6.5.5.18

    gt1_19 : list[CX] | None
        GT1.19 - Guarantor Employee ID Number (CX) O rep S6.5.5.19

    gt1_20 : str | None
        GT1.20 - Guarantor Employment Status (IS) O S6.5.5.20 | 0066 - Employment Status

    gt1_21 : list[XON] | None
        GT1.21 - Guarantor Organization Name (XON) O rep S6.5.5.21

    gt1_22 : str | None
        GT1.22 - Guarantor Billing Hold Flag (ID) O S6.5.5.22 | 0136 - Yes/no indicator

    gt1_23 : CE | None
        GT1.23 - Guarantor Credit Rating Code (CE) O S6.5.5.23 | 0341 - Guarantor Credit Rating Code

    gt1_24 : TS | None
        GT1.24 - Guarantor Death Date And Time (TS) O S6.5.5.24

    gt1_25 : str | None
        GT1.25 - Guarantor Death Flag (ID) O S6.5.5.25 | 0136 - Yes/no indicator

    gt1_26 : CE | None
        GT1.26 - Guarantor Charge Adjustment Code (CE) O S6.5.5.26 | 0218 - Patient Charge Adjustment

    gt1_27 : CP | None
        GT1.27 - Guarantor Household Annual Income (CP) O S6.5.5.27

    gt1_28 : str | None
        GT1.28 - Guarantor Household Size (NM) O S6.5.5.28

    gt1_29 : list[CX] | None
        GT1.29 - Guarantor Employer ID Number (CX) O rep S6.5.5.29

    gt1_30 : CE | None
        GT1.30 - Guarantor Marital Status Code (CE) O S6.5.5.30 | 0002 - Marital Status

    gt1_31 : str | None
        GT1.31 - Guarantor Hire Effective Date (DT) O S6.5.5.31

    gt1_32 : str | None
        GT1.32 - Employment Stop Date (DT) O S6.5.5.32

    gt1_33 : str | None
        GT1.33 - Living Dependency (IS) O S3.4.5.17 | 0223 - Living Dependency

    gt1_34 : list[str] | None
        GT1.34 - Ambulatory Status (IS) O rep S3.4.3.15 | 0009 - Ambulatory Status

    gt1_35 : list[CE] | None
        GT1.35 - Citizenship (CE) O rep S3.4.2.26 | 0171 - Citizenship

    gt1_36 : CE | None
        GT1.36 - Primary Language (CE) O S3.4.2.15 | 0296 - Primary Language

    gt1_37 : str | None
        GT1.37 - Living Arrangement (IS) O S3.4.5.21 | 0220 - Living Arrangement

    gt1_38 : CE | None
        GT1.38 - Publicity Code (CE) O S3.4.5.22 | 0215 - Publicity Code

    gt1_39 : str | None
        GT1.39 - Protection Indicator (ID) O S3.4.5.23 | 0136 - Yes/no indicator

    gt1_40 : str | None
        GT1.40 - Student Indicator (IS) O S3.4.5.24 | 0231 - Student Status

    gt1_41 : CE | None
        GT1.41 - Religion (CE) O S3.4.2.17 | 0006 - Religion

    gt1_42 : list[XPN] | None
        GT1.42 - Mother's Maiden Name (XPN) O rep S3.4.2.6

    gt1_43 : CE | None
        GT1.43 - Nationality (CE) O S3.4.2.28 | 0212 - Nationality

    gt1_44 : list[CE] | None
        GT1.44 - Ethnic Group (CE) O rep S3.4.2.22 | 0189 - Ethnic Group

    gt1_45 : list[XPN] | None
        GT1.45 - Contact Person's Name (XPN) O rep S3.4.5.30

    gt1_46 : list[XTN] | None
        GT1.46 - Contact Person's Telephone Number (XTN) O rep S3.4.5.31

    gt1_47 : CE | None
        GT1.47 - Contact Reason (CE) O S3.4.5.29 | 0222 - Contact Reason

    gt1_48 : str | None
        GT1.48 - Contact Relationship (IS) O S6.5.5.48 | 0063 - Relationship

    gt1_49 : str | None
        GT1.49 - Job Title (ST) O S6.5.5.49

    gt1_50 : JCC | None
        GT1.50 - Job Code/Class (JCC) O S6.5.5.50

    gt1_51 : list[XON] | None
        GT1.51 - Guarantor Employer's Organization Name (XON) O rep S6.5.5.51

    gt1_52 : str | None
        GT1.52 - Handicap (IS) O S3.4.5.36 | 0295 - Handicap

    gt1_53 : str | None
        GT1.53 - Job Status (IS) O S3.4.5.34 | 0311 - Job Status

    gt1_54 : FC | None
        GT1.54 - Guarantor Financial Class (FC) O S6.5.5.54

    gt1_55 : list[CE] | None
        GT1.55 - Guarantor Race (CE) O rep S6.5.5.55 | 0005 - Race

    gt1_56 : str | None
        GT1.56 - Guarantor Birth Place (ST) O S6.5.5.56

    gt1_57 : str | None
        GT1.57 - VIP Indicator (IS) O S3.4.3.16 | 0099 - VIP Indicator
    """

    gt1_1: str = Field(
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_gt1",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="Set ID - GT1",
        description="R | Item #00405 | LEN:4",
    )

    gt1_2: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_2",
            "guarantor_number",
            "GT1.2",
        ),
        serialization_alias="GT1.2",
        title="Guarantor Number",
        description="O | Item #00406",
    )

    gt1_3: List[XPN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "gt1_3",
            "guarantor_name",
            "GT1.3",
        ),
        serialization_alias="GT1.3",
        title="Guarantor Name",
        description="R | Item #00407",
    )

    gt1_4: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_4",
            "guarantor_spouse_name",
            "GT1.4",
        ),
        serialization_alias="GT1.4",
        title="Guarantor Spouse Name",
        description="O | Item #00408",
    )

    gt1_5: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_5",
            "guarantor_address",
            "GT1.5",
        ),
        serialization_alias="GT1.5",
        title="Guarantor Address",
        description="O | Item #00409",
    )

    gt1_6: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_6",
            "guarantor_ph_num_home",
            "GT1.6",
        ),
        serialization_alias="GT1.6",
        title="Guarantor Ph Num - Home",
        description="O | Item #00410",
    )

    gt1_7: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_7",
            "guarantor_ph_num_business",
            "GT1.7",
        ),
        serialization_alias="GT1.7",
        title="Guarantor Ph Num - Business",
        description="O | Item #00411",
    )

    gt1_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_8",
            "guarantor_date_time_of_birth",
            "GT1.8",
        ),
        serialization_alias="GT1.8",
        title="Guarantor Date/Time Of Birth",
        description="O | Item #00412",
    )

    gt1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_9",
            "guarantor_administrative_sex",
            "GT1.9",
        ),
        serialization_alias="GT1.9",
        title="Guarantor Administrative Sex",
        description="O | Item #00413 | Table 0001 - Administrative Sex | LEN:1",
    )

    gt1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_10",
            "guarantor_type",
            "GT1.10",
        ),
        serialization_alias="GT1.10",
        title="Guarantor Type",
        description="O | Item #00414 | Table 0068 - Guarantor Type | LEN:2",
    )

    gt1_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_11",
            "guarantor_relationship",
            "GT1.11",
        ),
        serialization_alias="GT1.11",
        title="Guarantor Relationship",
        description="O | Item #00415 | Table 0063 - Relationship",
    )

    gt1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_12",
            "guarantor_ssn",
            "GT1.12",
        ),
        serialization_alias="GT1.12",
        title="Guarantor SSN",
        description="O | Item #00416 | LEN:11",
    )

    gt1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_13",
            "guarantor_date_begin",
            "GT1.13",
        ),
        serialization_alias="GT1.13",
        title="Guarantor Date - Begin",
        description="O | Item #00417 | LEN:8",
    )

    gt1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_14",
            "guarantor_date_end",
            "GT1.14",
        ),
        serialization_alias="GT1.14",
        title="Guarantor Date - End",
        description="O | Item #00418 | LEN:8",
    )

    gt1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_15",
            "guarantor_priority",
            "GT1.15",
        ),
        serialization_alias="GT1.15",
        title="Guarantor Priority",
        description="O | Item #00419 | LEN:2",
    )

    gt1_16: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_16",
            "guarantor_employer_name",
            "GT1.16",
        ),
        serialization_alias="GT1.16",
        title="Guarantor Employer Name",
        description="O | Item #00420",
    )

    gt1_17: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_17",
            "guarantor_employer_address",
            "GT1.17",
        ),
        serialization_alias="GT1.17",
        title="Guarantor Employer Address",
        description="O | Item #00421",
    )

    gt1_18: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_18",
            "guarantor_employer_phone_number",
            "GT1.18",
        ),
        serialization_alias="GT1.18",
        title="Guarantor Employer Phone Number",
        description="O | Item #00422",
    )

    gt1_19: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_19",
            "guarantor_employee_id_number",
            "GT1.19",
        ),
        serialization_alias="GT1.19",
        title="Guarantor Employee ID Number",
        description="O | Item #00423",
    )

    gt1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_20",
            "guarantor_employment_status",
            "GT1.20",
        ),
        serialization_alias="GT1.20",
        title="Guarantor Employment Status",
        description="O | Item #00424 | Table 0066 - Employment Status | LEN:2",
    )

    gt1_21: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_21",
            "guarantor_organization_name",
            "GT1.21",
        ),
        serialization_alias="GT1.21",
        title="Guarantor Organization Name",
        description="O | Item #00425",
    )

    gt1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_22",
            "guarantor_billing_hold_flag",
            "GT1.22",
        ),
        serialization_alias="GT1.22",
        title="Guarantor Billing Hold Flag",
        description="O | Item #00773 | Table 0136 - Yes/no indicator | LEN:1",
    )

    gt1_23: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_23",
            "guarantor_credit_rating_code",
            "GT1.23",
        ),
        serialization_alias="GT1.23",
        title="Guarantor Credit Rating Code",
        description=(
            "O | Item #00774 | Table 0341 - Guarantor Credit Rating Code"
        ),
    )

    gt1_24: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_24",
            "guarantor_death_date_and_time",
            "GT1.24",
        ),
        serialization_alias="GT1.24",
        title="Guarantor Death Date And Time",
        description="O | Item #00775",
    )

    gt1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_25",
            "guarantor_death_flag",
            "GT1.25",
        ),
        serialization_alias="GT1.25",
        title="Guarantor Death Flag",
        description="O | Item #00776 | Table 0136 - Yes/no indicator | LEN:1",
    )

    gt1_26: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_26",
            "guarantor_charge_adjustment_code",
            "GT1.26",
        ),
        serialization_alias="GT1.26",
        title="Guarantor Charge Adjustment Code",
        description="O | Item #00777 | Table 0218 - Patient Charge Adjustment",
    )

    gt1_27: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_27",
            "guarantor_household_annual_income",
            "GT1.27",
        ),
        serialization_alias="GT1.27",
        title="Guarantor Household Annual Income",
        description="O | Item #00778",
    )

    gt1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_28",
            "guarantor_household_size",
            "GT1.28",
        ),
        serialization_alias="GT1.28",
        title="Guarantor Household Size",
        description="O | Item #00779 | LEN:3",
    )

    gt1_29: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_29",
            "guarantor_employer_id_number",
            "GT1.29",
        ),
        serialization_alias="GT1.29",
        title="Guarantor Employer ID Number",
        description="O | Item #00780",
    )

    gt1_30: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_30",
            "guarantor_marital_status_code",
            "GT1.30",
        ),
        serialization_alias="GT1.30",
        title="Guarantor Marital Status Code",
        description="O | Item #00781 | Table 0002 - Marital Status",
    )

    gt1_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_31",
            "guarantor_hire_effective_date",
            "GT1.31",
        ),
        serialization_alias="GT1.31",
        title="Guarantor Hire Effective Date",
        description="O | Item #00782 | LEN:8",
    )

    gt1_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_32",
            "employment_stop_date",
            "GT1.32",
        ),
        serialization_alias="GT1.32",
        title="Employment Stop Date",
        description="O | Item #00783 | LEN:8",
    )

    gt1_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_33",
            "living_dependency",
            "GT1.33",
        ),
        serialization_alias="GT1.33",
        title="Living Dependency",
        description="O | Item #00755 | Table 0223 - Living Dependency | LEN:2",
    )

    gt1_34: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_34",
            "ambulatory_status",
            "GT1.34",
        ),
        serialization_alias="GT1.34",
        title="Ambulatory Status",
        description="O | Item #00145 | Table 0009 - Ambulatory Status | LEN:2",
    )

    gt1_35: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_35",
            "citizenship",
            "GT1.35",
        ),
        serialization_alias="GT1.35",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Citizenship",
    )

    gt1_36: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_36",
            "primary_language",
            "GT1.36",
        ),
        serialization_alias="GT1.36",
        title="Primary Language",
        description="O | Item #00118 | Table 0296 - Primary Language",
    )

    gt1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_37",
            "living_arrangement",
            "GT1.37",
        ),
        serialization_alias="GT1.37",
        title="Living Arrangement",
        description="O | Item #00742 | Table 0220 - Living Arrangement | LEN:2",
    )

    gt1_38: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_38",
            "publicity_code",
            "GT1.38",
        ),
        serialization_alias="GT1.38",
        title="Publicity Code",
        description="O | Item #00743 | Table 0215 - Publicity Code",
    )

    gt1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_39",
            "protection_indicator",
            "GT1.39",
        ),
        serialization_alias="GT1.39",
        title="Protection Indicator",
        description="O | Item #00744 | Table 0136 - Yes/no indicator | LEN:1",
    )

    gt1_40: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_40",
            "student_indicator",
            "GT1.40",
        ),
        serialization_alias="GT1.40",
        title="Student Indicator",
        description="O | Item #00745 | Table 0231 - Student Status | LEN:2",
    )

    gt1_41: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_41",
            "religion",
            "GT1.41",
        ),
        serialization_alias="GT1.41",
        title="Religion",
        description="O | Item #00120 | Table 0006 - Religion",
    )

    gt1_42: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_42",
            "mother_s_maiden_name",
            "GT1.42",
        ),
        serialization_alias="GT1.42",
        title="Mother's Maiden Name",
        description="O | Item #00109",
    )

    gt1_43: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_43",
            "nationality",
            "GT1.43",
        ),
        serialization_alias="GT1.43",
        title="Nationality",
        description="O | Item #00739 | Table 0212 - Nationality",
    )

    gt1_44: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_44",
            "ethnic_group",
            "GT1.44",
        ),
        serialization_alias="GT1.44",
        title="Ethnic Group",
        description="O | Item #00125 | Table 0189 - Ethnic Group",
    )

    gt1_45: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_45",
            "contact_person_s_name",
            "GT1.45",
        ),
        serialization_alias="GT1.45",
        title="Contact Person's Name",
        description="O | Item #00748",
    )

    gt1_46: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_46",
            "contact_person_s_telephone_number",
            "GT1.46",
        ),
        serialization_alias="GT1.46",
        title="Contact Person's Telephone Number",
        description="O | Item #00749",
    )

    gt1_47: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_47",
            "contact_reason",
            "GT1.47",
        ),
        serialization_alias="GT1.47",
        title="Contact Reason",
        description="O | Item #00747 | Table 0222 - Contact Reason",
    )

    gt1_48: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_48",
            "contact_relationship",
            "GT1.48",
        ),
        serialization_alias="GT1.48",
        title="Contact Relationship",
        description="O | Item #00784 | Table 0063 - Relationship | LEN:3",
    )

    gt1_49: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_49",
            "job_title",
            "GT1.49",
        ),
        serialization_alias="GT1.49",
        title="Job Title",
        description="O | Item #00785 | LEN:20",
    )

    gt1_50: Optional[JCC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_50",
            "job_code_class",
            "GT1.50",
        ),
        serialization_alias="GT1.50",
        title="Job Code/Class",
        description="O | Item #00786",
    )

    gt1_51: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_51",
            "guarantor_employer_s_organization_name",
            "GT1.51",
        ),
        serialization_alias="GT1.51",
        title="Guarantor Employer's Organization Name",
        description="O | Item #01299",
    )

    gt1_52: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_52",
            "handicap",
            "GT1.52",
        ),
        serialization_alias="GT1.52",
        title="Handicap",
        description="O | Item #00753 | Table 0295 - Handicap | LEN:2",
    )

    gt1_53: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_53",
            "job_status",
            "GT1.53",
        ),
        serialization_alias="GT1.53",
        title="Job Status",
        description="O | Item #00752 | Table 0311 - Job Status | LEN:2",
    )

    gt1_54: Optional[FC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_54",
            "guarantor_financial_class",
            "GT1.54",
        ),
        serialization_alias="GT1.54",
        title="Guarantor Financial Class",
        description="O | Item #01231",
    )

    gt1_55: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_55",
            "guarantor_race",
            "GT1.55",
        ),
        serialization_alias="GT1.55",
        title="Guarantor Race",
        description="O | Item #01291 | Table 0005 - Race",
    )

    gt1_56: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_56",
            "guarantor_birth_place",
            "GT1.56",
        ),
        serialization_alias="GT1.56",
        title="Guarantor Birth Place",
        description="O | Item #01851 | LEN:250",
    )

    gt1_57: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_57",
            "vip_indicator",
            "GT1.57",
        ),
        serialization_alias="GT1.57",
        title="VIP Indicator",
        description="O | Item #00146 | Table 0099 - VIP Indicator | LEN:2",
    )

    @field_validator("gt1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("gt1_13", "gt1_14", "gt1_31", "gt1_32", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("gt1_15", "gt1_28", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
