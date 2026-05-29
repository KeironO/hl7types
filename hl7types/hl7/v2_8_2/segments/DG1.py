"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DG1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class DG1(BaseModel):
    """HL7 v2 DG1 segment.

    Attributes
    ----------
    dg1_1 : str
        DG1.1 (req) - Set ID - DG1 (SI)

    dg1_3 : CWE
        DG1.3 (req) - Diagnosis Code - DG1 (CWE)

    dg1_5 : str | None
        DG1.5 (opt) - Diagnosis Date/Time (DTM)

    dg1_6 : CWE
        DG1.6 (req) - Diagnosis Type (CWE)

    dg1_15 : str | None
        DG1.15 (opt) - Diagnosis Priority (NM)

    dg1_16 : list[XCN] | None
        DG1.16 (opt, rep) - Diagnosing Clinician (XCN)

    dg1_17 : CWE | None
        DG1.17 (opt) - Diagnosis Classification (CWE)

    dg1_18 : str | None
        DG1.18 (opt) - Confidential Indicator (ID)

    dg1_19 : str | None
        DG1.19 (opt) - Attestation Date/Time (DTM)

    dg1_20 : EI | None
        DG1.20 (opt) - Diagnosis Identifier (EI)

    dg1_21 : str | None
        DG1.21 (opt) - Diagnosis Action Code (ID)

    dg1_22 : EI | None
        DG1.22 (opt) - Parent Diagnosis (EI)

    dg1_23 : CWE | None
        DG1.23 (opt) - DRG CCL Value Code (CWE)

    dg1_24 : str | None
        DG1.24 (opt) - DRG Grouping Usage (ID)

    dg1_25 : CWE | None
        DG1.25 (opt) - DRG Diagnosis Determination Status (CWE)

    dg1_26 : CWE | None
        DG1.26 (opt) - Present On Admission (POA) Indicator (CWE)
    """

    dg1_1: str = Field(
        default=...,
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
        default=...,
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

    model_config = {"populate_by_name": True}
