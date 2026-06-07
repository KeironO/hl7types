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
    """HL7 v2 IN2 segment.

    Attributes
    ----------
    in2_1 : str | None
        IN2.1 (opt) - Insured's employee ID (ST)

    in2_2 : str | None
        IN2.2 (opt) - Insured's social security number (ST)

    in2_3 : str | None
        IN2.3 (opt) - Insured's employer name (CN)

    in2_4 : str | None
        IN2.4 (opt) - Employer information data (ID)

    in2_5 : str | None
        IN2.5 (opt) - Mail claim party (ID)

    in2_6 : str | None
        IN2.6 (opt) - Medicare health insurance card number (NM)

    in2_7 : PN | None
        IN2.7 (opt) - Medicaid case name (PN)

    in2_8 : str | None
        IN2.8 (opt) - Medicaid case number (NM)

    in2_9 : PN | None
        IN2.9 (opt) - Champus sponsor name (PN)

    in2_10 : str | None
        IN2.10 (opt) - Champus ID number (NM)

    in2_11 : str | None
        IN2.11 (opt) - Dependent of champus recipient (ID)

    in2_12 : str | None
        IN2.12 (opt) - Champus organization (ST)

    in2_13 : str | None
        IN2.13 (opt) - Champus station (ST)

    in2_14 : str | None
        IN2.14 (opt) - Champus service (ID)

    in2_15 : str | None
        IN2.15 (opt) - Champus rank / grade (ID)

    in2_16 : str | None
        IN2.16 (opt) - Champus status (ID)

    in2_17 : str | None
        IN2.17 (opt) - Champus retire date (DT)

    in2_18 : str | None
        IN2.18 (opt) - Champus non-availability certification on file (ID)

    in2_19 : str | None
        IN2.19 (opt) - Baby coverage (ID)

    in2_20 : str | None
        IN2.20 (opt) - Combine baby bill (ID)

    in2_21 : str | None
        IN2.21 (opt) - Blood deductible (NM)

    in2_22 : PN | None
        IN2.22 (opt) - Special coverage approval name (PN)

    in2_23 : str | None
        IN2.23 (opt) - Special coverage approval title (ST)

    in2_24 : list[str] | None
        IN2.24 (opt, rep) - Non-covered insurance code (ID)

    in2_25 : str | None
        IN2.25 (opt) - Payor ID (ST)

    in2_26 : str | None
        IN2.26 (opt) - Payor subscriber ID (ST)

    in2_27 : str | None
        IN2.27 (opt) - Eligibility source (ID)

    in2_28 : list[str] | None
        IN2.28 (opt, rep) - Room coverage type / amount (CM)

    in2_29 : list[str] | None
        IN2.29 (opt, rep) - Policy type / amount (CM)

    in2_30 : str | None
        IN2.30 (opt) - Daily deductible (CM)
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
        description="Item #472",
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
        description="Item #473",
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
        description="Item #474",
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
        description="Item #475 | Table HL70139",
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
        description="Item #476 | Table HL70137",
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
        description="Item #477",
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
        description="Item #478",
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
        description="Item #479",
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
        description="Item #480",
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
        description="Item #481",
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
        description="Item #482",
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
        description="Item #483",
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
        description="Item #484",
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
        description="Item #485 | Table HL70140",
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
        description="Item #486 | Table HL70141",
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
        description="Item #487 | Table HL70142",
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
        description="Item #488",
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
        description="Item #489 | Table HL70136",
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
        description="Item #490 | Table HL70136",
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
        description="Item #491 | Table HL70136",
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
        description="Item #531",
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
        description="Item #493",
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
        description="Item #494",
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
        description="Item #495 | Table HL70143",
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
        description="Item #496",
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
        description="Item #497",
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
        description="Item #498 | Table HL70144",
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
        description="Item #499 | Table HL70145",
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
        description="Item #500 | Table HL70147",
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
        description="Item #501",
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
