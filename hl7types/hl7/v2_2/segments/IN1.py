"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: IN1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.PN import PN
from ..datatypes.TS import TS


class IN1(BaseModel):
    """HL7 v2 IN1 segment.

    Attributes
    ----------
    in1_1 : str
        IN1.1 (req) - Set ID - insurance (SI)

    in1_2 : str
        IN1.2 (req) - Insurance plan ID (ID)

    in1_3 : str
        IN1.3 (req) - Insurance company ID (ST)

    in1_4 : str | None
        IN1.4 (opt) - Insurance company name (ST)

    in1_5 : AD | None
        IN1.5 (opt) - Insurance company address (AD)

    in1_6 : PN | None
        IN1.6 (opt) - Insurance company contact pers (PN)

    in1_7 : list[str] | None
        IN1.7 (opt, rep) - Insurance company phone number (TN)

    in1_8 : str | None
        IN1.8 (opt) - Group number (ST)

    in1_9 : str | None
        IN1.9 (opt) - Group name (ST)

    in1_10 : str | None
        IN1.10 (opt) - Insured's group employer ID (ST)

    in1_11 : str | None
        IN1.11 (opt) - Insured's group employer name (ST)

    in1_12 : str | None
        IN1.12 (opt) - Plan effective date (DT)

    in1_13 : str | None
        IN1.13 (opt) - Plan expiration date (DT)

    in1_14 : str | None
        IN1.14 (opt) - Authorization information (CM)

    in1_15 : str | None
        IN1.15 (opt) - Plan type (ID)

    in1_16 : PN | None
        IN1.16 (opt) - Name of insured (PN)

    in1_17 : str | None
        IN1.17 (opt) - Insured's relationship to patient (ID)

    in1_18 : str | None
        IN1.18 (opt) - Insured's date of birth (DT)

    in1_19 : AD | None
        IN1.19 (opt) - Insured's address (AD)

    in1_20 : str | None
        IN1.20 (opt) - Assignment of benefits (ID)

    in1_21 : str | None
        IN1.21 (opt) - Coordination of benefits (ID)

    in1_22 : str | None
        IN1.22 (opt) - Coordination of benefits - priority (ST)

    in1_23 : str | None
        IN1.23 (opt) - Notice of admission code (ID)

    in1_24 : str | None
        IN1.24 (opt) - Notice of admission date (DT)

    in1_25 : str | None
        IN1.25 (opt) - Report of eligibility code (ID)

    in1_26 : str | None
        IN1.26 (opt) - Report of eligibility date (DT)

    in1_27 : str | None
        IN1.27 (opt) - Release information code (ID)

    in1_28 : str | None
        IN1.28 (opt) - Pre-admit certification (PAC) (ST)

    in1_29 : TS | None
        IN1.29 (opt) - Verification date / time (TS)

    in1_30 : str | None
        IN1.30 (opt) - Verification by (CN)

    in1_31 : str | None
        IN1.31 (opt) - Type of agreement code (ID)

    in1_32 : str | None
        IN1.32 (opt) - Billing status (ID)

    in1_33 : str | None
        IN1.33 (opt) - Lifetime reserve days (NM)

    in1_34 : str | None
        IN1.34 (opt) - Delay before lifetime reserve days (NM)

    in1_35 : str | None
        IN1.35 (opt) - Company plan code (ID)

    in1_36 : str | None
        IN1.36 (opt) - Policy number (ST)

    in1_37 : str | None
        IN1.37 (opt) - Policy deductible (NM)

    in1_38 : str | None
        IN1.38 (opt) - Policy limit - amount (NM)

    in1_39 : str | None
        IN1.39 (opt) - Policy limit - days (NM)

    in1_40 : str | None
        IN1.40 (opt) - Room rate - semi-private (NM)

    in1_41 : str | None
        IN1.41 (opt) - Room rate - private (NM)

    in1_42 : CE | None
        IN1.42 (opt) - Insured's employment status (CE)

    in1_43 : str | None
        IN1.43 (opt) - Insured's sex (ID)

    in1_44 : AD | None
        IN1.44 (opt) - Insured's employer address (AD)

    in1_45 : str | None
        IN1.45 (opt) - Verification status (ST)

    in1_46 : str | None
        IN1.46 (opt) - Prior insurance plan ID (ID)
    """

    in1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_1",
            "set_id_insurance",
            "IN1.1",
        ),
        serialization_alias="IN1.1",
        title="Set ID - insurance",
        description="Item #426",
    )

    in1_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="Insurance plan ID",
        description="Item #368 | Table HL70072",
    )

    in1_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="Insurance company ID",
        description="Item #428",
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
        description="Item #429",
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
        description="Item #430",
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
        description="Item #431",
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
        description="Item #432",
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
        description="Item #433",
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
        description="Item #434",
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
        description="Item #435",
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
        description="Item #436",
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
        description="Item #437",
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
        description="Item #438",
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
        description="Item #439",
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
        description="Item #440 | Table HL70086",
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
        description="Item #441",
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
        description="Item #442 | Table HL70063",
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
        description="Item #443",
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
        description="Item #444",
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
        description="Item #445 | Table HL70135",
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
        description="Item #446 | Table HL70173",
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
        description="Item #447",
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
        description="Item #448 | Table HL70136",
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
        description="Item #449",
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
        description="Item #450",
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
        description="Item #451",
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
        description="Item #452 | Table HL70093",
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
        description="Item #453",
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
        description="Item #454",
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
        description="Item #455",
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
        description="Item #456 | Table HL70098",
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
        description="Item #457 | Table HL70022",
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
        description="Item #458",
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
        description="Item #459",
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
        description="Item #460 | Table HL70042",
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
        description="Item #461",
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
        description="Item #462",
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
        description="Item #463",
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
        description="Item #464",
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
        description="Item #465",
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
        description="Item #466",
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
        description="Item #467 | Table HL70066",
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
        description="Item #468 | Table HL70001",
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
        description="Item #469",
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
        description="Item #470",
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
        description="Item #471 | Table HL70072",
    )

    model_config = {"populate_by_name": True}
