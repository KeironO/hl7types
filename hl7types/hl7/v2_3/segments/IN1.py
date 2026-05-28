"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: IN1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.CX import CX
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


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
        title="Set ID - Insurance",
        description="Item #426",
    )

    in1_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="Insurance Plan ID",
        description="Item #368 | Table HL70072",
    )

    in1_3: CX = Field(
        default=...,
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="Insurance Company ID",
        description="Item #428",
    )

    in1_4: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_4",
            "insurance_company_name",
            "IN1.4",
        ),
        serialization_alias="IN1.4",
        title="Insurance Company Name",
        description="Item #429",
    )

    in1_5: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_5",
            "insurance_company_address",
            "IN1.5",
        ),
        serialization_alias="IN1.5",
        title="Insurance Company Address",
        description="Item #430",
    )

    in1_6: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_6",
            "insurance_co_contact_ppers",
            "IN1.6",
        ),
        serialization_alias="IN1.6",
        title="Insurance Co. Contact Ppers",
        description="Item #431",
    )

    in1_7: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_7",
            "insurance_co_phone_number",
            "IN1.7",
        ),
        serialization_alias="IN1.7",
        title="Insurance Co Phone Number",
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
        title="Group Number",
        description="Item #433",
    )

    in1_9: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_9",
            "group_name",
            "IN1.9",
        ),
        serialization_alias="IN1.9",
        title="Group Name",
        description="Item #434",
    )

    in1_10: Optional[CX] = Field(
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

    in1_11: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_11",
            "insured_s_group_emp_name",
            "IN1.11",
        ),
        serialization_alias="IN1.11",
        title="Insured's Group Emp Name",
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
        title="Plan Effective Date",
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
        title="Plan Expiration Date",
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
        title="Authorization Information",
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
        title="Plan Type",
        description="Item #440 | Table HL70086",
    )

    in1_16: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_16",
            "name_of_insured",
            "IN1.16",
        ),
        serialization_alias="IN1.16",
        title="Name of Insured",
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
        title="Insured's Relationship to Patient",
        description="Item #442 | Table HL70063",
    )

    in1_18: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_18",
            "insured_s_date_of_birth",
            "IN1.18",
        ),
        serialization_alias="IN1.18",
        title="Insured's Date of Birth",
        description="Item #443",
    )

    in1_19: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_19",
            "insured_s_address",
            "IN1.19",
        ),
        serialization_alias="IN1.19",
        title="Insured's Address",
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
        title="Assignment of Benefits",
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
        title="Coordination of Benefits",
        description="Item #446 | Table HL70173",
    )

    in1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_22",
            "coord_of_ben_priority",
            "IN1.22",
        ),
        serialization_alias="IN1.22",
        title="Coord of Ben. Priority",
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
        title="Notice of Admission Code",
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
        title="Notice of Admission Date",
        description="Item #449",
    )

    in1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_25",
            "rpt_of_eigibility_code",
            "IN1.25",
        ),
        serialization_alias="IN1.25",
        title="Rpt of Eigibility Code",
        description="Item #450 | Table HL70136",
    )

    in1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_26",
            "rpt_of_eligibility_date",
            "IN1.26",
        ),
        serialization_alias="IN1.26",
        title="Rpt of Eligibility Date",
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
        title="Release Information Code",
        description="Item #452 | Table HL70093",
    )

    in1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_28",
            "pre_admit_cert_pac",
            "IN1.28",
        ),
        serialization_alias="IN1.28",
        title="Pre-Admit Cert (PAC)",
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
        title="Verification Date/Time",
        description="Item #454",
    )

    in1_30: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_30",
            "verification_by",
            "IN1.30",
        ),
        serialization_alias="IN1.30",
        title="Verification By",
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
        title="Type of Agreement Code",
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
        title="Billing Status",
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
        title="Lifetime Reserve Days",
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
        title="Company Plan Code",
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
        title="Policy Number",
        description="Item #461",
    )

    in1_37: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_37",
            "policy_deductible",
            "IN1.37",
        ),
        serialization_alias="IN1.37",
        title="Policy Deductible",
        description="Item #462",
    )

    in1_38: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_38",
            "policy_limit_amount",
            "IN1.38",
        ),
        serialization_alias="IN1.38",
        title="Policy Limit - Amount",
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
        title="Policy Limit - Days",
        description="Item #464",
    )

    in1_40: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_40",
            "room_rate_semi_private",
            "IN1.40",
        ),
        serialization_alias="IN1.40",
        title="Room Rate - Semi-Private",
        description="Item #465",
    )

    in1_41: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_41",
            "room_rate_private",
            "IN1.41",
        ),
        serialization_alias="IN1.41",
        title="Room Rate - Private",
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
        title="Insured's Employment Status",
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
        title="Insured's Sex",
        description="Item #468 | Table HL70001",
    )

    in1_44: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_44",
            "insured_s_employer_address",
            "IN1.44",
        ),
        serialization_alias="IN1.44",
        title="Insured's Employer Address",
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
        title="Verification Status",
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
        title="Prior Insurance Plan ID",
        description="Item #471 | Table HL70072",
    )

    in1_47: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_47",
            "coverage_type",
            "IN1.47",
        ),
        serialization_alias="IN1.47",
        title="Coverage Type",
        description="Item #1277 | Table HL70309",
    )

    in1_48: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_48",
            "handicap",
            "IN1.48",
        ),
        serialization_alias="IN1.48",
        title="Handicap",
        description="Item #753 | Table HL70310",
    )

    in1_49: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_49",
            "insured_s_id_number",
            "IN1.49",
        ),
        serialization_alias="IN1.49",
        title="Insured's ID Number",
        description="Item #1230",
    )

    model_config = {"populate_by_name": True}
