"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SPM
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.EIP import EIP
from ..datatypes.TS import TS


class SPM(BaseModel):
    """HL7 v2 SPM segment."""

    spm_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_1",
            "set_id_spm",
            "SPM.1",
        ),
        serialization_alias="SPM.1",
        title="Set ID _ SPM",
        description="Item #1754",
    )

    spm_2: EIP | None = Field(
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

    spm_3: list[EIP] | None = Field(
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
        default=...,
        validation_alias=AliasChoices(
            "spm_4",
            "specimen_type",
            "SPM.4",
        ),
        serialization_alias="SPM.4",
        title="Specimen Type",
        description="Item #1900 | Table HL70487",
    )

    spm_5: list[CWE] | None = Field(
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

    spm_6: list[CWE] | None = Field(
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

    spm_7: CWE | None = Field(
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

    spm_8: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_8",
            "specimen_source_site",
            "SPM.8",
        ),
        serialization_alias="SPM.8",
        title="Specimen Source Site",
        description="Item #1901",
    )

    spm_9: list[CWE] | None = Field(
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

    spm_10: CWE | None = Field(
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

    spm_11: list[CWE] | None = Field(
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

    spm_12: CQ | None = Field(
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

    spm_13: str | None = Field(
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

    spm_14: list[str] | None = Field(
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

    spm_15: list[CWE] | None = Field(
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

    spm_16: list[CWE] | None = Field(
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

    spm_17: DR | None = Field(
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

    spm_18: TS | None = Field(
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

    spm_19: TS | None = Field(
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

    spm_20: str | None = Field(
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

    spm_21: list[CWE] | None = Field(
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

    spm_22: CWE | None = Field(
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

    spm_23: CWE | None = Field(
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

    spm_24: list[CWE] | None = Field(
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

    spm_25: CQ | None = Field(
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

    spm_26: str | None = Field(
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

    spm_27: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spm_27",
            "container_type",
            "SPM.27",
        ),
        serialization_alias="SPM.27",
        title="Container Type",
        description="Item #1773",
    )

    spm_28: CWE | None = Field(
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

    spm_29: CWE | None = Field(
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

    model_config = {"populate_by_name": True}
