"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PD1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.XON import XON


class PD1(BaseModel):
    """HL7 v2 PD1 segment."""

    pd1_1: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_1",
            "living_dependency",
            "PD1.1",
        ),
        serialization_alias="PD1.1",
        title="Living Dependency",
        description="Item #755 | Table HL70223",
    )

    pd1_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_2",
            "living_arrangement",
            "PD1.2",
        ),
        serialization_alias="PD1.2",
        title="Living Arrangement",
        description="Item #742 | Table HL70220",
    )

    pd1_3: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_3",
            "patient_primary_facility",
            "PD1.3",
        ),
        serialization_alias="PD1.3",
        title="Patient Primary Facility",
        description="Item #756 | Table HL70204",
    )

    pd1_5: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_5",
            "student_indicator",
            "PD1.5",
        ),
        serialization_alias="PD1.5",
        title="Student Indicator",
        description="Item #745 | Table HL70231",
    )

    pd1_6: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_6",
            "handicap",
            "PD1.6",
        ),
        serialization_alias="PD1.6",
        title="Handicap",
        description="Item #753 | Table HL70295",
    )

    pd1_7: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_7",
            "living_will_code",
            "PD1.7",
        ),
        serialization_alias="PD1.7",
        title="Living Will Code",
        description="Item #759 | Table HL70315",
    )

    pd1_8: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_8",
            "organ_donor_code",
            "PD1.8",
        ),
        serialization_alias="PD1.8",
        title="Organ Donor Code",
        description="Item #760 | Table HL70316",
    )

    pd1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_9",
            "separate_bill",
            "PD1.9",
        ),
        serialization_alias="PD1.9",
        title="Separate Bill",
        description="Item #761 | Table HL70136",
    )

    pd1_10: list[CX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_10",
            "duplicate_patient",
            "PD1.10",
        ),
        serialization_alias="PD1.10",
        title="Duplicate Patient",
        description="Item #762",
    )

    pd1_11: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_11",
            "publicity_code",
            "PD1.11",
        ),
        serialization_alias="PD1.11",
        title="Publicity Code",
        description="Item #743 | Table HL70215",
    )

    pd1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_12",
            "protection_indicator",
            "PD1.12",
        ),
        serialization_alias="PD1.12",
        title="Protection Indicator",
        description="Item #744 | Table HL70136",
    )

    pd1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_13",
            "protection_indicator_effective_date",
            "PD1.13",
        ),
        serialization_alias="PD1.13",
        title="Protection Indicator Effective Date",
        description="Item #1566",
    )

    pd1_14: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_14",
            "place_of_worship",
            "PD1.14",
        ),
        serialization_alias="PD1.14",
        title="Place of Worship",
        description="Item #1567",
    )

    pd1_15: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_15",
            "advance_directive_code",
            "PD1.15",
        ),
        serialization_alias="PD1.15",
        title="Advance Directive Code",
        description="Item #1548 | Table HL70435",
    )

    pd1_16: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_16",
            "immunization_registry_status",
            "PD1.16",
        ),
        serialization_alias="PD1.16",
        title="Immunization Registry Status",
        description="Item #1569 | Table HL70441",
    )

    pd1_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_17",
            "immunization_registry_status_effective_date",
            "PD1.17",
        ),
        serialization_alias="PD1.17",
        title="Immunization Registry Status Effective Date",
        description="Item #1570",
    )

    pd1_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_18",
            "publicity_code_effective_date",
            "PD1.18",
        ),
        serialization_alias="PD1.18",
        title="Publicity Code Effective Date",
        description="Item #1571",
    )

    pd1_19: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_19",
            "military_branch",
            "PD1.19",
        ),
        serialization_alias="PD1.19",
        title="Military Branch",
        description="Item #1572 | Table HL70140",
    )

    pd1_20: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_20",
            "military_rank_grade",
            "PD1.20",
        ),
        serialization_alias="PD1.20",
        title="Military Rank/Grade",
        description="Item #486 | Table HL70141",
    )

    pd1_21: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_21",
            "military_status",
            "PD1.21",
        ),
        serialization_alias="PD1.21",
        title="Military Status",
        description="Item #1573 | Table HL70142",
    )

    pd1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_22",
            "advance_directive_last_verified_date",
            "PD1.22",
        ),
        serialization_alias="PD1.22",
        title="Advance Directive Last Verified Date",
        description="Item #2141",
    )

    model_config = {"populate_by_name": True}
