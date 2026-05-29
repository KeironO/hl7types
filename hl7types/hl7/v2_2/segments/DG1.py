"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DG1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class DG1(BaseModel):
    """HL7 v2 DG1 segment.

    Attributes
    ----------
    dg1_1 : str
        DG1.1 (req) - Set ID - diagnosis (SI)

    dg1_2 : str
        DG1.2 (req) - Diagnosis coding method (ID)

    dg1_3 : str | None
        DG1.3 (opt) - Diagnosis code (ID)

    dg1_4 : str | None
        DG1.4 (opt) - Diagnosis description (ST)

    dg1_5 : TS | None
        DG1.5 (opt) - Diagnosis date / time (TS)

    dg1_6 : str
        DG1.6 (req) - Diagnosis / DRG type (ID)

    dg1_7 : CE | None
        DG1.7 (opt) - Major diagnostic category (CE)

    dg1_8 : str | None
        DG1.8 (opt) - Diagnostic related group (ID)

    dg1_9 : str | None
        DG1.9 (opt) - DRG approval indicator (ID)

    dg1_10 : str | None
        DG1.10 (opt) - DRG grouper review code (ID)

    dg1_11 : str | None
        DG1.11 (opt) - Outlier type (ID)

    dg1_12 : str | None
        DG1.12 (opt) - Outlier days (NM)

    dg1_13 : str | None
        DG1.13 (opt) - Outlier cost (NM)

    dg1_14 : str | None
        DG1.14 (opt) - Grouper version and type (ST)

    dg1_15 : str | None
        DG1.15 (opt) - Diagnosis / DRG priority (NM)

    dg1_16 : str | None
        DG1.16 (opt) - Diagnosing clinician (CN)
    """

    dg1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_diagnosis",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="Set ID - diagnosis",
        description="Item #375",
    )

    dg1_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_2",
            "diagnosis_coding_method",
            "DG1.2",
        ),
        serialization_alias="DG1.2",
        title="Diagnosis coding method",
        description="Item #376 | Table HL70053",
    )

    dg1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="Diagnosis code",
        description="Item #377 | Table HL70051",
    )

    dg1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_4",
            "diagnosis_description",
            "DG1.4",
        ),
        serialization_alias="DG1.4",
        title="Diagnosis description",
        description="Item #378",
    )

    dg1_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_5",
            "diagnosis_date_time",
            "DG1.5",
        ),
        serialization_alias="DG1.5",
        title="Diagnosis date / time",
        description="Item #379",
    )

    dg1_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_drg_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="Diagnosis / DRG type",
        description="Item #380 | Table HL70052",
    )

    dg1_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_7",
            "major_diagnostic_category",
            "DG1.7",
        ),
        serialization_alias="DG1.7",
        title="Major diagnostic category",
        description="Item #381 | Table HL70118",
    )

    dg1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_8",
            "diagnostic_related_group",
            "DG1.8",
        ),
        serialization_alias="DG1.8",
        title="Diagnostic related group",
        description="Item #382 | Table HL70055",
    )

    dg1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_9",
            "drg_approval_indicator",
            "DG1.9",
        ),
        serialization_alias="DG1.9",
        title="DRG approval indicator",
        description="Item #383",
    )

    dg1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_10",
            "drg_grouper_review_code",
            "DG1.10",
        ),
        serialization_alias="DG1.10",
        title="DRG grouper review code",
        description="Item #384 | Table HL70056",
    )

    dg1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_11",
            "outlier_type",
            "DG1.11",
        ),
        serialization_alias="DG1.11",
        title="Outlier type",
        description="Item #385 | Table HL70083",
    )

    dg1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_12",
            "outlier_days",
            "DG1.12",
        ),
        serialization_alias="DG1.12",
        title="Outlier days",
        description="Item #386",
    )

    dg1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_13",
            "outlier_cost",
            "DG1.13",
        ),
        serialization_alias="DG1.13",
        title="Outlier cost",
        description="Item #387",
    )

    dg1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_14",
            "grouper_version_and_type",
            "DG1.14",
        ),
        serialization_alias="DG1.14",
        title="Grouper version and type",
        description="Item #388",
    )

    dg1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_15",
            "diagnosis_drg_priority",
            "DG1.15",
        ),
        serialization_alias="DG1.15",
        title="Diagnosis / DRG priority",
        description="Item #389",
    )

    dg1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_16",
            "diagnosing_clinician",
            "DG1.16",
        ),
        serialization_alias="DG1.16",
        title="Diagnosing clinician",
        description="Item #390",
    )

    model_config = {"populate_by_name": True}
