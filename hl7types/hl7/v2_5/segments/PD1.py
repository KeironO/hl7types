"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PD1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PD1(HL7Model):
    """Patient Additional Demographic (S3.4.10).

    Attributes
    ----------
    pd1_1 : list[str] | None
        PD1.1 - Living Dependency (IS) O rep S3.4.5.17 | 0223 - Living Dependency

    pd1_2 : str | None
        PD1.2 - Living Arrangement (IS) O S3.4.5.21 | 0220 - Living Arrangement

    pd1_3 : list[XON] | None
        PD1.3 - Patient Primary Facility (XON) O rep S3.4.10.3

    pd1_4 : list[XCN] | None
        PD1.4 - Patient Primary Care Provider Name & ID No. (XCN) O rep S3.4.10.4

    pd1_5 : str | None
        PD1.5 - Student Indicator (IS) O S3.4.5.24 | 0231 - Student Status

    pd1_6 : str | None
        PD1.6 - Handicap (IS) O S3.4.5.36 | 0295 - Handicap

    pd1_7 : str | None
        PD1.7 - Living Will Code (IS) O S3.4.4.43 | 0315 - Living Will Code

    pd1_8 : str | None
        PD1.8 - Organ Donor Code (IS) O S3.4.4.44 | 0316 - Organ Donor Code

    pd1_9 : str | None
        PD1.9 - Separate Bill (ID) O S3.4.10.9 | 0136 - Yes/no indicator

    pd1_10 : list[CX] | None
        PD1.10 - Duplicate Patient (CX) O rep S3.4.10.10

    pd1_11 : CE | None
        PD1.11 - Publicity Code (CE) O S3.4.5.22 | 0215 - Publicity Code

    pd1_12 : str | None
        PD1.12 - Protection Indicator (ID) O S3.4.5.23 | 0136 - Yes/no indicator

    pd1_13 : str | None
        PD1.13 - Protection Indicator Effective Date (DT) O S3.4.10.13

    pd1_14 : list[XON] | None
        PD1.14 - Place of Worship (XON) O rep S3.4.10.14

    pd1_15 : list[CE] | None
        PD1.15 - Advance Directive Code (CE) O rep S3.4.10.15 | 0435 - Advance Directive Code

    pd1_16 : str | None
        PD1.16 - Immunization Registry Status (IS) O S3.4.10.16 | 0441 - Immunization Registry Status

    pd1_17 : str | None
        PD1.17 - Immunization Registry Status Effective Date (DT) O S3.4.10.17

    pd1_18 : str | None
        PD1.18 - Publicity Code Effective Date (DT) O S3.4.10.18

    pd1_19 : str | None
        PD1.19 - Military Branch (IS) O S3.4.10.19 | 0140 - Military Service

    pd1_20 : str | None
        PD1.20 - Military Rank/Grade (IS) O S3.4.10.20 | 0141 - Military Rank/Grade

    pd1_21 : str | None
        PD1.21 - Military Status (IS) O S3.4.10.21 | 0142 - Military Status
    """

    pd1_1: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_1",
            "living_dependency",
            "PD1.1",
        ),
        serialization_alias="PD1.1",
        title="Living Dependency",
        description="O | Item #00755 | Table 0223 - Living Dependency | LEN:2",
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
        description="O | Item #00742 | Table 0220 - Living Arrangement | LEN:2",
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
        description="O | Item #00756",
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
        description="O | Item #00757",
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
        description="O | Item #00745 | Table 0231 - Student Status | LEN:2",
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
        description="O | Item #00753 | Table 0295 - Handicap | LEN:2",
    )

    pd1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_7",
            "living_will_code",
            "PD1.7",
        ),
        serialization_alias="PD1.7",
        title="Living Will Code",
        description="O | Item #00759 | Table 0315 - Living Will Code | LEN:2",
    )

    pd1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_8",
            "organ_donor_code",
            "PD1.8",
        ),
        serialization_alias="PD1.8",
        title="Organ Donor Code",
        description="O | Item #00760 | Table 0316 - Organ Donor Code | LEN:2",
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
        description="O | Item #00761 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #00762",
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
        description="O | Item #00743 | Table 0215 - Publicity Code",
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
        description="O | Item #00744 | Table 0136 - Yes/no indicator | LEN:1",
    )

    pd1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_13",
            "protection_indicator_effective_date",
            "PD1.13",
        ),
        serialization_alias="PD1.13",
        title="Protection Indicator Effective Date",
        description="O | Item #01566 | LEN:8",
    )

    pd1_14: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_14",
            "place_of_worship",
            "PD1.14",
        ),
        serialization_alias="PD1.14",
        title="Place of Worship",
        description="O | Item #01567",
    )

    pd1_15: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_15",
            "advance_directive_code",
            "PD1.15",
        ),
        serialization_alias="PD1.15",
        title="Advance Directive Code",
        description="O | Item #01568 | Table 0435 - Advance Directive Code",
    )

    pd1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_16",
            "immunization_registry_status",
            "PD1.16",
        ),
        serialization_alias="PD1.16",
        title="Immunization Registry Status",
        description=(
            "O | Item #01569 | Table 0441 - Immunization Registry Status | LEN:1"
        ),
    )

    pd1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_17",
            "immunization_registry_status_effective_date",
            "PD1.17",
        ),
        serialization_alias="PD1.17",
        title="Immunization Registry Status Effective Date",
        description="O | Item #01570 | LEN:8",
    )

    pd1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_18",
            "publicity_code_effective_date",
            "PD1.18",
        ),
        serialization_alias="PD1.18",
        title="Publicity Code Effective Date",
        description="O | Item #01571 | LEN:8",
    )

    pd1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_19",
            "military_branch",
            "PD1.19",
        ),
        serialization_alias="PD1.19",
        title="Military Branch",
        description="O | Item #01572 | Table 0140 - Military Service | LEN:5",
    )

    pd1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_20",
            "military_rank_grade",
            "PD1.20",
        ),
        serialization_alias="PD1.20",
        title="Military Rank/Grade",
        description=(
            "O | Item #00486 | Table 0141 - Military Rank/Grade | LEN:2"
        ),
    )

    pd1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pd1_21",
            "military_status",
            "PD1.21",
        ),
        serialization_alias="PD1.21",
        title="Military Status",
        description="O | Item #01573 | Table 0142 - Military Status | LEN:3",
    )

    @field_validator("pd1_13", "pd1_17", "pd1_18", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
