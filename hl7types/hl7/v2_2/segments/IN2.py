"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: IN2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.PN import PN


class IN2(HL7Model):
    """INSURANCE ADDITIONAL INFO (S6.4.6).

    Attributes
    ----------
    in2_1 : str | None
        IN2.1 - Insured's employee ID (ST) NA S6.4.6.1

    in2_2 : str | None
        IN2.2 - Insured's social security number (ST) NA S6.4.6.2

    in2_3 : str | None
        IN2.3 - Insured's employer name (CN) NA S6.4.6.3

    in2_4 : str | None
        IN2.4 - Employer information data (ID) NA S6.4.6.4 | 0139 - EMPLOYER INFORMATION DATA

    in2_5 : str | None
        IN2.5 - Mail claim party (ID) NA S6.4.6.5 | 0137 - MAIL CLAIM PARTY

    in2_6 : str | None
        IN2.6 - Medicare health insurance card number (NM) NA S6.4.6.6

    in2_7 : PN | None
        IN2.7 - Medicaid case name (PN) NA S6.4.6.7

    in2_8 : str | None
        IN2.8 - Medicaid case number (NM) NA S6.4.6.8

    in2_9 : PN | None
        IN2.9 - Champus sponsor name (PN) NA S6.4.6.9

    in2_10 : str | None
        IN2.10 - Champus ID number (NM) NA S6.4.6.10

    in2_11 : str | None
        IN2.11 - Dependent of champus recipient (ID) NA S6.4.6.11

    in2_12 : str | None
        IN2.12 - Champus organization (ST) NA S6.4.6.12

    in2_13 : str | None
        IN2.13 - Champus station (ST) NA S6.4.6.13

    in2_14 : str | None
        IN2.14 - Champus service (ID) NA S6.4.6.14 | 0140 - CHAMPUS SERVICE

    in2_15 : str | None
        IN2.15 - Champus rank / grade (ID) NA S6.4.6.15 | 0141 - CHAMPUS RANK/GRADE

    in2_16 : str | None
        IN2.16 - Champus status (ID) NA S6.4.6.16 | 0142 - CHAMPUS STATE

    in2_17 : str | None
        IN2.17 - Champus retire date (DT) NA S6.4.6.17

    in2_18 : str | None
        IN2.18 - Champus non-availability certification on file (ID) NA S6.4.6.18 | 0136 - Y/N Indicator

    in2_19 : str | None
        IN2.19 - Baby coverage (ID) NA S6.4.6.19 | 0136 - Y/N Indicator

    in2_20 : str | None
        IN2.20 - Combine baby bill (ID) NA S6.4.6.20 | 0136 - Y/N Indicator

    in2_21 : str | None
        IN2.21 - Blood deductible (NM) NA S6.4.9.2

    in2_22 : PN | None
        IN2.22 - Special coverage approval name (PN) NA S6.4.6.22

    in2_23 : str | None
        IN2.23 - Special coverage approval title (ST) NA S6.4.6.23

    in2_24 : list[str] | None
        IN2.24 - Non-covered insurance code (ID) NA rep S6.4.6.24 | 0143 - NON-COVEREDINSURANCE CODE

    in2_25 : str | None
        IN2.25 - Payor ID (ST) NA S6.4.6.25

    in2_26 : str | None
        IN2.26 - Payor subscriber ID (ST) NA S6.4.6.26

    in2_27 : str | None
        IN2.27 - Eligibility source (ID) NA S6.4.6.27 | 0144 - ELIGIBILITY SOURCE

    in2_28 : list[str] | None
        IN2.28 - Room coverage type / amount (CM) NA rep S6.4.6.28 | 0145 - Room Type

    in2_29 : list[str] | None
        IN2.29 - Policy type / amount (CM) NA rep S6.4.6.29 | 0147 - POLICY TYPE

    in2_30 : str | None
        IN2.30 - Daily deductible (CM) NA S6.4.6.30
    """

    in2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_1",
            "insured_s_employee_id",
            "IN2.1",
        ),
        serialization_alias="IN2.1",
        title="Insured's employee ID",
        description="NA | Item #00472 | LEN:15",
    )

    in2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_2",
            "insured_s_social_security_number",
            "IN2.2",
        ),
        serialization_alias="IN2.2",
        title="Insured's social security number",
        description="NA | Item #00473 | LEN:9",
    )

    in2_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_3",
            "insured_s_employer_name",
            "IN2.3",
        ),
        serialization_alias="IN2.3",
        title="Insured's employer name",
        description="NA | Item #00474",
    )

    in2_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_4",
            "employer_information_data",
            "IN2.4",
        ),
        serialization_alias="IN2.4",
        title="Employer information data",
        description=(
            "NA | Item #00475 | Table 0139 - EMPLOYER INFORMATION DATA | LEN:1"
        ),
    )

    in2_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_5",
            "mail_claim_party",
            "IN2.5",
        ),
        serialization_alias="IN2.5",
        title="Mail claim party",
        description="NA | Item #00476 | Table 0137 - MAIL CLAIM PARTY | LEN:1",
    )

    in2_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_6",
            "medicare_health_insurance_card_number",
            "IN2.6",
        ),
        serialization_alias="IN2.6",
        title="Medicare health insurance card number",
        description="NA | Item #00477 | LEN:15",
    )

    in2_7: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_7",
            "medicaid_case_name",
            "IN2.7",
        ),
        serialization_alias="IN2.7",
        title="Medicaid case name",
        description="NA | Item #00478",
    )

    in2_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_8",
            "medicaid_case_number",
            "IN2.8",
        ),
        serialization_alias="IN2.8",
        title="Medicaid case number",
        description="NA | Item #00479 | LEN:15",
    )

    in2_9: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_9",
            "champus_sponsor_name",
            "IN2.9",
        ),
        serialization_alias="IN2.9",
        title="Champus sponsor name",
        description="NA | Item #00480",
    )

    in2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_10",
            "champus_id_number",
            "IN2.10",
        ),
        serialization_alias="IN2.10",
        title="Champus ID number",
        description="NA | Item #00481 | LEN:20",
    )

    in2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_11",
            "dependent_of_champus_recipient",
            "IN2.11",
        ),
        serialization_alias="IN2.11",
        title="Dependent of champus recipient",
        description="NA | Item #00482 | LEN:1",
    )

    in2_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_12",
            "champus_organization",
            "IN2.12",
        ),
        serialization_alias="IN2.12",
        title="Champus organization",
        description="NA | Item #00483 | LEN:25",
    )

    in2_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_13",
            "champus_station",
            "IN2.13",
        ),
        serialization_alias="IN2.13",
        title="Champus station",
        description="NA | Item #00484 | LEN:25",
    )

    in2_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_14",
            "champus_service",
            "IN2.14",
        ),
        serialization_alias="IN2.14",
        title="Champus service",
        description="NA | Item #00485 | Table 0140 - CHAMPUS SERVICE | LEN:14",
    )

    in2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_15",
            "champus_rank_grade",
            "IN2.15",
        ),
        serialization_alias="IN2.15",
        title="Champus rank / grade",
        description=(
            "NA | Item #00486 | Table 0141 - CHAMPUS RANK/GRADE | LEN:2"
        ),
    )

    in2_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_16",
            "champus_status",
            "IN2.16",
        ),
        serialization_alias="IN2.16",
        title="Champus status",
        description="NA | Item #00487 | Table 0142 - CHAMPUS STATE | LEN:3",
    )

    in2_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_17",
            "champus_retire_date",
            "IN2.17",
        ),
        serialization_alias="IN2.17",
        title="Champus retire date",
        description="NA | Item #00488 | LEN:8",
    )

    in2_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_18",
            "champus_non_availability_certification_on_file",
            "IN2.18",
        ),
        serialization_alias="IN2.18",
        title="Champus non-availability certification on file",
        description="NA | Item #00489 | Table 0136 - Y/N Indicator | LEN:1",
    )

    in2_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_19",
            "baby_coverage",
            "IN2.19",
        ),
        serialization_alias="IN2.19",
        title="Baby coverage",
        description="NA | Item #00490 | Table 0136 - Y/N Indicator | LEN:1",
    )

    in2_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_20",
            "combine_baby_bill",
            "IN2.20",
        ),
        serialization_alias="IN2.20",
        title="Combine baby bill",
        description="NA | Item #00491 | Table 0136 - Y/N Indicator | LEN:1",
    )

    in2_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_21",
            "blood_deductible",
            "IN2.21",
        ),
        serialization_alias="IN2.21",
        title="Blood deductible",
        description="NA | Item #00531 | LEN:1",
    )

    in2_22: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_22",
            "special_coverage_approval_name",
            "IN2.22",
        ),
        serialization_alias="IN2.22",
        title="Special coverage approval name",
        description="NA | Item #00493",
    )

    in2_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_23",
            "special_coverage_approval_title",
            "IN2.23",
        ),
        serialization_alias="IN2.23",
        title="Special coverage approval title",
        description="NA | Item #00494 | LEN:30",
    )

    in2_24: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_24",
            "non_covered_insurance_code",
            "IN2.24",
        ),
        serialization_alias="IN2.24",
        title="Non-covered insurance code",
        description=(
            "NA | Item #00495 | Table 0143 - NON-COVEREDINSURANCE CODE | LEN:8"
        ),
    )

    in2_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_25",
            "payor_id",
            "IN2.25",
        ),
        serialization_alias="IN2.25",
        title="Payor ID",
        description="NA | Item #00496 | LEN:6",
    )

    in2_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_26",
            "payor_subscriber_id",
            "IN2.26",
        ),
        serialization_alias="IN2.26",
        title="Payor subscriber ID",
        description="NA | Item #00497 | LEN:6",
    )

    in2_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_27",
            "eligibility_source",
            "IN2.27",
        ),
        serialization_alias="IN2.27",
        title="Eligibility source",
        description=(
            "NA | Item #00498 | Table 0144 - ELIGIBILITY SOURCE | LEN:1"
        ),
    )

    in2_28: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_28",
            "room_coverage_type_amount",
            "IN2.28",
        ),
        serialization_alias="IN2.28",
        title="Room coverage type / amount",
        description="NA | Item #00499 | Table 0145 - Room Type",
    )

    in2_29: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_29",
            "policy_type_amount",
            "IN2.29",
        ),
        serialization_alias="IN2.29",
        title="Policy type / amount",
        description="NA | Item #00500 | Table 0147 - POLICY TYPE",
    )

    in2_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in2_30",
            "daily_deductible",
            "IN2.30",
        ),
        serialization_alias="IN2.30",
        title="Daily deductible",
        description="NA | Item #00501",
    )

    @field_validator("in2_6", "in2_8", "in2_10", "in2_21", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("in2_17", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
