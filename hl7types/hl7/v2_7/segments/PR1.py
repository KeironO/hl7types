"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PR1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL


class PR1(HL7Model):
    """HL7 v2 PR1 segment.

    Attributes
    ----------
    pr1_1 : str
        PR1.1 (req) - Set ID - PR1 (SI)

    pr1_3 : CNE
        PR1.3 (req) - Procedure Code (CNE)

    pr1_5 : str
        PR1.5 (req) - Procedure Date/Time (DTM)

    pr1_6 : CWE | None
        PR1.6 (opt) - Procedure Functional Type (CWE)

    pr1_7 : str | None
        PR1.7 (opt) - Procedure Minutes (NM)

    pr1_9 : CWE | None
        PR1.9 (opt) - Anesthesia Code (CWE)

    pr1_10 : str | None
        PR1.10 (opt) - Anesthesia Minutes (NM)

    pr1_13 : CWE | None
        PR1.13 (opt) - Consent Code (CWE)

    pr1_14 : str | None
        PR1.14 (opt) - Procedure Priority (NM)

    pr1_15 : CWE | None
        PR1.15 (opt) - Associated Diagnosis Code (CWE)

    pr1_16 : list[CNE] | None
        PR1.16 (opt, rep) - Procedure Code Modifier (CNE)

    pr1_17 : CWE | None
        PR1.17 (opt) - Procedure DRG Type (CWE)

    pr1_18 : list[CWE] | None
        PR1.18 (opt, rep) - Tissue Type Code (CWE)

    pr1_19 : EI | None
        PR1.19 (opt) - Procedure Identifier (EI)

    pr1_20 : str | None
        PR1.20 (opt) - Procedure Action Code (ID)

    pr1_21 : CWE | None
        PR1.21 (opt) - DRG Procedure Determination Status (CWE)

    pr1_22 : CWE | None
        PR1.22 (opt) - DRG Procedure Relevance (CWE)

    pr1_23 : list[PL] | None
        PR1.23 (opt, rep) - Treating Organizational Unit (PL)

    pr1_24 : str | None
        PR1.24 (opt) - Respiratory Within Surgery (ID)

    pr1_25 : EI | None
        PR1.25 (opt) - Parent Procedure ID (EI)
    """

    pr1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_pr1",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="Set ID - PR1",
        description="Item #391",
    )

    pr1_3: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_3",
            "procedure_code",
            "PR1.3",
        ),
        serialization_alias="PR1.3",
        title="Procedure Code",
        description="Item #393 | Table HL70088",
    )

    pr1_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="Procedure Date/Time",
        description="Item #395",
    )

    pr1_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_functional_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="Procedure Functional Type",
        description="Item #396 | Table HL70230",
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
        description="Item #397",
    )

    pr1_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_9",
            "anesthesia_code",
            "PR1.9",
        ),
        serialization_alias="PR1.9",
        title="Anesthesia Code",
        description="Item #399 | Table HL70019",
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
        description="Item #400",
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
        description="Item #403 | Table HL70059",
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
        description="Item #404 | Table HL70418",
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
        description="Item #772 | Table HL70051",
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
        description="Item #1316 | Table HL70340",
    )

    pr1_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_17",
            "procedure_drg_type",
            "PR1.17",
        ),
        serialization_alias="PR1.17",
        title="Procedure DRG Type",
        description="Item #1501 | Table HL70416",
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
        description="Item #1502 | Table HL70417",
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
        description="Item #1848",
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
        description="Item #1849 | Table HL70206",
    )

    pr1_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_21",
            "drg_procedure_determination_status",
            "PR1.21",
        ),
        serialization_alias="PR1.21",
        title="DRG Procedure Determination Status",
        description="Item #2177 | Table HL70761",
    )

    pr1_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_22",
            "drg_procedure_relevance",
            "PR1.22",
        ),
        serialization_alias="PR1.22",
        title="DRG Procedure Relevance",
        description="Item #2178 | Table HL70763",
    )

    pr1_23: Optional[List[PL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_23",
            "treating_organizational_unit",
            "PR1.23",
        ),
        serialization_alias="PR1.23",
        title="Treating Organizational Unit",
        description="Item #2371",
    )

    pr1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_24",
            "respiratory_within_surgery",
            "PR1.24",
        ),
        serialization_alias="PR1.24",
        title="Respiratory Within Surgery",
        description="Item #2372 | Table HL70136",
    )

    pr1_25: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_25",
            "parent_procedure_id",
            "PR1.25",
        ),
        serialization_alias="PR1.25",
        title="Parent Procedure ID",
        description="Item #2373",
    )

    model_config = {"populate_by_name": True}
