"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DG1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class DG1(HL7Model):
    """Diagnosis (S6.5.2).

    Attributes
    ----------
    dg1_1 : str
        DG1.1 - Set ID - DG1 (SI) R S6.5.2.1

    dg1_3 : CWE
        DG1.3 - Diagnosis Code - DG1 (CWE) R S6.5.2.3 | 0051 - Diagnosis Code

    dg1_5 : str | None
        DG1.5 - Diagnosis Date/Time (DTM) O S6.5.2.5

    dg1_6 : CWE
        DG1.6 - Diagnosis Type (CWE) R S6.5.2.6 | 0052 - Diagnosis Type

    dg1_15 : str | None
        DG1.15 - Diagnosis Priority (NM) O S6.5.2.15 | 0359 - Diagnosis Priority

    dg1_16 : list[XCN] | None
        DG1.16 - Diagnosing Clinician (XCN) O rep S6.5.2.16

    dg1_17 : CWE | None
        DG1.17 - Diagnosis Classification (CWE) O S6.5.2.17 | 0228 - Diagnosis Classification

    dg1_18 : str | None
        DG1.18 - Confidential Indicator (ID) O S6.5.2.18 | 0136 - Yes/no Indicator

    dg1_19 : str | None
        DG1.19 - Attestation Date/Time (DTM) O S6.5.2.19

    dg1_20 : EI | None
        DG1.20 - Diagnosis Identifier (EI) C S6.5.2.20

    dg1_21 : str | None
        DG1.21 - Diagnosis Action Code (ID) C S6.5.2.21 | 0206 - Segment Action Code

    dg1_22 : EI | None
        DG1.22 - Parent Diagnosis (EI) C S6.5.2.22

    dg1_23 : CWE | None
        DG1.23 - DRG CCL Value Code (CWE) O S6.5.2.23 | 0728 - CCL Value

    dg1_24 : str | None
        DG1.24 - DRG Grouping Usage (ID) O S6.5.2.24 | 0136 - Yes/no Indicator

    dg1_25 : CWE | None
        DG1.25 - DRG Diagnosis Determination Status (CWE) O S6.5.2.25 | 0731 - DRG Diagnosis Determination Status

    dg1_26 : CWE | None
        DG1.26 - Present On Admission (POA) Indicator (CWE) O S6.5.2.26 | 0895 - Present On Admission (POA) Indicator
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

    dg1_3: CWE = Field(
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code_dg1",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="Diagnosis Code - DG1",
        description="R | Item #00377 | Table 0051 - Diagnosis Code",
    )

    dg1_5: Optional[str] = Field(
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

    dg1_6: CWE = Field(
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="Diagnosis Type",
        description="R | Item #00380 | Table 0052 - Diagnosis Type",
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
        description="O | Item #00389 | Table 0359 - Diagnosis Priority",
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

    dg1_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_17",
            "diagnosis_classification",
            "DG1.17",
        ),
        serialization_alias="DG1.17",
        title="Diagnosis Classification",
        description="O | Item #00766 | Table 0228 - Diagnosis Classification",
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
        description="O | Item #00767 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    dg1_19: Optional[str] = Field(
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

    dg1_20: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_20",
            "diagnosis_identifier",
            "DG1.20",
        ),
        serialization_alias="DG1.20",
        title="Diagnosis Identifier",
        description="C | Item #01850",
    )

    dg1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_21",
            "diagnosis_action_code",
            "DG1.21",
        ),
        serialization_alias="DG1.21",
        title="Diagnosis Action Code",
        description=(
            "C | Item #01894 | Table 0206 - Segment Action Code | LEN:1"
        ),
    )

    dg1_22: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_22",
            "parent_diagnosis",
            "DG1.22",
        ),
        serialization_alias="DG1.22",
        title="Parent Diagnosis",
        description="C | Item #02152",
    )

    dg1_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_23",
            "drg_ccl_value_code",
            "DG1.23",
        ),
        serialization_alias="DG1.23",
        title="DRG CCL Value Code",
        description="O | Item #02153 | Table 0728 - CCL Value",
    )

    dg1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_24",
            "drg_grouping_usage",
            "DG1.24",
        ),
        serialization_alias="DG1.24",
        title="DRG Grouping Usage",
        description="O | Item #02154 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    dg1_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_25",
            "drg_diagnosis_determination_status",
            "DG1.25",
        ),
        serialization_alias="DG1.25",
        title="DRG Diagnosis Determination Status",
        description=(
            "O | Item #02155 | Table 0731 - DRG Diagnosis Determination Status"
        ),
    )

    dg1_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_26",
            "present_on_admission_poa_indicator",
            "DG1.26",
        ),
        serialization_alias="DG1.26",
        title="Present On Admission (POA) Indicator",
        description=(
            "O | Item #02288 | Table 0895 - Present On Admission (POA) Indicator"
        ),
    )

    @field_validator("dg1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("dg1_5", "dg1_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("dg1_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
