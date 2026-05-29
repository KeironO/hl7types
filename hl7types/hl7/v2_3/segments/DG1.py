"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: DG1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class DG1(BaseModel):
    """HL7 v2 DG1 segment.

    Attributes
    ----------
    dg1_1 : str
        DG1.1 (req) - Set ID - Diagnosis (SI)

    dg1_2 : str | None
        DG1.2 (opt) - Diagnosis Coding Method (ID)

    dg1_3 : CE | None
        DG1.3 (opt) - Diagnosis Code (CE)

    dg1_4 : str | None
        DG1.4 (opt) - Diagnosis Description (ST)

    dg1_5 : TS | None
        DG1.5 (opt) - Diagnosis Date/Time (TS)

    dg1_6 : str
        DG1.6 (req) - Diagnosis Type (IS)

    dg1_7 : CE | None
        DG1.7 (opt) - Major Diagnostic Category (CE)

    dg1_8 : CE | None
        DG1.8 (opt) - Diagnostic Related Group (CE)

    dg1_9 : str | None
        DG1.9 (opt) - DRG Approval Indicator (ID)

    dg1_10 : str | None
        DG1.10 (opt) - DRG Grouper Review Code (IS)

    dg1_11 : CE | None
        DG1.11 (opt) - Outlier Type (CE)

    dg1_12 : str | None
        DG1.12 (opt) - Outlier Days (NM)

    dg1_13 : CP | None
        DG1.13 (opt) - Outlier Cost (CP)

    dg1_14 : str | None
        DG1.14 (opt) - Grouper Version and Type (ST)

    dg1_15 : str | None
        DG1.15 (opt) - Diagnosis Priority (NM)

    dg1_16 : list[XCN] | None
        DG1.16 (opt, rep) - Diagnosing Clinician (XCN)

    dg1_17 : str | None
        DG1.17 (opt) - Diagnosis Classification (IS)

    dg1_18 : str | None
        DG1.18 (opt) - Confidential Indicator (ID)

    dg1_19 : TS | None
        DG1.19 (opt) - Attestation Date/Time (TS)
    """

    dg1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_diagnosis",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="Set ID - Diagnosis",
        description="Item #375",
    )

    dg1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_2",
            "diagnosis_coding_method",
            "DG1.2",
        ),
        serialization_alias="DG1.2",
        title="Diagnosis Coding Method",
        description="Item #376 | Table HL70053",
    )

    dg1_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="Diagnosis Code",
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
        title="Diagnosis Description",
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
        title="Diagnosis Date/Time",
        description="Item #379",
    )

    dg1_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="Diagnosis Type",
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
        title="Major Diagnostic Category",
        description="Item #381 | Table HL70118",
    )

    dg1_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_8",
            "diagnostic_related_group",
            "DG1.8",
        ),
        serialization_alias="DG1.8",
        title="Diagnostic Related Group",
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
        title="DRG Approval Indicator",
        description="Item #383 | Table HL70136",
    )

    dg1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_10",
            "drg_grouper_review_code",
            "DG1.10",
        ),
        serialization_alias="DG1.10",
        title="DRG Grouper Review Code",
        description="Item #384 | Table HL70056",
    )

    dg1_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_11",
            "outlier_type",
            "DG1.11",
        ),
        serialization_alias="DG1.11",
        title="Outlier Type",
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
        title="Outlier Days",
        description="Item #386",
    )

    dg1_13: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_13",
            "outlier_cost",
            "DG1.13",
        ),
        serialization_alias="DG1.13",
        title="Outlier Cost",
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
        title="Grouper Version and Type",
        description="Item #388",
    )

    dg1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_15",
            "diagnosis_priority",
            "DG1.15",
        ),
        serialization_alias="DG1.15",
        title="Diagnosis Priority",
        description="Item #389",
    )

    dg1_16: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_16",
            "diagnosing_clinician",
            "DG1.16",
        ),
        serialization_alias="DG1.16",
        title="Diagnosing Clinician",
        description="Item #390",
    )

    dg1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_17",
            "diagnosis_classification",
            "DG1.17",
        ),
        serialization_alias="DG1.17",
        title="Diagnosis Classification",
        description="Item #766 | Table HL70228",
    )

    dg1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_18",
            "confidential_indicator",
            "DG1.18",
        ),
        serialization_alias="DG1.18",
        title="Confidential Indicator",
        description="Item #767 | Table HL70136",
    )

    dg1_19: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_19",
            "attestation_date_time",
            "DG1.19",
        ),
        serialization_alias="DG1.19",
        title="Attestation Date/Time",
        description="Item #768",
    )

    model_config = {"populate_by_name": True}
