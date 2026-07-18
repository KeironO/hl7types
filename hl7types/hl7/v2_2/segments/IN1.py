"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: IN1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.PN import PN
from ..datatypes.TS import TS

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class IN1(HL7Model):
    """INSURANCE (S6.4.5).

    Attributes
    ----------
    in1_1 : str
        IN1.1 - Set ID - insurance (SI) R S6.4.5.1

    in1_2 : str
        IN1.2 - Insurance plan ID (ID) R S6.4.1.14 | 0072 - INS. PLAN ID

    in1_3 : str
        IN1.3 - Insurance company ID (ST) R S6.4.5.3

    in1_4 : str | None
        IN1.4 - Insurance company name (ST) NA S6.4.5.4

    in1_5 : AD | None
        IN1.5 - Insurance company address (AD) NA S6.4.5.5

    in1_6 : PN | None
        IN1.6 - Insurance company contact pers (PN) NA S6.4.5.6

    in1_7 : list[str] | None
        IN1.7 - Insurance company phone number (TN) NA rep S6.4.5.7

    in1_8 : str | None
        IN1.8 - Group number (ST) NA S6.4.5.8

    in1_9 : str | None
        IN1.9 - Group name (ST) NA S6.4.5.9

    in1_10 : str | None
        IN1.10 - Insured's group employer ID (ST) NA S6.4.5.10

    in1_11 : str | None
        IN1.11 - Insured's group employer name (ST) NA S6.4.5.11

    in1_12 : str | None
        IN1.12 - Plan effective date (DT) NA S6.4.5.12

    in1_13 : str | None
        IN1.13 - Plan expiration date (DT) NA S6.4.5.13

    in1_14 : str | None
        IN1.14 - Authorization information (CM) NA S6.4.5.14

    in1_15 : str | None
        IN1.15 - Plan type (ID) NA S6.4.5.15 | 0086 - INS. PLAN TYPE

    in1_16 : PN | None
        IN1.16 - Name of insured (PN) NA S6.4.5.16

    in1_17 : str | None
        IN1.17 - Insured's relationship to patient (ID) NA S6.4.5.17 | 0063 - RELATIONSHIP

    in1_18 : str | None
        IN1.18 - Insured's date of birth (DT) NA S6.4.5.18

    in1_19 : AD | None
        IN1.19 - Insured's address (AD) NA S6.4.5.19

    in1_20 : str | None
        IN1.20 - Assignment of benefits (ID) NA S6.4.5.20 | 0135 - ASSIGNMENT OF BENEFITS

    in1_21 : str | None
        IN1.21 - Coordination of benefits (ID) NA S6.4.5.21 | 0173 - COORDINATION OF BENEFITS

    in1_22 : str | None
        IN1.22 - Coordination of benefits - priority (ST) NA S6.4.5.22

    in1_23 : str | None
        IN1.23 - Notice of admission code (ID) NA S6.4.5.23 | 0136 - Y/N Indicator

    in1_24 : str | None
        IN1.24 - Notice of admission date (DT) NA S6.4.5.24

    in1_25 : str | None
        IN1.25 - Report of eligibility code (ID) NA S6.4.5.25

    in1_26 : str | None
        IN1.26 - Report of eligibility date (DT) NA S6.4.5.26

    in1_27 : str | None
        IN1.27 - Release information code (ID) NA S6.4.5.27 | 0093 - RELEASE OF INFORMATION

    in1_28 : str | None
        IN1.28 - Pre-admit certification (PAC) (ST) NA S6.4.5.28

    in1_29 : TS | None
        IN1.29 - Verification date / time (TS) NA S6.4.5.29

    in1_30 : str | None
        IN1.30 - Verification by (CN) NA S6.4.5.30

    in1_31 : str | None
        IN1.31 - Type of agreement code (ID) NA S6.4.5.31 | 0098 - TYPE OF AGREEMENT CODE

    in1_32 : str | None
        IN1.32 - Billing status (ID) NA S6.4.5.32 | 0022 - BILLING STATUS

    in1_33 : str | None
        IN1.33 - Lifetime reserve days (NM) NA S6.4.5.33

    in1_34 : str | None
        IN1.34 - Delay before lifetime reserve days (NM) NA S6.4.5.34

    in1_35 : str | None
        IN1.35 - Company plan code (ID) NA S6.4.5.35 | 0042 - INS. COMPANY PLAN CODE

    in1_36 : str | None
        IN1.36 - Policy number (ST) NA S6.4.5.36

    in1_37 : str | None
        IN1.37 - Policy deductible (NM) NA S6.4.5.37

    in1_38 : str | None
        IN1.38 - Policy limit - amount (NM) NA S6.4.5.38

    in1_39 : str | None
        IN1.39 - Policy limit - days (NM) NA S6.4.5.39

    in1_40 : str | None
        IN1.40 - Room rate - semi-private (NM) NA S6.4.5.40

    in1_41 : str | None
        IN1.41 - Room rate - private (NM) NA S6.4.5.41

    in1_42 : CE | None
        IN1.42 - Insured's employment status (CE) NA S6.4.5.42 | 0066 - EMPLOYMENT STATUS

    in1_43 : str | None
        IN1.43 - Insured's sex (ID) NA S6.4.5.43 | 0001 - SEX

    in1_44 : AD | None
        IN1.44 - Insured's employer address (AD) NA S6.4.5.44

    in1_45 : str | None
        IN1.45 - Verification status (ST) NA S6.4.5.45

    in1_46 : str | None
        IN1.46 - Prior insurance plan ID (ID) NA S6.4.5.46 | 0072 - INS. PLAN ID
    """

    in1_1: str = Field(
        validation_alias=AliasChoices(
            "in1_1",
            "set_id_insurance",
            "IN1.1",
        ),
        serialization_alias="IN1.1",
        title="Set ID - insurance",
        description="R | Item #00426 | LEN:4",
    )

    in1_2: str = Field(
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="Insurance plan ID",
        description="R | Item #00368 | Table 0072 - INS. PLAN ID | LEN:8",
    )

    in1_3: str = Field(
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="Insurance company ID",
        description="R | Item #00428 | LEN:9",
    )

    in1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_4",
            "insurance_company_name",
            "IN1.4",
        ),
        serialization_alias="IN1.4",
        title="Insurance company name",
        description="NA | Item #00429 | LEN:45",
    )

    in1_5: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_5",
            "insurance_company_address",
            "IN1.5",
        ),
        serialization_alias="IN1.5",
        title="Insurance company address",
        description="NA | Item #00430",
    )

    in1_6: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_6",
            "insurance_company_contact_pers",
            "IN1.6",
        ),
        serialization_alias="IN1.6",
        title="Insurance company contact pers",
        description="NA | Item #00431",
    )

    in1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_7",
            "insurance_company_phone_number",
            "IN1.7",
        ),
        serialization_alias="IN1.7",
        title="Insurance company phone number",
        description="NA | Item #00432 | LEN:40",
    )

    in1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_8",
            "group_number",
            "IN1.8",
        ),
        serialization_alias="IN1.8",
        title="Group number",
        description="NA | Item #00433 | LEN:12",
    )

    in1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_9",
            "group_name",
            "IN1.9",
        ),
        serialization_alias="IN1.9",
        title="Group name",
        description="NA | Item #00434 | LEN:35",
    )

    in1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_10",
            "insured_s_group_employer_id",
            "IN1.10",
        ),
        serialization_alias="IN1.10",
        title="Insured's group employer ID",
        description="NA | Item #00435 | LEN:12",
    )

    in1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_11",
            "insured_s_group_employer_name",
            "IN1.11",
        ),
        serialization_alias="IN1.11",
        title="Insured's group employer name",
        description="NA | Item #00436 | LEN:45",
    )

    in1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_12",
            "plan_effective_date",
            "IN1.12",
        ),
        serialization_alias="IN1.12",
        title="Plan effective date",
        description="NA | Item #00437 | LEN:8",
    )

    in1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_13",
            "plan_expiration_date",
            "IN1.13",
        ),
        serialization_alias="IN1.13",
        title="Plan expiration date",
        description="NA | Item #00438 | LEN:8",
    )

    in1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_14",
            "authorization_information",
            "IN1.14",
        ),
        serialization_alias="IN1.14",
        title="Authorization information",
        description="NA | Item #00439",
    )

    in1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_15",
            "plan_type",
            "IN1.15",
        ),
        serialization_alias="IN1.15",
        title="Plan type",
        description="NA | Item #00440 | Table 0086 - INS. PLAN TYPE | LEN:5",
    )

    in1_16: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_16",
            "name_of_insured",
            "IN1.16",
        ),
        serialization_alias="IN1.16",
        title="Name of insured",
        description="NA | Item #00441",
    )

    in1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_17",
            "insured_s_relationship_to_patient",
            "IN1.17",
        ),
        serialization_alias="IN1.17",
        title="Insured's relationship to patient",
        description="NA | Item #00442 | Table 0063 - RELATIONSHIP | LEN:2",
    )

    in1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_18",
            "insured_s_date_of_birth",
            "IN1.18",
        ),
        serialization_alias="IN1.18",
        title="Insured's date of birth",
        description="NA | Item #00443 | LEN:8",
    )

    in1_19: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_19",
            "insured_s_address",
            "IN1.19",
        ),
        serialization_alias="IN1.19",
        title="Insured's address",
        description="NA | Item #00444",
    )

    in1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_20",
            "assignment_of_benefits",
            "IN1.20",
        ),
        serialization_alias="IN1.20",
        title="Assignment of benefits",
        description=(
            "NA | Item #00445 | Table 0135 - ASSIGNMENT OF BENEFITS | LEN:2"
        ),
    )

    in1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_21",
            "coordination_of_benefits",
            "IN1.21",
        ),
        serialization_alias="IN1.21",
        title="Coordination of benefits",
        description=(
            "NA | Item #00446 | Table 0173 - COORDINATION OF BENEFITS | LEN:2"
        ),
    )

    in1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_22",
            "coordination_of_benefits_priority",
            "IN1.22",
        ),
        serialization_alias="IN1.22",
        title="Coordination of benefits - priority",
        description="NA | Item #00447 | LEN:2",
    )

    in1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_23",
            "notice_of_admission_code",
            "IN1.23",
        ),
        serialization_alias="IN1.23",
        title="Notice of admission code",
        description="NA | Item #00448 | Table 0136 - Y/N Indicator | LEN:2",
    )

    in1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_24",
            "notice_of_admission_date",
            "IN1.24",
        ),
        serialization_alias="IN1.24",
        title="Notice of admission date",
        description="NA | Item #00449 | LEN:8",
    )

    in1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_25",
            "report_of_eligibility_code",
            "IN1.25",
        ),
        serialization_alias="IN1.25",
        title="Report of eligibility code",
        description="NA | Item #00450 | LEN:4",
    )

    in1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_26",
            "report_of_eligibility_date",
            "IN1.26",
        ),
        serialization_alias="IN1.26",
        title="Report of eligibility date",
        description="NA | Item #00451 | LEN:8",
    )

    in1_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_27",
            "release_information_code",
            "IN1.27",
        ),
        serialization_alias="IN1.27",
        title="Release information code",
        description=(
            "NA | Item #00452 | Table 0093 - RELEASE OF INFORMATION | LEN:2"
        ),
    )

    in1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_28",
            "pre_admit_certification_pac",
            "IN1.28",
        ),
        serialization_alias="IN1.28",
        title="Pre-admit certification (PAC)",
        description="NA | Item #00453 | LEN:15",
    )

    in1_29: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_29",
            "verification_date_time",
            "IN1.29",
        ),
        serialization_alias="IN1.29",
        title="Verification date / time",
        description="NA | Item #00454",
    )

    in1_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_30",
            "verification_by",
            "IN1.30",
        ),
        serialization_alias="IN1.30",
        title="Verification by",
        description="NA | Item #00455",
    )

    in1_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_31",
            "type_of_agreement_code",
            "IN1.31",
        ),
        serialization_alias="IN1.31",
        title="Type of agreement code",
        description=(
            "NA | Item #00456 | Table 0098 - TYPE OF AGREEMENT CODE | LEN:2"
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
        title="Billing status",
        description="NA | Item #00457 | Table 0022 - BILLING STATUS | LEN:2",
    )

    in1_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_33",
            "lifetime_reserve_days",
            "IN1.33",
        ),
        serialization_alias="IN1.33",
        title="Lifetime reserve days",
        description="NA | Item #00458 | LEN:4",
    )

    in1_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_34",
            "delay_before_lifetime_reserve_days",
            "IN1.34",
        ),
        serialization_alias="IN1.34",
        title="Delay before lifetime reserve days",
        description="NA | Item #00459 | LEN:4",
    )

    in1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_35",
            "company_plan_code",
            "IN1.35",
        ),
        serialization_alias="IN1.35",
        title="Company plan code",
        description=(
            "NA | Item #00460 | Table 0042 - INS. COMPANY PLAN CODE | LEN:8"
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
        title="Policy number",
        description="NA | Item #00461 | LEN:15",
    )

    in1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_37",
            "policy_deductible",
            "IN1.37",
        ),
        serialization_alias="IN1.37",
        title="Policy deductible",
        description="NA | Item #00462 | LEN:12",
    )

    in1_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_38",
            "policy_limit_amount",
            "IN1.38",
        ),
        serialization_alias="IN1.38",
        title="Policy limit - amount",
        description="NA | Item #00463 | LEN:12",
    )

    in1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_39",
            "policy_limit_days",
            "IN1.39",
        ),
        serialization_alias="IN1.39",
        title="Policy limit - days",
        description="NA | Item #00464 | LEN:4",
    )

    in1_40: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_40",
            "room_rate_semi_private",
            "IN1.40",
        ),
        serialization_alias="IN1.40",
        title="Room rate - semi-private",
        description="NA | Item #00465 | LEN:12",
    )

    in1_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_41",
            "room_rate_private",
            "IN1.41",
        ),
        serialization_alias="IN1.41",
        title="Room rate - private",
        description="NA | Item #00466 | LEN:12",
    )

    in1_42: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_42",
            "insured_s_employment_status",
            "IN1.42",
        ),
        serialization_alias="IN1.42",
        title="Insured's employment status",
        description="NA | Item #00467 | Table 0066 - EMPLOYMENT STATUS",
    )

    in1_43: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_43",
            "insured_s_sex",
            "IN1.43",
        ),
        serialization_alias="IN1.43",
        title="Insured's sex",
        description="NA | Item #00468 | Table 0001 - SEX | LEN:1",
    )

    in1_44: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_44",
            "insured_s_employer_address",
            "IN1.44",
        ),
        serialization_alias="IN1.44",
        title="Insured's employer address",
        description="NA | Item #00469",
    )

    in1_45: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_45",
            "verification_status",
            "IN1.45",
        ),
        serialization_alias="IN1.45",
        title="Verification status",
        description="NA | Item #00470 | LEN:2",
    )

    in1_46: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_46",
            "prior_insurance_plan_id",
            "IN1.46",
        ),
        serialization_alias="IN1.46",
        title="Prior insurance plan ID",
        description="NA | Item #00471 | Table 0072 - INS. PLAN ID | LEN:8",
    )

    @field_validator("in1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("in1_12", "in1_13", "in1_18", "in1_24", "in1_26", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("in1_33", "in1_34", "in1_37", "in1_38", "in1_39", "in1_40", "in1_41", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
