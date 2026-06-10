"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: GT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
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


class GT1(HL7Model):
    """HL7 v2 GT1 segment.

    Attributes
    ----------
    gt1_1 : str
        GT1.1 (req) - Set ID - GT1 (SI)

    gt1_2 : list[CX] | None
        GT1.2 (opt, rep) - Guarantor Number (CX)

    gt1_3 : list[XPN]
        GT1.3 (req, rep) - Guarantor Name (XPN)

    gt1_4 : list[XPN] | None
        GT1.4 (opt, rep) - Guarantor Spouse Name (XPN)

    gt1_5 : list[XAD] | None
        GT1.5 (opt, rep) - Guarantor Address (XAD)

    gt1_6 : list[XTN] | None
        GT1.6 (opt, rep) - Guarantor Ph Num-Home (XTN)

    gt1_7 : list[XTN] | None
        GT1.7 (opt, rep) - Guarantor Ph Num-Business (XTN)

    gt1_8 : TS | None
        GT1.8 (opt) - Guarantor Date/Time Of Birth (TS)

    gt1_9 : str | None
        GT1.9 (opt) - Guarantor Sex (IS)

    gt1_10 : str | None
        GT1.10 (opt) - Guarantor Type (IS)

    gt1_11 : CE | None
        GT1.11 (opt) - Guarantor Relationship (CE)

    gt1_12 : str | None
        GT1.12 (opt) - Guarantor SSN (ST)

    gt1_13 : str | None
        GT1.13 (opt) - Guarantor Date - Begin (DT)

    gt1_14 : str | None
        GT1.14 (opt) - Guarantor Date - End (DT)

    gt1_15 : str | None
        GT1.15 (opt) - Guarantor Priority (NM)

    gt1_16 : list[XPN] | None
        GT1.16 (opt, rep) - Guarantor Employer Name (XPN)

    gt1_17 : list[XAD] | None
        GT1.17 (opt, rep) - Guarantor Employer Address (XAD)

    gt1_18 : list[XTN] | None
        GT1.18 (opt, rep) - Guarantor Employer Phone Number (XTN)

    gt1_19 : list[CX] | None
        GT1.19 (opt, rep) - Guarantor Employee ID Number (CX)

    gt1_20 : str | None
        GT1.20 (opt) - Guarantor Employment Status (IS)

    gt1_21 : list[XON] | None
        GT1.21 (opt, rep) - Guarantor Organization Name (XON)

    gt1_22 : str | None
        GT1.22 (opt) - Guarantor Billing Hold Flag (ID)

    gt1_23 : CE | None
        GT1.23 (opt) - Guarantor Credit Rating Code (CE)

    gt1_24 : TS | None
        GT1.24 (opt) - Guarantor Death Date And Time (TS)

    gt1_25 : str | None
        GT1.25 (opt) - Guarantor Death Flag (ID)

    gt1_26 : CE | None
        GT1.26 (opt) - Guarantor Charge Adjustment Code (CE)

    gt1_27 : CP | None
        GT1.27 (opt) - Guarantor Household Annual Income (CP)

    gt1_28 : str | None
        GT1.28 (opt) - Guarantor Household Size (NM)

    gt1_29 : list[CX] | None
        GT1.29 (opt, rep) - Guarantor Employer ID Number (CX)

    gt1_30 : CE | None
        GT1.30 (opt) - Guarantor Marital Status Code (CE)

    gt1_31 : str | None
        GT1.31 (opt) - Guarantor Hire Effective Date (DT)

    gt1_32 : str | None
        GT1.32 (opt) - Employment Stop Date (DT)

    gt1_33 : str | None
        GT1.33 (opt) - Living Dependency (IS)

    gt1_34 : list[str] | None
        GT1.34 (opt, rep) - Ambulatory Status (IS)

    gt1_35 : list[CE] | None
        GT1.35 (opt, rep) - Citizenship (CE)

    gt1_36 : CE | None
        GT1.36 (opt) - Primary Language (CE)

    gt1_37 : str | None
        GT1.37 (opt) - Living Arrangement (IS)

    gt1_38 : CE | None
        GT1.38 (opt) - Publicity Code (CE)

    gt1_39 : str | None
        GT1.39 (opt) - Protection Indicator (ID)

    gt1_40 : str | None
        GT1.40 (opt) - Student Indicator (IS)

    gt1_41 : CE | None
        GT1.41 (opt) - Religion (CE)

    gt1_42 : list[XPN] | None
        GT1.42 (opt, rep) - Mother’s Maiden Name (XPN)

    gt1_43 : CE | None
        GT1.43 (opt) - Nationality (CE)

    gt1_44 : list[CE] | None
        GT1.44 (opt, rep) - Ethnic Group (CE)

    gt1_45 : list[XPN] | None
        GT1.45 (opt, rep) - Contact Person’s Name (XPN)

    gt1_46 : list[XTN] | None
        GT1.46 (opt, rep) - Contact Person’s Telephone Number (XTN)

    gt1_47 : CE | None
        GT1.47 (opt) - Contact Reason (CE)

    gt1_48 : str | None
        GT1.48 (opt) - Contact Relationship (IS)

    gt1_49 : str | None
        GT1.49 (opt) - Job Title (ST)

    gt1_50 : JCC | None
        GT1.50 (opt) - Job Code/Class (JCC)

    gt1_51 : list[XON] | None
        GT1.51 (opt, rep) - Guarantor Employer’s Organization Name (XON)

    gt1_52 : str | None
        GT1.52 (opt) - Handicap (IS)

    gt1_53 : str | None
        GT1.53 (opt) - Job Status (IS)

    gt1_54 : FC | None
        GT1.54 (opt) - Guarantor Financial Class (FC)

    gt1_55 : list[CE] | None
        GT1.55 (opt, rep) - Guarantor Race (CE)
    """

    gt1_1: str = Field(
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_gt1",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="Set ID - GT1",
        description="Item #405",
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
        description="Item #406",
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
        description="Item #407",
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
        description="Item #408",
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
        description="Item #409",
    )

    gt1_6: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_6",
            "guarantor_ph_num_home",
            "GT1.6",
        ),
        serialization_alias="GT1.6",
        title="Guarantor Ph Num-Home",
        description="Item #410",
    )

    gt1_7: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_7",
            "guarantor_ph_num_business",
            "GT1.7",
        ),
        serialization_alias="GT1.7",
        title="Guarantor Ph Num-Business",
        description="Item #411",
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
        description="Item #412",
    )

    gt1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_9",
            "guarantor_sex",
            "GT1.9",
        ),
        serialization_alias="GT1.9",
        title="Guarantor Sex",
        description="Item #413 | Table HL70001",
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
        description="Item #414 | Table HL70068",
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
        description="Item #415 | Table HL70063",
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
        description="Item #416",
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
        description="Item #417",
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
        description="Item #418",
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
        description="Item #419",
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
        description="Item #420",
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
        description="Item #421",
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
        description="Item #422",
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
        description="Item #423",
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
        description="Item #424 | Table HL70066",
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
        description="Item #425",
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
        description="Item #773 | Table HL70136",
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
        description="Item #774 | Table HL70341",
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
        description="Item #775",
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
        description="Item #776 | Table HL70136",
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
        description="Item #777 | Table HL70218",
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
        description="Item #778",
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
        description="Item #779",
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
        description="Item #780",
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
        description="Item #781 | Table HL70002",
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
        description="Item #782",
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
        description="Item #783",
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
        description="Item #755 | Table HL70223",
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
        description="Item #145 | Table HL70009",
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
        description="Item #129 | Table HL70171",
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
        description="Item #118 | Table HL70296",
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
        description="Item #742 | Table HL70220",
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
        description="Item #743 | Table HL70215",
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
        description="Item #744 | Table HL70136",
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
        description="Item #745 | Table HL70231",
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
        description="Item #120 | Table HL70006",
    )

    gt1_42: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_42",
            "mother_s_maiden_name",
            "GT1.42",
        ),
        serialization_alias="GT1.42",
        title="Mother’s Maiden Name",
        description="Item #109",
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
        description="Item #739 | Table HL70212",
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
        description="Item #125 | Table HL70189",
    )

    gt1_45: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_45",
            "contact_person_s_name",
            "GT1.45",
        ),
        serialization_alias="GT1.45",
        title="Contact Person’s Name",
        description="Item #748",
    )

    gt1_46: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_46",
            "contact_person_s_telephone_number",
            "GT1.46",
        ),
        serialization_alias="GT1.46",
        title="Contact Person’s Telephone Number",
        description="Item #749",
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
        description="Item #747 | Table HL70222",
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
        description="Item #784 | Table HL70063",
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
        description="Item #785",
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
        description="Item #786 | Table HL70327",
    )

    gt1_51: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_51",
            "guarantor_employer_s_organization_name",
            "GT1.51",
        ),
        serialization_alias="GT1.51",
        title="Guarantor Employer’s Organization Name",
        description="Item #1299",
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
        description="Item #753 | Table HL70295",
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
        description="Item #752 | Table HL70311",
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
        description="Item #1231 | Table HL70064",
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
        description="Item #1291 | Table HL70005",
    )

    @field_validator("gt1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("gt1_13", "gt1_14", "gt1_31", "gt1_32", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("gt1_15", "gt1_28", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
