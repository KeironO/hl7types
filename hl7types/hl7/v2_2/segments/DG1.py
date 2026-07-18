"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DG1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class DG1(HL7Model):
    """DIAGNOSIS (S6.4.2).

    Attributes
    ----------
    dg1_1 : str
        DG1.1 - Set ID - diagnosis (SI) R S6.4.2.1

    dg1_2 : str
        DG1.2 - Diagnosis coding method (ID) R S6.4.2.2 | 0053 - DIAGNOSIS CODING METHOD

    dg1_3 : str | None
        DG1.3 - Diagnosis code (ID) NA S6.4.2.3 | 0051 - DIAGNOSIS CODE

    dg1_4 : str | None
        DG1.4 - Diagnosis description (ST) NA S6.4.2.4

    dg1_5 : TS | None
        DG1.5 - Diagnosis date / time (TS) NA S6.4.2.5

    dg1_6 : str
        DG1.6 - Diagnosis / DRG type (ID) R S6.4.2.6 | 0052 - DIAGNOSIS TYPE

    dg1_7 : CE | None
        DG1.7 - Major diagnostic category (CE) NA S6.4.2.7 | 0118 - MAJOR DIAGNOSTIC CATEGORY

    dg1_8 : str | None
        DG1.8 - Diagnostic related group (ID) NA S6.4.2.8 | 0055 - DRG CODE

    dg1_9 : str | None
        DG1.9 - DRG approval indicator (ID) NA S6.4.2.9

    dg1_10 : str | None
        DG1.10 - DRG grouper review code (ID) NA S6.4.2.10 | 0056 - DRG GROUPER REVIEW CODE

    dg1_11 : str | None
        DG1.11 - Outlier type (ID) NA S6.4.2.11 | 0083 - OUTLIER TYPE

    dg1_12 : str | None
        DG1.12 - Outlier days (NM) NA S6.4.2.12

    dg1_13 : str | None
        DG1.13 - Outlier cost (NM) NA S6.4.2.13

    dg1_14 : str | None
        DG1.14 - Grouper version and type (ST) NA S6.4.2.14

    dg1_15 : str | None
        DG1.15 - Diagnosis / DRG priority (NM) NA S6.4.2.15

    dg1_16 : str | None
        DG1.16 - Diagnosing clinician (CN) NA S6.4.2.16
    """

    dg1_1: str = Field(
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_diagnosis",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="Set ID - diagnosis",
        description="R | Item #00375 | LEN:4",
    )

    dg1_2: str = Field(
        validation_alias=AliasChoices(
            "dg1_2",
            "diagnosis_coding_method",
            "DG1.2",
        ),
        serialization_alias="DG1.2",
        title="Diagnosis coding method",
        description=(
            "R | Item #00376 | Table 0053 - DIAGNOSIS CODING METHOD | LEN:2"
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
        title="Diagnosis code",
        description="NA | Item #00377 | Table 0051 - DIAGNOSIS CODE | LEN:8",
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
        description="NA | Item #00378 | LEN:40",
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
        description="NA | Item #00379",
    )

    dg1_6: str = Field(
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_drg_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="Diagnosis / DRG type",
        description="R | Item #00380 | Table 0052 - DIAGNOSIS TYPE | LEN:2",
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
        description="NA | Item #00381 | Table 0118 - MAJOR DIAGNOSTIC CATEGORY",
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
        description="NA | Item #00382 | Table 0055 - DRG CODE | LEN:4",
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
        description="NA | Item #00383 | LEN:2",
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
        description=(
            "NA | Item #00384 | Table 0056 - DRG GROUPER REVIEW CODE | LEN:2"
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
        title="Outlier type",
        description="NA | Item #00385 | Table 0083 - OUTLIER TYPE | LEN:60",
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
        description="NA | Item #00386 | LEN:3",
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
        description="NA | Item #00387 | LEN:12",
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
        description="NA | Item #00388 | LEN:4",
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
        description="NA | Item #00389 | LEN:2",
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
        description="NA | Item #00390",
    )

    @field_validator("dg1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("dg1_12", "dg1_13", "dg1_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
