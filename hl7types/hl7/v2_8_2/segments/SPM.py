"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SPM
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class SPM(HL7Model):
    """Specimen (S7.4.3).

    Attributes
    ----------
    spm_1 : str | None
        SPM.1 - Set ID - SPM (SI) O S7.4.3.1

    spm_2 : EIP | None
        SPM.2 - Specimen ID (EIP) O S7.4.3.2

    spm_3 : list[EIP] | None
        SPM.3 - Specimen Parent IDs (EIP) O rep S7.4.3.3

    spm_4 : CWE
        SPM.4 - Specimen Type (CWE) R S7.4.3.4 | 0487 - Specimen Type

    spm_5 : list[CWE] | None
        SPM.5 - Specimen Type Modifier (CWE) O rep S7.4.3.5 | 0541 - Specimen Type Modifier

    spm_6 : list[CWE] | None
        SPM.6 - Specimen Additives (CWE) O rep S7.4.3.6 | 0371 - Additive/Preservative

    spm_7 : CWE | None
        SPM.7 - Specimen Collection Method (CWE) O S7.4.3.7 | 0488 - Specimen Collection Method

    spm_8 : CWE | None
        SPM.8 - Specimen Source Site (CWE) O S7.4.3.8 | 9999 - no table for CE

    spm_9 : list[CWE] | None
        SPM.9 - Specimen Source Site Modifier (CWE) O rep S7.4.3.9 | 0542 - Specimen Source Type Modifier

    spm_10 : CWE | None
        SPM.10 - Specimen Collection Site (CWE) O S7.4.3.10 | 0543 - Specimen Collection Site

    spm_11 : list[CWE] | None
        SPM.11 - Specimen Role (CWE) O rep S7.4.3.11 | 0369 - Specimen Role

    spm_12 : CQ | None
        SPM.12 - Specimen Collection Amount (CQ) O S7.4.3.12

    spm_13 : str | None
        SPM.13 - Grouped Specimen Count (NM) C S7.4.3.13

    spm_14 : list[str] | None
        SPM.14 - Specimen Description (ST) O rep S7.4.3.14

    spm_15 : list[CWE] | None
        SPM.15 - Specimen Handling Code (CWE) O rep S7.4.3.15 | 0376 - Special Handling Code

    spm_16 : list[CWE] | None
        SPM.16 - Specimen Risk Code (CWE) O rep S7.4.3.16 | 0489 - Risk Codes

    spm_17 : DR | None
        SPM.17 - Specimen Collection Date/Time (DR) O S7.4.3.17

    spm_18 : str | None
        SPM.18 - Specimen Received Date/Time * (DTM) O S7.4.3.18

    spm_19 : str | None
        SPM.19 - Specimen Expiration Date/Time (DTM) O S7.4.3.19

    spm_20 : str | None
        SPM.20 - Specimen Availability (ID) O S7.4.3.20 | 0136 - Yes/no Indicator

    spm_21 : list[CWE] | None
        SPM.21 - Specimen Reject Reason (CWE) O rep S7.4.3.21 | 0490 - Specimen Reject Reason

    spm_22 : CWE | None
        SPM.22 - Specimen Quality (CWE) O S7.4.3.22 | 0491 - Specimen Quality

    spm_23 : CWE | None
        SPM.23 - Specimen Appropriateness (CWE) O S7.4.3.23 | 0492 - Specimen Appropriateness

    spm_24 : list[CWE] | None
        SPM.24 - Specimen Condition (CWE) O rep S7.4.3.24 | 0493 - Specimen Condition

    spm_25 : CQ | None
        SPM.25 - Specimen Current Quantity (CQ) O S7.4.3.25

    spm_26 : str | None
        SPM.26 - Number of Specimen Containers (NM) O S7.4.3.26

    spm_27 : CWE | None
        SPM.27 - Container Type (CWE) O S7.4.3.27 | 9999 - no table for CE

    spm_28 : CWE | None
        SPM.28 - Container Condition (CWE) O S7.4.3.28 | 0544 - Container Condition

    spm_29 : CWE | None
        SPM.29 - Specimen Child Role (CWE) O S7.4.3.29 | 0494 - Specimen Child Role

    spm_30 : list[CX] | None
        SPM.30 - Accession ID (CX) O rep S7.4.3.30

    spm_31 : list[CX] | None
        SPM.31 - Other Specimen ID (CX) O rep S7.4.3.31

    spm_32 : EI | None
        SPM.32 - Shipment ID (EI) O S7.4.3.32
    """

    spm_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_1",
            "set_id_spm",
            "SPM.1",
        ),
        serialization_alias="SPM.1",
        title="Set ID - SPM",
        description="O | Item #01754 | LEN:4",
    )

    spm_2: Optional[EIP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_2",
            "specimen_id",
            "SPM.2",
        ),
        serialization_alias="SPM.2",
        title="Specimen ID",
        description="O | Item #01755",
    )

    spm_3: Optional[List[EIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_3",
            "specimen_parent_ids",
            "SPM.3",
        ),
        serialization_alias="SPM.3",
        title="Specimen Parent IDs",
        description="O | Item #01756",
    )

    spm_4: CWE = Field(
        validation_alias=AliasChoices(
            "spm_4",
            "specimen_type",
            "SPM.4",
        ),
        serialization_alias="SPM.4",
        title="Specimen Type",
        description="R | Item #01900 | Table 0487 - Specimen Type",
    )

    spm_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_5",
            "specimen_type_modifier",
            "SPM.5",
        ),
        serialization_alias="SPM.5",
        title="Specimen Type Modifier",
        description="O | Item #01757 | Table 0541 - Specimen Type Modifier",
    )

    spm_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_6",
            "specimen_additives",
            "SPM.6",
        ),
        serialization_alias="SPM.6",
        title="Specimen Additives",
        description="O | Item #01758 | Table 0371 - Additive/Preservative",
    )

    spm_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_7",
            "specimen_collection_method",
            "SPM.7",
        ),
        serialization_alias="SPM.7",
        title="Specimen Collection Method",
        description="O | Item #01759 | Table 0488 - Specimen Collection Method",
    )

    spm_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_8",
            "specimen_source_site",
            "SPM.8",
        ),
        serialization_alias="SPM.8",
        title="Specimen Source Site",
        description="O | Item #01901 | Table 9999 - no table for CE",
    )

    spm_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_9",
            "specimen_source_site_modifier",
            "SPM.9",
        ),
        serialization_alias="SPM.9",
        title="Specimen Source Site Modifier",
        description=(
            "O | Item #01760 | Table 0542 - Specimen Source Type Modifier"
        ),
    )

    spm_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_10",
            "specimen_collection_site",
            "SPM.10",
        ),
        serialization_alias="SPM.10",
        title="Specimen Collection Site",
        description="O | Item #01761 | Table 0543 - Specimen Collection Site",
    )

    spm_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_11",
            "specimen_role",
            "SPM.11",
        ),
        serialization_alias="SPM.11",
        title="Specimen Role",
        description="O | Item #01762 | Table 0369 - Specimen Role",
    )

    spm_12: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_12",
            "specimen_collection_amount",
            "SPM.12",
        ),
        serialization_alias="SPM.12",
        title="Specimen Collection Amount",
        description="O | Item #01902",
    )

    spm_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_13",
            "grouped_specimen_count",
            "SPM.13",
        ),
        serialization_alias="SPM.13",
        title="Grouped Specimen Count",
        description="C | Item #01763",
    )

    spm_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_14",
            "specimen_description",
            "SPM.14",
        ),
        serialization_alias="SPM.14",
        title="Specimen Description",
        description="O | Item #01764",
    )

    spm_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_15",
            "specimen_handling_code",
            "SPM.15",
        ),
        serialization_alias="SPM.15",
        title="Specimen Handling Code",
        description="O | Item #01908 | Table 0376 - Special Handling Code",
    )

    spm_16: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_16",
            "specimen_risk_code",
            "SPM.16",
        ),
        serialization_alias="SPM.16",
        title="Specimen Risk Code",
        description="O | Item #01903 | Table 0489 - Risk Codes",
    )

    spm_17: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_17",
            "specimen_collection_date_time",
            "SPM.17",
        ),
        serialization_alias="SPM.17",
        title="Specimen Collection Date/Time",
        description="O | Item #01765",
    )

    spm_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_18",
            "specimen_received_date_time",
            "SPM.18",
        ),
        serialization_alias="SPM.18",
        title="Specimen Received Date/Time *",
        description="O | Item #00248",
    )

    spm_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_19",
            "specimen_expiration_date_time",
            "SPM.19",
        ),
        serialization_alias="SPM.19",
        title="Specimen Expiration Date/Time",
        description="O | Item #01904",
    )

    spm_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_20",
            "specimen_availability",
            "SPM.20",
        ),
        serialization_alias="SPM.20",
        title="Specimen Availability",
        description="O | Item #01766 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    spm_21: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_21",
            "specimen_reject_reason",
            "SPM.21",
        ),
        serialization_alias="SPM.21",
        title="Specimen Reject Reason",
        description="O | Item #01767 | Table 0490 - Specimen Reject Reason",
    )

    spm_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_22",
            "specimen_quality",
            "SPM.22",
        ),
        serialization_alias="SPM.22",
        title="Specimen Quality",
        description="O | Item #01768 | Table 0491 - Specimen Quality",
    )

    spm_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_23",
            "specimen_appropriateness",
            "SPM.23",
        ),
        serialization_alias="SPM.23",
        title="Specimen Appropriateness",
        description="O | Item #01769 | Table 0492 - Specimen Appropriateness",
    )

    spm_24: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_24",
            "specimen_condition",
            "SPM.24",
        ),
        serialization_alias="SPM.24",
        title="Specimen Condition",
        description="O | Item #01770 | Table 0493 - Specimen Condition",
    )

    spm_25: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_25",
            "specimen_current_quantity",
            "SPM.25",
        ),
        serialization_alias="SPM.25",
        title="Specimen Current Quantity",
        description="O | Item #01771",
    )

    spm_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_26",
            "number_of_specimen_containers",
            "SPM.26",
        ),
        serialization_alias="SPM.26",
        title="Number of Specimen Containers",
        description="O | Item #01772",
    )

    spm_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_27",
            "container_type",
            "SPM.27",
        ),
        serialization_alias="SPM.27",
        title="Container Type",
        description="O | Item #01773 | Table 9999 - no table for CE",
    )

    spm_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_28",
            "container_condition",
            "SPM.28",
        ),
        serialization_alias="SPM.28",
        title="Container Condition",
        description="O | Item #01774 | Table 0544 - Container Condition",
    )

    spm_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_29",
            "specimen_child_role",
            "SPM.29",
        ),
        serialization_alias="SPM.29",
        title="Specimen Child Role",
        description="O | Item #01775 | Table 0494 - Specimen Child Role",
    )

    spm_30: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_30",
            "accession_id",
            "SPM.30",
        ),
        serialization_alias="SPM.30",
        title="Accession ID",
        description="O | Item #02314",
    )

    spm_31: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_31",
            "other_specimen_id",
            "SPM.31",
        ),
        serialization_alias="SPM.31",
        title="Other Specimen ID",
        description="O | Item #02315",
    )

    spm_32: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_32",
            "shipment_id",
            "SPM.32",
        ),
        serialization_alias="SPM.32",
        title="Shipment ID",
        description="O | Item #02316",
    )

    @field_validator("spm_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("spm_13", "spm_26", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("spm_18", "spm_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
