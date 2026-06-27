"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SPM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP


class SPM(HL7Model):
    """HL7 v2 SPM segment.

    Attributes
    ----------
    spm_1 : str | None
        SPM.1 (opt) - Set ID - SPM (SI)

    spm_2 : EIP | None
        SPM.2 (opt) - Specimen ID (EIP)

    spm_3 : list[EIP] | None
        SPM.3 (opt, rep) - Specimen Parent IDs (EIP)

    spm_4 : CWE
        SPM.4 (req) - Specimen Type (CWE)

    spm_5 : list[CWE] | None
        SPM.5 (opt, rep) - Specimen Type Modifier (CWE)

    spm_6 : list[CWE] | None
        SPM.6 (opt, rep) - Specimen Additives (CWE)

    spm_7 : CWE | None
        SPM.7 (opt) - Specimen Collection Method (CWE)

    spm_8 : CWE | None
        SPM.8 (opt) - Specimen Source Site (CWE)

    spm_9 : list[CWE] | None
        SPM.9 (opt, rep) - Specimen Source Site Modifier (CWE)

    spm_10 : CWE | None
        SPM.10 (opt) - Specimen Collection Site (CWE)

    spm_11 : list[CWE] | None
        SPM.11 (opt, rep) - Specimen Role (CWE)

    spm_12 : CQ | None
        SPM.12 (opt) - Specimen Collection Amount (CQ)

    spm_13 : str | None
        SPM.13 (opt) - Grouped Specimen Count (NM)

    spm_14 : list[str] | None
        SPM.14 (opt, rep) - Specimen Description (ST)

    spm_15 : list[CWE] | None
        SPM.15 (opt, rep) - Specimen Handling Code (CWE)

    spm_16 : list[CWE] | None
        SPM.16 (opt, rep) - Specimen Risk Code (CWE)

    spm_17 : DR | None
        SPM.17 (opt) - Specimen Collection Date/Time (DR)

    spm_18 : str | None
        SPM.18 (opt) - Specimen Received Date/Time (DTM)

    spm_19 : str | None
        SPM.19 (opt) - Specimen Expiration Date/Time (DTM)

    spm_20 : str | None
        SPM.20 (opt) - Specimen Availability (ID)

    spm_21 : list[CWE] | None
        SPM.21 (opt, rep) - Specimen Reject Reason (CWE)

    spm_22 : CWE | None
        SPM.22 (opt) - Specimen Quality (CWE)

    spm_23 : CWE | None
        SPM.23 (opt) - Specimen Appropriateness (CWE)

    spm_24 : list[CWE] | None
        SPM.24 (opt, rep) - Specimen Condition (CWE)

    spm_25 : CQ | None
        SPM.25 (opt) - Specimen Current Quantity (CQ)

    spm_26 : str | None
        SPM.26 (opt) - Number of Specimen Containers (NM)

    spm_27 : CWE | None
        SPM.27 (opt) - Container Type (CWE)

    spm_28 : CWE | None
        SPM.28 (opt) - Container Condition (CWE)

    spm_29 : CWE | None
        SPM.29 (opt) - Specimen Child Role (CWE)

    spm_30 : list[CX] | None
        SPM.30 (opt, rep) - Accession ID (CX)

    spm_31 : list[CX] | None
        SPM.31 (opt, rep) - Other Specimen ID (CX)

    spm_32 : EI | None
        SPM.32 (opt) - Shipment ID (EI)
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
        description="Item #1754",
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
        description="Item #1755",
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
        description="Item #1756",
    )

    spm_4: CWE = Field(
        validation_alias=AliasChoices(
            "spm_4",
            "specimen_type",
            "SPM.4",
        ),
        serialization_alias="SPM.4",
        title="Specimen Type",
        description="Item #1900 | Table HL70487",
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
        description="Item #1757 | Table HL70541",
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
        description="Item #1758 | Table HL70371",
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
        description="Item #1759 | Table HL70488",
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
        description="Item #1901 | Table HL79999",
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
        description="Item #1760 | Table HL70542",
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
        description="Item #1761 | Table HL70543",
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
        description="Item #1762 | Table HL70369",
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
        description="Item #1902",
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
        description="Item #1763",
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
        description="Item #1764",
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
        description="Item #1908 | Table HL70376",
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
        description="Item #1903 | Table HL70489",
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
        description="Item #1765",
    )

    spm_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_18",
            "specimen_received_date_time",
            "SPM.18",
        ),
        serialization_alias="SPM.18",
        title="Specimen Received Date/Time",
        description="Item #248",
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
        description="Item #1904",
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
        description="Item #1766 | Table HL70136",
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
        description="Item #1767 | Table HL70490",
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
        description="Item #1768 | Table HL70491",
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
        description="Item #1769 | Table HL70492",
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
        description="Item #1770 | Table HL70493",
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
        description="Item #1771",
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
        description="Item #1772",
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
        description="Item #1773 | Table HL79999",
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
        description="Item #1774 | Table HL70544",
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
        description="Item #1775 | Table HL70494",
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
        description="Item #2314",
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
        description="Item #2315",
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
        description="Item #2316",
    )

    @field_validator("spm_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("spm_13", "spm_26", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("spm_18", "spm_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
