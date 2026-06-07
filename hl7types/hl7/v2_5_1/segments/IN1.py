"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: IN1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AUI import AUI
from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.CX import CX
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class IN1(HL7Model):
    """HL7 v2 IN1 segment.

    Attributes
    ----------
    in1_1 : str
        IN1.1 (req) - Set ID - IN1 (SI)

    in1_2 : CE
        IN1.2 (req) - Insurance Plan ID (CE)

    in1_3 : list[CX] | None
        IN1.3 (req, rep) - Insurance Company ID (CX) [optional: CX has no required components]

    in1_4 : list[XON] | None
        IN1.4 (opt, rep) - Insurance Company Name (XON)

    in1_5 : list[XAD] | None
        IN1.5 (opt, rep) - Insurance Company Address (XAD)

    in1_6 : list[XPN] | None
        IN1.6 (opt, rep) - Insurance Co Contact Person (XPN)

    in1_7 : list[XTN] | None
        IN1.7 (opt, rep) - Insurance Co Phone Number (XTN)

    in1_8 : str | None
        IN1.8 (opt) - Group Number (ST)

    in1_9 : list[XON] | None
        IN1.9 (opt, rep) - Group Name (XON)

    in1_10 : list[CX] | None
        IN1.10 (opt, rep) - Insured's Group Emp ID (CX)

    in1_11 : list[XON] | None
        IN1.11 (opt, rep) - Insured's Group Emp Name (XON)

    in1_12 : str | None
        IN1.12 (opt) - Plan Effective Date (DT)

    in1_13 : str | None
        IN1.13 (opt) - Plan Expiration Date (DT)

    in1_14 : AUI | None
        IN1.14 (opt) - Authorization Information (AUI)

    in1_15 : str | None
        IN1.15 (opt) - Plan Type (IS)

    in1_16 : list[XPN] | None
        IN1.16 (opt, rep) - Name Of Insured (XPN)

    in1_17 : CE | None
        IN1.17 (opt) - Insured's Relationship To Patient (CE)

    in1_18 : TS | None
        IN1.18 (opt) - Insured's Date Of Birth (TS)

    in1_19 : list[XAD] | None
        IN1.19 (opt, rep) - Insured's Address (XAD)

    in1_20 : str | None
        IN1.20 (opt) - Assignment Of Benefits (IS)

    in1_21 : str | None
        IN1.21 (opt) - Coordination Of Benefits (IS)

    in1_22 : str | None
        IN1.22 (opt) - Coord Of Ben. Priority (ST)

    in1_23 : str | None
        IN1.23 (opt) - Notice Of Admission Flag (ID)

    in1_24 : str | None
        IN1.24 (opt) - Notice Of Admission Date (DT)

    in1_25 : str | None
        IN1.25 (opt) - Report Of Eligibility Flag (ID)

    in1_26 : str | None
        IN1.26 (opt) - Report Of Eligibility Date (DT)

    in1_27 : str | None
        IN1.27 (opt) - Release Information Code (IS)

    in1_28 : str | None
        IN1.28 (opt) - Pre-Admit Cert (PAC) (ST)

    in1_29 : TS | None
        IN1.29 (opt) - Verification Date/Time (TS)

    in1_30 : list[XCN] | None
        IN1.30 (opt, rep) - Verification By (XCN)

    in1_31 : str | None
        IN1.31 (opt) - Type Of Agreement Code (IS)

    in1_32 : str | None
        IN1.32 (opt) - Billing Status (IS)

    in1_33 : str | None
        IN1.33 (opt) - Lifetime Reserve Days (NM)

    in1_34 : str | None
        IN1.34 (opt) - Delay Before L.R. Day (NM)

    in1_35 : str | None
        IN1.35 (opt) - Company Plan Code (IS)

    in1_36 : str | None
        IN1.36 (opt) - Policy Number (ST)

    in1_37 : CP | None
        IN1.37 (opt) - Policy Deductible (CP)

    in1_38 : CP | None
        IN1.38 (opt) - Policy Limit - Amount (CP)

    in1_39 : str | None
        IN1.39 (opt) - Policy Limit - Days (NM)

    in1_40 : CP | None
        IN1.40 (opt) - Room Rate - Semi-Private (CP)

    in1_41 : CP | None
        IN1.41 (opt) - Room Rate - Private (CP)

    in1_42 : CE | None
        IN1.42 (opt) - Insured's Employment Status (CE)

    in1_43 : str | None
        IN1.43 (opt) - Insured's Administrative Sex (IS)

    in1_44 : list[XAD] | None
        IN1.44 (opt, rep) - Insured's Employer's Address (XAD)

    in1_45 : str | None
        IN1.45 (opt) - Verification Status (ST)

    in1_46 : str | None
        IN1.46 (opt) - Prior Insurance Plan ID (IS)

    in1_47 : str | None
        IN1.47 (opt) - Coverage Type (IS)

    in1_48 : str | None
        IN1.48 (opt) - Handicap (IS)

    in1_49 : list[CX] | None
        IN1.49 (opt, rep) - Insured's ID Number (CX)

    in1_50 : str | None
        IN1.50 (opt) - Signature Code (IS)

    in1_51 : str | None
        IN1.51 (opt) - Signature Code Date (DT)

    in1_52 : str | None
        IN1.52 (opt) - Insured's Birth Place (ST)

    in1_53 : str | None
        IN1.53 (opt) - VIP Indicator (IS)
    """

    in1_1: str = Field(
        validation_alias=AliasChoices(
            "in1_1",
            "set_id_in1",
            "IN1.1",
        ),
        serialization_alias="IN1.1",
        title="Set ID - IN1",
        description="Item #426",
    )

    in1_2: CE = Field(
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="Insurance Plan ID",
        description="Item #368 | Table HL70072",
    )

    in1_3: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="Insurance Company ID",
        description="Item #428",
    )

    in1_4: Optional[List[XON]] = Field(
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

    in1_5: Optional[List[XAD]] = Field(
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

    in1_6: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_6",
            "insurance_co_contact_person",
            "IN1.6",
        ),
        serialization_alias="IN1.6",
        title="Insurance Co Contact Person",
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

    in1_9: Optional[List[XON]] = Field(
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

    in1_10: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_10",
            "insured_s_group_emp_id",
            "IN1.10",
        ),
        serialization_alias="IN1.10",
        title="Insured's Group Emp ID",
        description="Item #435",
    )

    in1_11: Optional[List[XON]] = Field(
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

    in1_14: Optional[AUI] = Field(
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

    in1_16: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_16",
            "name_of_insured",
            "IN1.16",
        ),
        serialization_alias="IN1.16",
        title="Name Of Insured",
        description="Item #441",
    )

    in1_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_17",
            "insured_s_relationship_to_patient",
            "IN1.17",
        ),
        serialization_alias="IN1.17",
        title="Insured's Relationship To Patient",
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
        title="Insured's Date Of Birth",
        description="Item #443",
    )

    in1_19: Optional[List[XAD]] = Field(
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
        title="Assignment Of Benefits",
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
        title="Coordination Of Benefits",
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
        title="Coord Of Ben. Priority",
        description="Item #447",
    )

    in1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_23",
            "notice_of_admission_flag",
            "IN1.23",
        ),
        serialization_alias="IN1.23",
        title="Notice Of Admission Flag",
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
        title="Notice Of Admission Date",
        description="Item #449",
    )

    in1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_25",
            "report_of_eligibility_flag",
            "IN1.25",
        ),
        serialization_alias="IN1.25",
        title="Report Of Eligibility Flag",
        description="Item #450 | Table HL70136",
    )

    in1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_26",
            "report_of_eligibility_date",
            "IN1.26",
        ),
        serialization_alias="IN1.26",
        title="Report Of Eligibility Date",
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

    in1_30: Optional[List[XCN]] = Field(
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
        title="Type Of Agreement Code",
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
            "delay_before_l_r_day",
            "IN1.34",
        ),
        serialization_alias="IN1.34",
        title="Delay Before L.R. Day",
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
            "insured_s_administrative_sex",
            "IN1.43",
        ),
        serialization_alias="IN1.43",
        title="Insured's Administrative Sex",
        description="Item #468 | Table HL70001",
    )

    in1_44: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_44",
            "insured_s_employer_s_address",
            "IN1.44",
        ),
        serialization_alias="IN1.44",
        title="Insured's Employer's Address",
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
        description="Item #1227 | Table HL70309",
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
        description="Item #753 | Table HL70295",
    )

    in1_49: Optional[List[CX]] = Field(
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

    in1_50: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_50",
            "signature_code",
            "IN1.50",
        ),
        serialization_alias="IN1.50",
        title="Signature Code",
        description="Item #1854 | Table HL70535",
    )

    in1_51: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_51",
            "signature_code_date",
            "IN1.51",
        ),
        serialization_alias="IN1.51",
        title="Signature Code Date",
        description="Item #1855",
    )

    in1_52: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_52",
            "insured_s_birth_place",
            "IN1.52",
        ),
        serialization_alias="IN1.52",
        title="Insured's Birth Place",
        description="Item #1899",
    )

    in1_53: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_53",
            "vip_indicator",
            "IN1.53",
        ),
        serialization_alias="IN1.53",
        title="VIP Indicator",
        description="Item #1852 | Table HL70099",
    )

    @field_validator("in1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("in1_12", "in1_13", "in1_24", "in1_26", "in1_51", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("in1_33", "in1_34", "in1_39", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
