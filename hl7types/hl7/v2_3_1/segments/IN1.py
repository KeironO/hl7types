"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: IN1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
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

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class IN1(HL7Model):
    """IN1 - insurance segment (S6.4.6).

    Attributes
    ----------
    in1_1 : str
        IN1.1 - Set ID - IN1 (SI) R S6.4.6.1

    in1_2 : CE
        IN1.2 - Insurance Plan ID (CE) R S6.4.6.2 | 0072 - Insurance Plan ID

    in1_3 : list[CX]
        IN1.3 - Insurance Company ID (CX) R rep S6.4.6.3

    in1_4 : list[XON] | None
        IN1.4 - Insurance Company Name (XON) O rep S6.4.6.4

    in1_5 : list[XAD] | None
        IN1.5 - Insurance Company Address (XAD) O rep S6.4.6.5

    in1_6 : list[XPN] | None
        IN1.6 - Insurance Co Contact Person (XPN) O rep S6.4.6.6

    in1_7 : list[XTN] | None
        IN1.7 - Insurance Co Phone Number (XTN) O rep S6.4.6.7

    in1_8 : str | None
        IN1.8 - Group Number (ST) O S6.4.6.8

    in1_9 : list[XON] | None
        IN1.9 - Group Name (XON) O rep S6.4.6.9

    in1_10 : list[CX] | None
        IN1.10 - Insured’s Group Emp ID (CX) O rep S6.4.6.10

    in1_11 : list[XON] | None
        IN1.11 - Insured’s Group Emp Name (XON) O rep S6.4.6.11

    in1_12 : str | None
        IN1.12 - Plan Effective Date (DT) O S6.4.6.12

    in1_13 : str | None
        IN1.13 - Plan Expiration Date (DT) O S6.4.6.13

    in1_14 : AUI | None
        IN1.14 - Authorization Information (AUI) O S6.4.6.14

    in1_15 : str | None
        IN1.15 - Plan Type (IS) O S6.4.6.15 | 0086 - Plan Type

    in1_16 : list[XPN] | None
        IN1.16 - Name Of Insured (XPN) O rep S6.4.6.16

    in1_17 : CE | None
        IN1.17 - Insured’s Relationship To Patient (CE) O S6.4.6.17 | 0063 - Relationship

    in1_18 : TS | None
        IN1.18 - Insured’s Date Of Birth (TS) O S6.4.6.18

    in1_19 : list[XAD] | None
        IN1.19 - Insured’s Address (XAD) O rep S6.4.6.19

    in1_20 : str | None
        IN1.20 - Assignment Of Benefits (IS) O S6.4.6.20 | 0135 - Assignment of benefits

    in1_21 : str | None
        IN1.21 - Coordination Of Benefits (IS) O S6.4.6.21 | 0173 - Coordination of benefits

    in1_22 : str | None
        IN1.22 - Coord Of Ben. Priority (ST) O S6.4.6.22

    in1_23 : str | None
        IN1.23 - Notice Of Admission Flag (ID) O S6.4.6.23 | 0136 - Yes/no indicator

    in1_24 : str | None
        IN1.24 - Notice Of Admission Date (DT) O S6.4.6.24

    in1_25 : str | None
        IN1.25 - Report Of Eligibility Flag (ID) O S6.4.6.25 | 0136 - Yes/no indicator

    in1_26 : str | None
        IN1.26 - Report Of Eligibility Date (DT) O S6.4.6.26

    in1_27 : str | None
        IN1.27 - Release Information Code (IS) O S6.4.6.27 | 0093 - Release information

    in1_28 : str | None
        IN1.28 - Pre-Admit Cert (PAC) (ST) O S6.4.6.28

    in1_29 : TS | None
        IN1.29 - Verification Date/Time (TS) O S6.4.6.29

    in1_30 : list[XCN] | None
        IN1.30 - Verification By (XCN) O rep S6.4.6.30

    in1_31 : str | None
        IN1.31 - Type Of Agreement Code (IS) O S6.4.6.31 | 0098 - Type of agreement

    in1_32 : str | None
        IN1.32 - Billing Status (IS) O S6.4.6.32 | 0022 - Billing Status

    in1_33 : str | None
        IN1.33 - Lifetime Reserve Days (NM) O S6.4.6.33

    in1_34 : str | None
        IN1.34 - Delay Before L.R. Day (NM) O S6.4.6.34

    in1_35 : str | None
        IN1.35 - Company Plan Code (IS) O S6.4.6.35 | 0042 - Company Plan Code

    in1_36 : str | None
        IN1.36 - Policy Number (ST) O S6.4.6.36

    in1_37 : CP | None
        IN1.37 - Policy Deductible (CP) O S6.4.6.37

    in1_38 : CP | None
        IN1.38 - Policy Limit - Amount (CP) O S6.4.6.38

    in1_39 : str | None
        IN1.39 - Policy Limit - Days (NM) O S6.4.6.39

    in1_40 : CP | None
        IN1.40 - Room Rate - Semi-Private (CP) O S6.4.6.40

    in1_41 : CP | None
        IN1.41 - Room Rate - Private (CP) O S6.4.6.41

    in1_42 : CE | None
        IN1.42 - Insured’s Employment Status (CE) O S6.4.6.42 | 0066 - Employment Status

    in1_43 : str | None
        IN1.43 - Insured’s Sex (IS) O S6.4.6.43 | 0001 - Sex

    in1_44 : list[XAD] | None
        IN1.44 - Insured’s Employer’s Address (XAD) O rep S6.4.6.44

    in1_45 : str | None
        IN1.45 - Verification Status (ST) O S6.4.6.45

    in1_46 : str | None
        IN1.46 - Prior Insurance Plan ID (IS) O S6.4.6.46 | 0072 - Insurance Plan ID

    in1_47 : str | None
        IN1.47 - Coverage Type (IS) O S6.4.6.47 | 0309 - Coverage type

    in1_48 : str | None
        IN1.48 - Handicap (IS) O S6.4.6.48 | 0295 - Handicap

    in1_49 : list[CX] | None
        IN1.49 - Insured’s ID Number (CX) O rep S6.4.6.49
    """

    in1_1: str = Field(
        validation_alias=AliasChoices(
            "in1_1",
            "set_id_in1",
            "IN1.1",
        ),
        serialization_alias="IN1.1",
        title="Set ID - IN1",
        description="R | Item #00426 | LEN:4",
    )

    in1_2: CE = Field(
        validation_alias=AliasChoices(
            "in1_2",
            "insurance_plan_id",
            "IN1.2",
        ),
        serialization_alias="IN1.2",
        title="Insurance Plan ID",
        description="R | Item #00368 | Table 0072 - Insurance Plan ID",
    )

    in1_3: List[CX] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "in1_3",
            "insurance_company_id",
            "IN1.3",
        ),
        serialization_alias="IN1.3",
        title="Insurance Company ID",
        description="R | Item #00428",
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
        description="O | Item #00429",
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
        description="O | Item #00430",
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
        description="O | Item #00431",
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
        description="O | Item #00432",
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
        description="O | Item #00433 | LEN:12",
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
        description="O | Item #00434",
    )

    in1_10: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_10",
            "insured_s_group_emp_id",
            "IN1.10",
        ),
        serialization_alias="IN1.10",
        title="Insured’s Group Emp ID",
        description="O | Item #00435",
    )

    in1_11: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_11",
            "insured_s_group_emp_name",
            "IN1.11",
        ),
        serialization_alias="IN1.11",
        title="Insured’s Group Emp Name",
        description="O | Item #00436",
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
        description="O | Item #00437 | LEN:8",
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
        description="O | Item #00438 | LEN:8",
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
        description="O | Item #00439",
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
        description="O | Item #00440 | Table 0086 - Plan Type | LEN:3",
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
        description="O | Item #00441",
    )

    in1_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_17",
            "insured_s_relationship_to_patient",
            "IN1.17",
        ),
        serialization_alias="IN1.17",
        title="Insured’s Relationship To Patient",
        description="O | Item #00442 | Table 0063 - Relationship",
    )

    in1_18: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_18",
            "insured_s_date_of_birth",
            "IN1.18",
        ),
        serialization_alias="IN1.18",
        title="Insured’s Date Of Birth",
        description="O | Item #00443",
    )

    in1_19: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_19",
            "insured_s_address",
            "IN1.19",
        ),
        serialization_alias="IN1.19",
        title="Insured’s Address",
        description="O | Item #00444",
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
        description=(
            "O | Item #00445 | Table 0135 - Assignment of benefits | LEN:2"
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
        title="Coordination Of Benefits",
        description=(
            "O | Item #00446 | Table 0173 - Coordination of benefits | LEN:2"
        ),
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
        description="O | Item #00447 | LEN:2",
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
        description="O | Item #00448 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #00449 | LEN:8",
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
        description="O | Item #00450 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #00451 | LEN:8",
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
        description=(
            "O | Item #00452 | Table 0093 - Release information | LEN:2"
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
        title="Pre-Admit Cert (PAC)",
        description="O | Item #00453 | LEN:15",
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
        description="O | Item #00454",
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
        description="O | Item #00455",
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
        description="O | Item #00456 | Table 0098 - Type of agreement | LEN:2",
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
        description="O | Item #00457 | Table 0022 - Billing Status | LEN:2",
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
        description="O | Item #00458 | LEN:4",
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
        description="O | Item #00459 | LEN:4",
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
        description="O | Item #00460 | Table 0042 - Company Plan Code | LEN:8",
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
        description="O | Item #00461 | LEN:15",
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
        description="O | Item #00462",
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
        description="O | Item #00463",
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
        description="O | Item #00464 | LEN:4",
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
        description="O | Item #00465",
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
        description="O | Item #00466",
    )

    in1_42: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_42",
            "insured_s_employment_status",
            "IN1.42",
        ),
        serialization_alias="IN1.42",
        title="Insured’s Employment Status",
        description="O | Item #00467 | Table 0066 - Employment Status",
    )

    in1_43: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_43",
            "insured_s_sex",
            "IN1.43",
        ),
        serialization_alias="IN1.43",
        title="Insured’s Sex",
        description="O | Item #00468 | Table 0001 - Sex | LEN:1",
    )

    in1_44: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_44",
            "insured_s_employer_s_address",
            "IN1.44",
        ),
        serialization_alias="IN1.44",
        title="Insured’s Employer’s Address",
        description="O | Item #00469",
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
        description="O | Item #00470 | LEN:2",
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
        description="O | Item #00471 | Table 0072 - Insurance Plan ID | LEN:8",
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
        description="O | Item #01227 | Table 0309 - Coverage type | LEN:3",
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
        description="O | Item #00753 | Table 0295 - Handicap | LEN:2",
    )

    in1_49: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in1_49",
            "insured_s_id_number",
            "IN1.49",
        ),
        serialization_alias="IN1.49",
        title="Insured’s ID Number",
        description="O | Item #01230",
    )

    @field_validator("in1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("in1_12", "in1_13", "in1_24", "in1_26", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("in1_33", "in1_34", "in1_39", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
