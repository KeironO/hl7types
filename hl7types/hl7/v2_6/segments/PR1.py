"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PR1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class PR1(HL7Model):
    """Procedures (S6.5.4).

    Attributes
    ----------
    pr1_1 : str
        PR1.1 - Set ID - PR1 (SI) R S6.5.4.1

    pr1_3 : CNE
        PR1.3 - Procedure Code (CNE) R S17.4.1.14 | 0088 - Procedure Code

    pr1_5 : str
        PR1.5 - Procedure Date/Time (DTM) R S6.5.4.5

    pr1_6 : str | None
        PR1.6 - Procedure Functional Type (IS) O S6.5.4.6 | 0230 - Procedure Functional Type

    pr1_7 : str | None
        PR1.7 - Procedure Minutes (NM) O S6.5.4.7

    pr1_9 : str | None
        PR1.9 - Anesthesia Code (IS) O S6.5.4.9 | 0019 - Anesthesia Code

    pr1_10 : str | None
        PR1.10 - Anesthesia Minutes (NM) O S6.5.4.10

    pr1_13 : CWE | None
        PR1.13 - Consent Code (CWE) O S6.5.4.13 | 0059 - Consent Code

    pr1_14 : str | None
        PR1.14 - Procedure Priority (ID) O S6.5.4.14 | 0418 - Procedure Priority

    pr1_15 : CWE | None
        PR1.15 - Associated Diagnosis Code (CWE) O S6.5.4.15 | 0051 - Diagnosis Code

    pr1_16 : list[CNE] | None
        PR1.16 - Procedure Code Modifier (CNE) O rep S17.4.1.15 | 0340 - Procedure Code Modifier

    pr1_17 : str | None
        PR1.17 - Procedure DRG Type (IS) O S6.5.4.17 | 0416 - Procedure DRG Type

    pr1_18 : list[CWE] | None
        PR1.18 - Tissue Type Code (CWE) O rep S6.5.4.18 | 0417 - Tissue Type Code

    pr1_19 : EI | None
        PR1.19 - Procedure Identifier (EI) C S6.5.4.19

    pr1_20 : str | None
        PR1.20 - Procedure Action Code (ID) C S6.5.4.20 | 0206 - Segment action code

    pr1_21 : str | None
        PR1.21 - DRG Procedure Determination Status (IS) O S6.5.4.21 | 0761 - DRG Procedure Determination Status

    pr1_22 : str | None
        PR1.22 - DRG Procedure Relevance (IS) O S6.5.4.22 | 0763 - DRG Procedure Relevance
    """

    pr1_1: str = Field(
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_pr1",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="Set ID - PR1",
        description="R | Item #00391 | LEN:4",
    )

    pr1_3: CNE = Field(
        validation_alias=AliasChoices(
            "pr1_3",
            "procedure_code",
            "PR1.3",
        ),
        serialization_alias="PR1.3",
        title="Procedure Code",
        description="R | Item #00393 | Table 0088 - Procedure Code",
    )

    pr1_5: str = Field(
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="Procedure Date/Time",
        description="R | Item #00395 | LEN:24",
    )

    pr1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_functional_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="Procedure Functional Type",
        description=(
            "O | Item #00396 | Table 0230 - Procedure Functional Type | LEN:2"
        ),
    )

    pr1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_7",
            "procedure_minutes",
            "PR1.7",
        ),
        serialization_alias="PR1.7",
        title="Procedure Minutes",
        description="O | Item #00397 | LEN:4",
    )

    pr1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_9",
            "anesthesia_code",
            "PR1.9",
        ),
        serialization_alias="PR1.9",
        title="Anesthesia Code",
        description="O | Item #00399 | Table 0019 - Anesthesia Code | LEN:2",
    )

    pr1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_10",
            "anesthesia_minutes",
            "PR1.10",
        ),
        serialization_alias="PR1.10",
        title="Anesthesia Minutes",
        description="O | Item #00400 | LEN:4",
    )

    pr1_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_13",
            "consent_code",
            "PR1.13",
        ),
        serialization_alias="PR1.13",
        title="Consent Code",
        description="O | Item #00403 | Table 0059 - Consent Code",
    )

    pr1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_14",
            "procedure_priority",
            "PR1.14",
        ),
        serialization_alias="PR1.14",
        title="Procedure Priority",
        description="O | Item #00404 | Table 0418 - Procedure Priority | LEN:2",
    )

    pr1_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_15",
            "associated_diagnosis_code",
            "PR1.15",
        ),
        serialization_alias="PR1.15",
        title="Associated Diagnosis Code",
        description="O | Item #00772 | Table 0051 - Diagnosis Code",
    )

    pr1_16: Optional[List[CNE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_16",
            "procedure_code_modifier",
            "PR1.16",
        ),
        serialization_alias="PR1.16",
        title="Procedure Code Modifier",
        description="O | Item #01316 | Table 0340 - Procedure Code Modifier",
    )

    pr1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_17",
            "procedure_drg_type",
            "PR1.17",
        ),
        serialization_alias="PR1.17",
        title="Procedure DRG Type",
        description=(
            "O | Item #01501 | Table 0416 - Procedure DRG Type | LEN:20"
        ),
    )

    pr1_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_18",
            "tissue_type_code",
            "PR1.18",
        ),
        serialization_alias="PR1.18",
        title="Tissue Type Code",
        description="O | Item #01502 | Table 0417 - Tissue Type Code",
    )

    pr1_19: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_19",
            "procedure_identifier",
            "PR1.19",
        ),
        serialization_alias="PR1.19",
        title="Procedure Identifier",
        description="C | Item #01848",
    )

    pr1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_20",
            "procedure_action_code",
            "PR1.20",
        ),
        serialization_alias="PR1.20",
        title="Procedure Action Code",
        description=(
            "C | Item #01849 | Table 0206 - Segment action code | LEN:1"
        ),
    )

    pr1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_21",
            "drg_procedure_determination_status",
            "PR1.21",
        ),
        serialization_alias="PR1.21",
        title="DRG Procedure Determination Status",
        description=(
            "O | Item #02177 | Table 0761 - DRG Procedure Determination Status | "
            "LEN:20"
        ),
    )

    pr1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_22",
            "drg_procedure_relevance",
            "PR1.22",
        ),
        serialization_alias="PR1.22",
        title="DRG Procedure Relevance",
        description=(
            "O | Item #02178 | Table 0763 - DRG Procedure Relevance | LEN:20"
        ),
    )

    @field_validator("pr1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pr1_5", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("pr1_7", "pr1_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
