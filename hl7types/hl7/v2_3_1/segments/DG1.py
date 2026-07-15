"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DG1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class DG1(HL7Model):
    """DG1 - diagnosis segment (S6.4.2).

    Attributes
    ----------
    dg1_1 : str
        DG1.1 - Set ID - DG1 (SI) R S6.4.2.1

    dg1_2 : str | None
        DG1.2 - Diagnosis Coding Method (ID) R S6.4.2.2 | 0053 - Diagnosis Coding Methed

    dg1_3 : CE | None
        DG1.3 - Diagnosis Code - DG1 (CE) O S6.4.2.3 | 0051 - Diagnosis Code

    dg1_4 : str | None
        DG1.4 - Diagnosis Description (ST) O S6.4.2.4

    dg1_5 : TS | None
        DG1.5 - Diagnosis Date/Time (TS) O S6.4.2.5

    dg1_6 : str
        DG1.6 - Diagnosis Type (IS) R S6.4.2.6 | 0052 - Diagnosis Type

    dg1_7 : CE | None
        DG1.7 - Major Diagnostic Category (CE) O S6.4.2.7 | 0118 - Major Diagnostic Category

    dg1_8 : CE | None
        DG1.8 - Diagnostic Related Group (CE) O S6.4.3.1 | 0055 - Diagnostic Related Group

    dg1_9 : str | None
        DG1.9 - DRG Approval Indicator (ID) O S6.4.3.3 | 0136 - Yes/no indicator

    dg1_10 : str | None
        DG1.10 - DRG Grouper Review Code (IS) O S6.4.3.4 | 0056 - DRG Grouper Review Code

    dg1_11 : CE | None
        DG1.11 - Outlier Type (CE) O S6.4.3.5 | 0083 - Outlier Type

    dg1_12 : str | None
        DG1.12 - Outlier Days (NM) O S6.4.3.6

    dg1_13 : CP | None
        DG1.13 - Outlier Cost (CP) O S6.4.3.7

    dg1_14 : str | None
        DG1.14 - Grouper Version And Type (ST) O S6.4.2.14

    dg1_15 : str | None
        DG1.15 - Diagnosis Priority (ID) O S6.4.2.15 | 0359 - Diagnosis priority

    dg1_16 : list[XCN] | None
        DG1.16 - Diagnosing Clinician (XCN) O rep S6.4.2.16

    dg1_17 : str | None
        DG1.17 - Diagnosis Classification (IS) O S6.4.2.17 | 0228 - Diagnosis classification

    dg1_18 : str | None
        DG1.18 - Confidential Indicator (ID) O S6.4.3.10 | 0136 - Yes/no indicator

    dg1_19 : TS | None
        DG1.19 - Attestation Date/Time (TS) O S6.4.2.19
    """

    dg1_1: str = Field(
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_dg1",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="Set ID - DG1",
        description="R | Item #00375 | LEN:4",
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
        description=(
            "R | Item #00376 | Table 0053 - Diagnosis Coding Methed | LEN:2"
        ),
    )

    dg1_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code_dg1",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="Diagnosis Code - DG1",
        description="O | Item #00377 | Table 0051 - Diagnosis Code",
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
        description="O | Item #00378 | LEN:40",
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
        description="O | Item #00379",
    )

    dg1_6: str = Field(
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="Diagnosis Type",
        description="R | Item #00380 | Table 0052 - Diagnosis Type | LEN:2",
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
        description="O | Item #00381 | Table 0118 - Major Diagnostic Category",
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
        description="O | Item #00382 | Table 0055 - Diagnostic Related Group",
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
        description="O | Item #00383 | Table 0136 - Yes/no indicator | LEN:1",
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
        description=(
            "O | Item #00384 | Table 0056 - DRG Grouper Review Code | LEN:2"
        ),
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
        description="O | Item #00385 | Table 0083 - Outlier Type",
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
        description="O | Item #00386 | LEN:3",
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
        description="O | Item #00387",
    )

    dg1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_14",
            "grouper_version_and_type",
            "DG1.14",
        ),
        serialization_alias="DG1.14",
        title="Grouper Version And Type",
        description="O | Item #00388 | LEN:4",
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
        description="O | Item #00389 | Table 0359 - Diagnosis priority | LEN:2",
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
        description="O | Item #00390",
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
        description=(
            "O | Item #00766 | Table 0228 - Diagnosis classification | LEN:3"
        ),
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
        description="O | Item #00767 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #00768",
    )

    @field_validator("dg1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("dg1_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
