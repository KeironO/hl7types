"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: IN1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class IN1(HL7Model):
    """INSURANCE (S6.3.5).

    Attributes
    ----------
    in1_1 : str
        IN1.1 - SET ID - INSURANCE (SI) R S6-10

    in1_2 : str
        IN1.2 - INSURANCE PLAN ID (ID) R | 0072 - INS. PLAN ID

    in1_3 : str
        IN1.3 - INSURANCE COMPANY ID (ST) R

    in1_4 : str | None
        IN1.4 - INSURANCE COMPANY NAME (ST) O

    in1_5 : str | None
        IN1.5 - INSURANCE COMPANY ADDRESS (AD) O

    in1_6 : str | None
        IN1.6 - INSURANCE CO. CONTACT PERS (PN) O

    in1_7 : str | None
        IN1.7 - INSURANCE CO PHONE NUMBER (TN) O

    in1_8 : str | None
        IN1.8 - GROUP NUMBER (ST) O

    in1_9 : str | None
        IN1.9 - GROUP NAME (ST) O

    in1_10 : str | None
        IN1.10 - INSURED'S GROUP EMP. ID (ST) O

    in1_11 : str | None
        IN1.11 - INSURED'S GROUP EMP. NAME (ST) O

    in1_12 : str | None
        IN1.12 - PLAN EFFECTIVE DATE (DT) O

    in1_13 : str | None
        IN1.13 - PLAN EXPIRATION DATE (DT) O

    in1_14 : str | None
        IN1.14 - AUTHORIZATION INFORMATION (ST) O

    in1_15 : str | None
        IN1.15 - PLAN TYPE (ID) O | 0086 - INS. PLAN TYPE

    in1_16 : str | None
        IN1.16 - NAME OF INSURED (PN) O

    in1_17 : str | None
        IN1.17 - INSURED'S RELATIONSHIP TO PATIENT (ID) O | 0063 - RELATIONSHIP

    in1_18 : str | None
        IN1.18 - INSURED'S DATE OF BIRTH (DT) O

    in1_19 : str | None
        IN1.19 - INSURED'S ADDRESS (AD) O

    in1_20 : str | None
        IN1.20 - ASSIGNMENT OF BENEFITS (ID) O

    in1_21 : str | None
        IN1.21 - COORDINATION OF BENEFITS (ID) O

    in1_22 : str | None
        IN1.22 - COORD OF BEN. PRIORITY (ST) O

    in1_23 : str | None
        IN1.23 - NOTICE OF ADMISSION CODE (ID) O | 0081 - NOTICE OF ADMISSION

    in1_24 : str | None
        IN1.24 - NOTICE OF ADMISSION DATE (DT) O

    in1_25 : str | None
        IN1.25 - RPT OF ELIGIBILITY CODE (ID) O | 0094 - REPORT OF ELIGIBILITY

    in1_26 : str | None
        IN1.26 - RPT OF ELIGIBILITY DATE (DT) O

    in1_27 : str | None
        IN1.27 - RELEASE INFORMATION CODE (ID) O | 0093 - RELEASE OF INFORMATION

    in1_28 : str | None
        IN1.28 - PRE-ADMIT CERT. (PAC) (ST) O

    in1_29 : str | None
        IN1.29 - VERIFICATION DATE (DT) O

    in1_30 : str | None
        IN1.30 - VERIFICATION BY (CM) O

    in1_31 : str | None
        IN1.31 - TYPE OF AGREEMENT CODE (ID) O | 0098 - TYPE OF AGREEMENT CODE

    in1_32 : str | None
        IN1.32 - BILLING STATUS (ID) O | 0022 - BILLING STATUS

    in1_33 : str | None
        IN1.33 - LIFETIME RESERVE DAYS (NM) O

    in1_34 : str | None
        IN1.34 - DELAY BEFORE L. R. DAY (NM) O

    in1_35 : str | None
        IN1.35 - COMPANY PLAN CODE (ST) O | 0042 - INS. COMPANY PLAN CODE

    in1_36 : str | None
        IN1.36 - POLICY NUMBER (ST) O

    in1_37 : str | None
        IN1.37 - POLICY DEDUCTIBLE (NM) O

    in1_38 : str | None
        IN1.38 - POLICY LIMIT - AMOUNT (NM) O

    in1_39 : str | None
        IN1.39 - POLICY LIMIT - DAYS (NM) O

    in1_40 : str | None
        IN1.40 - ROOM RATE - SEMI-PRIVATE (NM) O

    in1_41 : str | None
        IN1.41 - ROOM RATE - PRIVATE (NM) O

    in1_42 : str | None
        IN1.42 - INSURED'S EMPLOYMENT STATUS (ID) O | 0066 - EMPLOYMENT STATUS

    in1_43 : str | None
        IN1.43 - INSURED'S SEX (ID) O | 0001 - SEX

    in1_44 : str | None
        IN1.44 - INSURED'S EMPLOYER ADDRESS (AD) O
    """

    in1_1: str = Field(
        validation_alias=AliasChoices(
            "in1_1",
            "set_id_insurance",
            "IN1.1",
        ),
        serialization_alias="IN1.1",
        title="SET ID - INSURANCE",
        description="R | Item #00234 | LEN:4",
    )

    in1_2: str = Field(
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="INSURANCE PLAN ID",
        description="R | Item #00378 | Table 0072 - INS. PLAN ID | LEN:8",
    )

    in1_3: str = Field(
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="INSURANCE COMPANY ID",
        description="R | Item #00235 | LEN:6",
    )

    in1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_4",
            "insurance_company_name",
            "IN1.4",
        ),
        serialization_alias="IN1.4",
        title="INSURANCE COMPANY NAME",
        description="O | Item #00236 | LEN:45",
    )

    in1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_5",
            "insurance_company_address",
            "IN1.5",
        ),
        serialization_alias="IN1.5",
        title="INSURANCE COMPANY ADDRESS",
        description="O | Item #00237 | LEN:106",
    )

    in1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_6",
            "insurance_co_contact_pers",
            "IN1.6",
        ),
        serialization_alias="IN1.6",
        title="INSURANCE CO. CONTACT PERS",
        description="O | Item #00242 | LEN:48",
    )

    in1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_7",
            "insurance_co_phone_number",
            "IN1.7",
        ),
        serialization_alias="IN1.7",
        title="INSURANCE CO PHONE NUMBER",
        description="O | Item #00243 | LEN:40",
    )

    in1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_8",
            "group_number",
            "IN1.8",
        ),
        serialization_alias="IN1.8",
        title="GROUP NUMBER",
        description="O | Item #00248 | LEN:12",
    )

    in1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_9",
            "group_name",
            "IN1.9",
        ),
        serialization_alias="IN1.9",
        title="GROUP NAME",
        description="O | Item #00249 | LEN:35",
    )

    in1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_10",
            "insured_s_group_emp_id",
            "IN1.10",
        ),
        serialization_alias="IN1.10",
        title="INSURED'S GROUP EMP. ID",
        description="O | Item #00250 | LEN:12",
    )

    in1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_11",
            "insured_s_group_emp_name",
            "IN1.11",
        ),
        serialization_alias="IN1.11",
        title="INSURED'S GROUP EMP. NAME",
        description="O | Item #00251 | LEN:45",
    )

    in1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_12",
            "plan_effective_date",
            "IN1.12",
        ),
        serialization_alias="IN1.12",
        title="PLAN EFFECTIVE DATE",
        description="O | Item #00252 | LEN:8",
    )

    in1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_13",
            "plan_expiration_date",
            "IN1.13",
        ),
        serialization_alias="IN1.13",
        title="PLAN EXPIRATION DATE",
        description="O | Item #00253 | LEN:8",
    )

    in1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_14",
            "authorization_information",
            "IN1.14",
        ),
        serialization_alias="IN1.14",
        title="AUTHORIZATION INFORMATION",
        description="O | Item #00254 | LEN:55",
    )

    in1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_15",
            "plan_type",
            "IN1.15",
        ),
        serialization_alias="IN1.15",
        title="PLAN TYPE",
        description="O | Item #00260 | Table 0086 - INS. PLAN TYPE | LEN:2",
    )

    in1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_16",
            "name_of_insured",
            "IN1.16",
        ),
        serialization_alias="IN1.16",
        title="NAME OF INSURED",
        description="O | Item #00261 | LEN:48",
    )

    in1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_17",
            "insured_s_relationship_to_patient",
            "IN1.17",
        ),
        serialization_alias="IN1.17",
        title="INSURED'S RELATIONSHIP TO PATIENT",
        description="O | Item #00262 | Table 0063 - RELATIONSHIP | LEN:2",
    )

    in1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_18",
            "insured_s_date_of_birth",
            "IN1.18",
        ),
        serialization_alias="IN1.18",
        title="INSURED'S DATE OF BIRTH",
        description="O | Item #00708 | LEN:8",
    )

    in1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_19",
            "insured_s_address",
            "IN1.19",
        ),
        serialization_alias="IN1.19",
        title="INSURED'S ADDRESS",
        description="O | Item #00709 | LEN:106",
    )

    in1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_20",
            "assignment_of_benefits",
            "IN1.20",
        ),
        serialization_alias="IN1.20",
        title="ASSIGNMENT OF BENEFITS",
        description="O | Item #00263 | LEN:2",
    )

    in1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_21",
            "coordination_of_benefits",
            "IN1.21",
        ),
        serialization_alias="IN1.21",
        title="COORDINATION OF BENEFITS",
        description="O | Item #00264 | LEN:2",
    )

    in1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_22",
            "coord_of_ben_priority",
            "IN1.22",
        ),
        serialization_alias="IN1.22",
        title="COORD OF BEN. PRIORITY",
        description="O | Item #00265 | LEN:2",
    )

    in1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_23",
            "notice_of_admission_code",
            "IN1.23",
        ),
        serialization_alias="IN1.23",
        title="NOTICE OF ADMISSION CODE",
        description=(
            "O | Item #00266 | Table 0081 - NOTICE OF ADMISSION | LEN:2"
        ),
    )

    in1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_24",
            "notice_of_admission_date",
            "IN1.24",
        ),
        serialization_alias="IN1.24",
        title="NOTICE OF ADMISSION DATE",
        description="O | Item #00267 | LEN:8",
    )

    in1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_25",
            "rpt_of_eligibility_code",
            "IN1.25",
        ),
        serialization_alias="IN1.25",
        title="RPT OF ELIGIBILITY CODE",
        description=(
            "O | Item #00268 | Table 0094 - REPORT OF ELIGIBILITY | LEN:2"
        ),
    )

    in1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_26",
            "rpt_of_eligibility_date",
            "IN1.26",
        ),
        serialization_alias="IN1.26",
        title="RPT OF ELIGIBILITY DATE",
        description="O | Item #00269 | LEN:8",
    )

    in1_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_27",
            "release_information_code",
            "IN1.27",
        ),
        serialization_alias="IN1.27",
        title="RELEASE INFORMATION CODE",
        description=(
            "O | Item #00270 | Table 0093 - RELEASE OF INFORMATION | LEN:2"
        ),
    )

    in1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_28",
            "pre_admit_cert_pac",
            "IN1.28",
        ),
        serialization_alias="IN1.28",
        title="PRE-ADMIT CERT. (PAC)",
        description="O | Item #00271 | LEN:15",
    )

    in1_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_29",
            "verification_date",
            "IN1.29",
        ),
        serialization_alias="IN1.29",
        title="VERIFICATION DATE",
        description="O | Item #00272 | LEN:8",
    )

    in1_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_30",
            "verification_by",
            "IN1.30",
        ),
        serialization_alias="IN1.30",
        title="VERIFICATION BY",
        description="O | Item #00273 | LEN:60",
    )

    in1_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_31",
            "type_of_agreement_code",
            "IN1.31",
        ),
        serialization_alias="IN1.31",
        title="TYPE OF AGREEMENT CODE",
        description=(
            "O | Item #00277 | Table 0098 - TYPE OF AGREEMENT CODE | LEN:2"
        ),
    )

    in1_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_32",
            "billing_status",
            "IN1.32",
        ),
        serialization_alias="IN1.32",
        title="BILLING STATUS",
        description="O | Item #00278 | Table 0022 - BILLING STATUS | LEN:2",
    )

    in1_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_33",
            "lifetime_reserve_days",
            "IN1.33",
        ),
        serialization_alias="IN1.33",
        title="LIFETIME RESERVE DAYS",
        description="O | Item #00280 | LEN:4",
    )

    in1_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_34",
            "delay_before_l_r_day",
            "IN1.34",
        ),
        serialization_alias="IN1.34",
        title="DELAY BEFORE L. R. DAY",
        description="O | Item #00281 | LEN:4",
    )

    in1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_35",
            "company_plan_code",
            "IN1.35",
        ),
        serialization_alias="IN1.35",
        title="COMPANY PLAN CODE",
        description=(
            "O | Item #00282 | Table 0042 - INS. COMPANY PLAN CODE | LEN:8"
        ),
    )

    in1_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_36",
            "policy_number",
            "IN1.36",
        ),
        serialization_alias="IN1.36",
        title="POLICY NUMBER",
        description="O | Item #00283 | LEN:15",
    )

    in1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_37",
            "policy_deductible",
            "IN1.37",
        ),
        serialization_alias="IN1.37",
        title="POLICY DEDUCTIBLE",
        description="O | Item #00284 | LEN:12",
    )

    in1_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_38",
            "policy_limit_amount",
            "IN1.38",
        ),
        serialization_alias="IN1.38",
        title="POLICY LIMIT - AMOUNT",
        description="O | Item #00285 | LEN:12",
    )

    in1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_39",
            "policy_limit_days",
            "IN1.39",
        ),
        serialization_alias="IN1.39",
        title="POLICY LIMIT - DAYS",
        description="O | Item #00286 | LEN:4",
    )

    in1_40: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_40",
            "room_rate_semi_private",
            "IN1.40",
        ),
        serialization_alias="IN1.40",
        title="ROOM RATE - SEMI-PRIVATE",
        description="O | Item #00287 | LEN:12",
    )

    in1_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_41",
            "room_rate_private",
            "IN1.41",
        ),
        serialization_alias="IN1.41",
        title="ROOM RATE - PRIVATE",
        description="O | Item #00288 | LEN:12",
    )

    in1_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_42",
            "insured_s_employment_status",
            "IN1.42",
        ),
        serialization_alias="IN1.42",
        title="INSURED'S EMPLOYMENT STATUS",
        description="O | Item #00710 | Table 0066 - EMPLOYMENT STATUS | LEN:1",
    )

    in1_43: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_43",
            "insured_s_sex",
            "IN1.43",
        ),
        serialization_alias="IN1.43",
        title="INSURED'S SEX",
        description="O | Item #00711 | Table 0001 - SEX | LEN:1",
    )

    in1_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_44",
            "insured_s_employer_address",
            "IN1.44",
        ),
        serialization_alias="IN1.44",
        title="INSURED'S EMPLOYER ADDRESS",
        description="O | Item #00713 | LEN:106",
    )

    @field_validator("in1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("in1_12", "in1_13", "in1_18", "in1_24", "in1_26", "in1_29", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("in1_33", "in1_34", "in1_37", "in1_38", "in1_39", "in1_40", "in1_41", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
