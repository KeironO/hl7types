"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DG1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class DG1(HL7Model):
    """Diagnosis (S6.5.2).

    Attributes
    ----------
    dg1_1 : str
        DG1.1 (req) - Set ID - DG1 (SI) S6.5.2.1

    dg1_3 : CWE
        DG1.3 (req) - Diagnosis Code - DG1 (CWE) S6.5.2.3 | 0051 - Diagnosis Code

    dg1_5 : str | None
        DG1.5 (opt) - Diagnosis Date/Time (DTM) S6.5.2.5

    dg1_6 : CWE
        DG1.6 (req) - Diagnosis Type (CWE) S6.5.2.6 | 0052 - Diagnosis Type

    dg1_15 : str | None
        DG1.15 (opt) - Diagnosis Priority (NM) S6.5.2.15 | 0359 - Diagnosis Priority

    dg1_16 : list[XCN] | None
        DG1.16 (opt, rep) - Diagnosing Clinician (XCN) S6.5.2.16

    dg1_17 : CWE | None
        DG1.17 (opt) - Diagnosis Classification (CWE) S6.5.2.17 | 0228 - Diagnosis Classification

    dg1_18 : str | None
        DG1.18 (opt) - Confidential Indicator (ID) S6.5.2.18 | 0136 - Yes/no Indicator

    dg1_19 : str | None
        DG1.19 (opt) - Attestation Date/Time (DTM) S6.5.2.19

    dg1_20 : EI | None
        DG1.20 (opt) - Diagnosis Identifier (EI) S6.5.2.20

    dg1_21 : str | None
        DG1.21 (opt) - Diagnosis Action Code (ID) S6.5.2.21 | 0206 - Segment Action Code

    dg1_22 : EI | None
        DG1.22 (opt) - Parent Diagnosis (EI) S6.5.2.22

    dg1_23 : CWE | None
        DG1.23 (opt) - DRG CCL Value Code (CWE) S6.5.2.23 | 0728 - CCL Value

    dg1_24 : str | None
        DG1.24 (opt) - DRG Grouping Usage (ID) S6.5.2.24 | 0136 - Yes/no Indicator

    dg1_25 : CWE | None
        DG1.25 (opt) - DRG Diagnosis Determination Status (CWE) S6.5.2.25 | 0731 - DRG Diagnosis Determination Status

    dg1_26 : CWE | None
        DG1.26 (opt) - Present On Admission (POA) Indicator (CWE) S6.5.2.26 | 0895 - Present On Admission (POA) Indicator
    """

    dg1_1: str = Field(
        validation_alias=AliasChoices(
            "dg1_1",
            "set_id_dg1",
            "DG1.1",
        ),
        serialization_alias="DG1.1",
        title="Set ID - DG1",
        description="Item #375",
    )

    dg1_3: CWE = Field(
        validation_alias=AliasChoices(
            "dg1_3",
            "diagnosis_code_dg1",
            "DG1.3",
        ),
        serialization_alias="DG1.3",
        title="Diagnosis Code - DG1",
        description="Item #377 | Table HL70051",
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
        description="Item #379",
    )

    dg1_6: CWE = Field(
        validation_alias=AliasChoices(
            "dg1_6",
            "diagnosis_type",
            "DG1.6",
        ),
        serialization_alias="DG1.6",
        title="Diagnosis Type",
        description="Item #380 | Table HL70052",
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
        description="Item #389 | Table HL70359",
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

    dg1_17: Optional[CWE] = Field(
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

    dg1_19: Optional[str] = Field(
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

    dg1_20: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dg1_20",
            "diagnosis_identifier",
            "DG1.20",
        ),
        serialization_alias="DG1.20",
        title="Diagnosis Identifier",
        description="Item #1850",
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
        description="Item #1894 | Table HL70206",
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
        description="Item #2152",
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
        description="Item #2153 | Table HL70728",
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
        description="Item #2154 | Table HL70136",
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
        description="Item #2155 | Table HL70731",
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
        description="Item #2288 | Table HL70895",
    )

    @field_validator("dg1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("dg1_5", "dg1_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("dg1_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
