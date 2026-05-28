"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: IN1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class IN1(BaseModel):
    """HL7 v2 IN1 segment."""

    in1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_1",
            "set_id_insurance",
            "IN1.1",
        ),
        serialization_alias="IN1.1",
        title="SET ID - INSURANCE",
        description="Item #234",
    )

    in1_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="INSURANCE PLAN ID",
        description="Item #378 | Table HL70072",
    )

    in1_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="INSURANCE COMPANY ID",
        description="Item #235",
    )

    in1_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_4",
            "insurance_company_name",
            "IN1.4",
        ),
        serialization_alias="IN1.4",
        title="INSURANCE COMPANY NAME",
        description="Item #236",
    )

    in1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_5",
            "insurance_company_address",
            "IN1.5",
        ),
        serialization_alias="IN1.5",
        title="INSURANCE COMPANY ADDRESS",
        description="Item #237",
    )

    in1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_6",
            "insurance_co_contact_pers",
            "IN1.6",
        ),
        serialization_alias="IN1.6",
        title="INSURANCE CO. CONTACT PERS",
        description="Item #242",
    )

    in1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_7",
            "insurance_co_phone_number",
            "IN1.7",
        ),
        serialization_alias="IN1.7",
        title="INSURANCE CO PHONE NUMBER",
        description="Item #243",
    )

    in1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_8",
            "group_number",
            "IN1.8",
        ),
        serialization_alias="IN1.8",
        title="GROUP NUMBER",
        description="Item #248",
    )

    in1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_9",
            "group_name",
            "IN1.9",
        ),
        serialization_alias="IN1.9",
        title="GROUP NAME",
        description="Item #249",
    )

    in1_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_10",
            "insured_s_group_emp_id",
            "IN1.10",
        ),
        serialization_alias="IN1.10",
        title="INSURED'S GROUP EMP. ID",
        description="Item #250",
    )

    in1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_11",
            "insured_s_group_emp_name",
            "IN1.11",
        ),
        serialization_alias="IN1.11",
        title="INSURED'S GROUP EMP. NAME",
        description="Item #251",
    )

    in1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_12",
            "plan_effective_date",
            "IN1.12",
        ),
        serialization_alias="IN1.12",
        title="PLAN EFFECTIVE DATE",
        description="Item #252",
    )

    in1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_13",
            "plan_expiration_date",
            "IN1.13",
        ),
        serialization_alias="IN1.13",
        title="PLAN EXPIRATION DATE",
        description="Item #253",
    )

    in1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_14",
            "authorization_information",
            "IN1.14",
        ),
        serialization_alias="IN1.14",
        title="AUTHORIZATION INFORMATION",
        description="Item #254",
    )

    in1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_15",
            "plan_type",
            "IN1.15",
        ),
        serialization_alias="IN1.15",
        title="PLAN TYPE",
        description="Item #260 | Table HL70086",
    )

    in1_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_16",
            "name_of_insured",
            "IN1.16",
        ),
        serialization_alias="IN1.16",
        title="NAME OF INSURED",
        description="Item #261",
    )

    in1_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_17",
            "insured_s_relationship_to_patient",
            "IN1.17",
        ),
        serialization_alias="IN1.17",
        title="INSURED'S RELATIONSHIP TO PATIENT",
        description="Item #262 | Table HL70063",
    )

    in1_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_18",
            "insured_s_date_of_birth",
            "IN1.18",
        ),
        serialization_alias="IN1.18",
        title="INSURED'S DATE OF BIRTH",
        description="Item #708",
    )

    in1_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_19",
            "insured_s_address",
            "IN1.19",
        ),
        serialization_alias="IN1.19",
        title="INSURED'S ADDRESS",
        description="Item #709",
    )

    in1_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_20",
            "assignment_of_benefits",
            "IN1.20",
        ),
        serialization_alias="IN1.20",
        title="ASSIGNMENT OF BENEFITS",
        description="Item #263",
    )

    in1_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_21",
            "coordination_of_benefits",
            "IN1.21",
        ),
        serialization_alias="IN1.21",
        title="COORDINATION OF BENEFITS",
        description="Item #264",
    )

    in1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_22",
            "coord_of_ben_priority",
            "IN1.22",
        ),
        serialization_alias="IN1.22",
        title="COORD OF BEN. PRIORITY",
        description="Item #265",
    )

    in1_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_23",
            "notice_of_admission_code",
            "IN1.23",
        ),
        serialization_alias="IN1.23",
        title="NOTICE OF ADMISSION CODE",
        description="Item #266 | Table HL70081",
    )

    in1_24: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_24",
            "notice_of_admission_date",
            "IN1.24",
        ),
        serialization_alias="IN1.24",
        title="NOTICE OF ADMISSION DATE",
        description="Item #267",
    )

    in1_25: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_25",
            "rpt_of_eligibility_code",
            "IN1.25",
        ),
        serialization_alias="IN1.25",
        title="RPT OF ELIGIBILITY CODE",
        description="Item #268 | Table HL70094",
    )

    in1_26: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_26",
            "rpt_of_eligibility_date",
            "IN1.26",
        ),
        serialization_alias="IN1.26",
        title="RPT OF ELIGIBILITY DATE",
        description="Item #269",
    )

    in1_27: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_27",
            "release_information_code",
            "IN1.27",
        ),
        serialization_alias="IN1.27",
        title="RELEASE INFORMATION CODE",
        description="Item #270 | Table HL70093",
    )

    in1_28: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_28",
            "pre_admit_cert_pac",
            "IN1.28",
        ),
        serialization_alias="IN1.28",
        title="PRE-ADMIT CERT. (PAC)",
        description="Item #271",
    )

    in1_29: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_29",
            "verification_date",
            "IN1.29",
        ),
        serialization_alias="IN1.29",
        title="VERIFICATION DATE",
        description="Item #272",
    )

    in1_30: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_30",
            "verification_by",
            "IN1.30",
        ),
        serialization_alias="IN1.30",
        title="VERIFICATION BY",
        description="Item #273",
    )

    in1_31: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_31",
            "type_of_agreement_code",
            "IN1.31",
        ),
        serialization_alias="IN1.31",
        title="TYPE OF AGREEMENT CODE",
        description="Item #277 | Table HL70098",
    )

    in1_32: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_32",
            "billing_status",
            "IN1.32",
        ),
        serialization_alias="IN1.32",
        title="BILLING STATUS",
        description="Item #278 | Table HL70022",
    )

    in1_33: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_33",
            "lifetime_reserve_days",
            "IN1.33",
        ),
        serialization_alias="IN1.33",
        title="LIFETIME RESERVE DAYS",
        description="Item #280",
    )

    in1_34: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_34",
            "delay_before_l_r_day",
            "IN1.34",
        ),
        serialization_alias="IN1.34",
        title="DELAY BEFORE L. R. DAY",
        description="Item #281",
    )

    in1_35: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_35",
            "company_plan_code",
            "IN1.35",
        ),
        serialization_alias="IN1.35",
        title="COMPANY PLAN CODE",
        description="Item #282 | Table HL70042",
    )

    in1_36: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_36",
            "policy_number",
            "IN1.36",
        ),
        serialization_alias="IN1.36",
        title="POLICY NUMBER",
        description="Item #283",
    )

    in1_37: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_37",
            "policy_deductible",
            "IN1.37",
        ),
        serialization_alias="IN1.37",
        title="POLICY DEDUCTIBLE",
        description="Item #284",
    )

    in1_38: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_38",
            "policy_limit_amount",
            "IN1.38",
        ),
        serialization_alias="IN1.38",
        title="POLICY LIMIT - AMOUNT",
        description="Item #285",
    )

    in1_39: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_39",
            "policy_limit_days",
            "IN1.39",
        ),
        serialization_alias="IN1.39",
        title="POLICY LIMIT - DAYS",
        description="Item #286",
    )

    in1_40: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_40",
            "room_rate_semi_private",
            "IN1.40",
        ),
        serialization_alias="IN1.40",
        title="ROOM RATE - SEMI-PRIVATE",
        description="Item #287",
    )

    in1_41: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_41",
            "room_rate_private",
            "IN1.41",
        ),
        serialization_alias="IN1.41",
        title="ROOM RATE - PRIVATE",
        description="Item #288",
    )

    in1_42: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_42",
            "insured_s_employment_status",
            "IN1.42",
        ),
        serialization_alias="IN1.42",
        title="INSURED'S EMPLOYMENT STATUS",
        description="Item #710 | Table HL70066",
    )

    in1_43: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_43",
            "insured_s_sex",
            "IN1.43",
        ),
        serialization_alias="IN1.43",
        title="INSURED'S SEX",
        description="Item #711 | Table HL70001",
    )

    in1_44: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_44",
            "insured_s_employer_address",
            "IN1.44",
        ),
        serialization_alias="IN1.44",
        title="INSURED'S EMPLOYER ADDRESS",
        description="Item #713",
    )

    model_config = {"populate_by_name": True}
