"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PD1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class PD1(BaseModel):
    """HL7 v2 PD1 segment."""

    pd1_1: Optional[List[str]] = Field(
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

    pd1_2: Optional[str] = Field(
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

    pd1_3: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_3",
            "patient_primary_facility",
            "PD1.3",
        ),
        serialization_alias="PD1.3",
        title="Patient Primary Facility",
        description="Item #756",
    )

    pd1_4: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_4",
            "patient_primary_care_provider_name_id_no",
            "PD1.4",
        ),
        serialization_alias="PD1.4",
        title="Patient Primary Care Provider Name & ID No.",
        description="Item #757",
    )

    pd1_5: Optional[str] = Field(
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

    pd1_6: Optional[str] = Field(
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

    pd1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_7",
            "living_will",
            "PD1.7",
        ),
        serialization_alias="PD1.7",
        title="Living Will",
        description="Item #759 | Table HL70315",
    )

    pd1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_8",
            "organ_donor",
            "PD1.8",
        ),
        serialization_alias="PD1.8",
        title="Organ Donor",
        description="Item #760 | Table HL70316",
    )

    pd1_9: Optional[str] = Field(
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

    pd1_10: Optional[List[CX]] = Field(
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

    pd1_11: Optional[CE] = Field(
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

    pd1_12: Optional[str] = Field(
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

    model_config = {"populate_by_name": True}
