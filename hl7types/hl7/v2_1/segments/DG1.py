"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DG1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class DG1(BaseModel):
    """HL7 v2 DG1 segment."""

    dg1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_diagnosis",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="SET ID - DIAGNOSIS",
        description="Item #506",
    )

    dg1_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_2",
            "diagnosis_coding_method",
            "DG1.2",
        ),
        serialization_alias="DG1.2",
        title="DIAGNOSIS CODING METHOD",
        description="Item #394 | Table HL70053",
    )

    dg1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="DIAGNOSIS CODE",
        description="Item #293 | Table HL70051",
    )

    dg1_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_4",
            "diagnosis_description",
            "DG1.4",
        ),
        serialization_alias="DG1.4",
        title="DIAGNOSIS DESCRIPTION",
        description="Item #294",
    )

    dg1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_5",
            "diagnosis_date_time",
            "DG1.5",
        ),
        serialization_alias="DG1.5",
        title="DIAGNOSIS DATE/TIME",
        description="Item #295",
    )

    dg1_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_drg_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="DIAGNOSIS/DRG TYPE",
        description="Item #297 | Table HL70052",
    )

    dg1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_7",
            "major_diagnostic_category",
            "DG1.7",
        ),
        serialization_alias="DG1.7",
        title="MAJOR DIAGNOSTIC CATEGORY",
        description="Item #298 | Table HL70118",
    )

    dg1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_8",
            "diagnostic_related_group",
            "DG1.8",
        ),
        serialization_alias="DG1.8",
        title="DIAGNOSTIC RELATED GROUP",
        description="Item #299 | Table HL70055",
    )

    dg1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_9",
            "drg_approval_indicator",
            "DG1.9",
        ),
        serialization_alias="DG1.9",
        title="DRG APPROVAL INDICATOR",
        description="Item #373",
    )

    dg1_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_10",
            "drg_grouper_review_code",
            "DG1.10",
        ),
        serialization_alias="DG1.10",
        title="DRG GROUPER REVIEW CODE",
        description="Item #374 | Table HL70056",
    )

    dg1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_11",
            "outlier_type",
            "DG1.11",
        ),
        serialization_alias="DG1.11",
        title="OUTLIER TYPE",
        description="Item #375 | Table HL70083",
    )

    dg1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_12",
            "outlier_days",
            "DG1.12",
        ),
        serialization_alias="DG1.12",
        title="OUTLIER DAYS",
        description="Item #300",
    )

    dg1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_13",
            "outlier_cost",
            "DG1.13",
        ),
        serialization_alias="DG1.13",
        title="OUTLIER COST",
        description="Item #376",
    )

    dg1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_14",
            "grouper_version_and_type",
            "DG1.14",
        ),
        serialization_alias="DG1.14",
        title="GROUPER VERSION AND TYPE",
        description="Item #781",
    )

    model_config = {"populate_by_name": True}
