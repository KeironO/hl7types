"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DG1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class DG1(HL7Model):
    """DIAGNOSIS (S6.3.2).

    Attributes
    ----------
    dg1_1 : str
        DG1.1 - SET ID - DIAGNOSIS (SI) R S6-3

    dg1_2 : str
        DG1.2 - DIAGNOSIS CODING METHOD (ID) R | 0053 - DIAGNOSIS CODING METHOD

    dg1_3 : str | None
        DG1.3 - DIAGNOSIS CODE (ID) O | 0051 - DIAGNOSIS CODE

    dg1_4 : str | None
        DG1.4 - DIAGNOSIS DESCRIPTION (ST) O

    dg1_5 : str | None
        DG1.5 - DIAGNOSIS DATE/TIME (TS) O

    dg1_6 : str
        DG1.6 - DIAGNOSIS/DRG TYPE (ID) R | 0052 - DIAGNOSIS TYPE

    dg1_7 : str | None
        DG1.7 - MAJOR DIAGNOSTIC CATEGORY (ST) O | 0118 - MAJOR DIAGNOSTIC CATEGORY

    dg1_8 : str | None
        DG1.8 - DIAGNOSTIC RELATED GROUP (ID) O | 0055 - DRG CODE

    dg1_9 : str | None
        DG1.9 - DRG APPROVAL INDICATOR (ID) O

    dg1_10 : str | None
        DG1.10 - DRG GROUPER REVIEW CODE (ID) O | 0056 - DRG GROUPER REVIEW CODE

    dg1_11 : str | None
        DG1.11 - OUTLIER TYPE (ID) O | 0083 - OUTLIER TYPE

    dg1_12 : str | None
        DG1.12 - OUTLIER DAYS (NM) O

    dg1_13 : str | None
        DG1.13 - OUTLIER COST (NM) O

    dg1_14 : str | None
        DG1.14 - GROUPER VERSION AND TYPE (ST) O
    """

    dg1_1: str = Field(
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_diagnosis",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="SET ID - DIAGNOSIS",
        description="R | Item #00506 | LEN:4",
    )

    dg1_2: str = Field(
        validation_alias=AliasChoices(
            "dg1_2",
            "diagnosis_coding_method",
            "DG1.2",
        ),
        serialization_alias="DG1.2",
        title="DIAGNOSIS CODING METHOD",
        description=(
            "R | Item #00394 | Table 0053 - DIAGNOSIS CODING METHOD | LEN:2"
        ),
    )

    dg1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="DIAGNOSIS CODE",
        description="O | Item #00293 | Table 0051 - DIAGNOSIS CODE | LEN:8",
    )

    dg1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_4",
            "diagnosis_description",
            "DG1.4",
        ),
        serialization_alias="DG1.4",
        title="DIAGNOSIS DESCRIPTION",
        description="O | Item #00294 | LEN:40",
    )

    dg1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_5",
            "diagnosis_date_time",
            "DG1.5",
        ),
        serialization_alias="DG1.5",
        title="DIAGNOSIS DATE/TIME",
        description="O | Item #00295 | LEN:19",
    )

    dg1_6: str = Field(
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_drg_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="DIAGNOSIS/DRG TYPE",
        description="R | Item #00297 | Table 0052 - DIAGNOSIS TYPE | LEN:2",
    )

    dg1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_7",
            "major_diagnostic_category",
            "DG1.7",
        ),
        serialization_alias="DG1.7",
        title="MAJOR DIAGNOSTIC CATEGORY",
        description=(
            "O | Item #00298 | Table 0118 - MAJOR DIAGNOSTIC CATEGORY | LEN:4"
        ),
    )

    dg1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_8",
            "diagnostic_related_group",
            "DG1.8",
        ),
        serialization_alias="DG1.8",
        title="DIAGNOSTIC RELATED GROUP",
        description="O | Item #00299 | Table 0055 - DRG CODE | LEN:4",
    )

    dg1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_9",
            "drg_approval_indicator",
            "DG1.9",
        ),
        serialization_alias="DG1.9",
        title="DRG APPROVAL INDICATOR",
        description="O | Item #00373 | LEN:2",
    )

    dg1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_10",
            "drg_grouper_review_code",
            "DG1.10",
        ),
        serialization_alias="DG1.10",
        title="DRG GROUPER REVIEW CODE",
        description=(
            "O | Item #00374 | Table 0056 - DRG GROUPER REVIEW CODE | LEN:2"
        ),
    )

    dg1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_11",
            "outlier_type",
            "DG1.11",
        ),
        serialization_alias="DG1.11",
        title="OUTLIER TYPE",
        description="O | Item #00375 | Table 0083 - OUTLIER TYPE | LEN:2",
    )

    dg1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_12",
            "outlier_days",
            "DG1.12",
        ),
        serialization_alias="DG1.12",
        title="OUTLIER DAYS",
        description="O | Item #00300 | LEN:3",
    )

    dg1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_13",
            "outlier_cost",
            "DG1.13",
        ),
        serialization_alias="DG1.13",
        title="OUTLIER COST",
        description="O | Item #00376 | LEN:12",
    )

    dg1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_14",
            "grouper_version_and_type",
            "DG1.14",
        ),
        serialization_alias="DG1.14",
        title="GROUPER VERSION AND TYPE",
        description="O | Item #00781 | LEN:4",
    )

    @field_validator("dg1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("dg1_12", "dg1_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
