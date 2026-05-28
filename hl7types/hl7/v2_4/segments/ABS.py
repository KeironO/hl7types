"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ABS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class ABS(BaseModel):
    """HL7 v2 ABS segment."""

    abs_1: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_1",
            "discharge_care_provider",
            "ABS.1",
        ),
        serialization_alias="ABS.1",
        title="Discharge Care Provider",
        description="Item #1514 | Table HL70010",
    )

    abs_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_2",
            "transfer_medical_service_code",
            "ABS.2",
        ),
        serialization_alias="ABS.2",
        title="Transfer Medical Service Code",
        description="Item #1515 | Table HL70069",
    )

    abs_3: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_3",
            "severity_of_illness_code",
            "ABS.3",
        ),
        serialization_alias="ABS.3",
        title="Severity of Illness Code",
        description="Item #1516 | Table HL70421",
    )

    abs_4: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_4",
            "date_time_of_attestation",
            "ABS.4",
        ),
        serialization_alias="ABS.4",
        title="Date/Time of Attestation",
        description="Item #1517",
    )

    abs_5: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_5",
            "attested_by",
            "ABS.5",
        ),
        serialization_alias="ABS.5",
        title="Attested By",
        description="Item #1518",
    )

    abs_6: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_6",
            "triage_code",
            "ABS.6",
        ),
        serialization_alias="ABS.6",
        title="Triage Code",
        description="Item #1519 | Table HL70422",
    )

    abs_7: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_7",
            "abstract_completion_date_time",
            "ABS.7",
        ),
        serialization_alias="ABS.7",
        title="Abstract Completion Date/Time",
        description="Item #1520",
    )

    abs_8: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_8",
            "abstracted_by",
            "ABS.8",
        ),
        serialization_alias="ABS.8",
        title="Abstracted By",
        description="Item #1521",
    )

    abs_9: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_9",
            "case_category_code",
            "ABS.9",
        ),
        serialization_alias="ABS.9",
        title="Case Category Code",
        description="Item #1522 | Table HL70423",
    )

    abs_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_10",
            "caesarian_section_indicator",
            "ABS.10",
        ),
        serialization_alias="ABS.10",
        title="Caesarian Section Indicator",
        description="Item #1523 | Table HL70136",
    )

    abs_11: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_11",
            "gestation_category_code",
            "ABS.11",
        ),
        serialization_alias="ABS.11",
        title="Gestation Category Code",
        description="Item #1524 | Table HL70424",
    )

    abs_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_12",
            "gestation_period_weeks",
            "ABS.12",
        ),
        serialization_alias="ABS.12",
        title="Gestation Period - Weeks",
        description="Item #1525",
    )

    abs_13: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_13",
            "newborn_code",
            "ABS.13",
        ),
        serialization_alias="ABS.13",
        title="Newborn Code",
        description="Item #1526 | Table HL70425",
    )

    abs_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_14",
            "stillborn_indicator",
            "ABS.14",
        ),
        serialization_alias="ABS.14",
        title="Stillborn Indicator",
        description="Item #1527 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
