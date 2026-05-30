"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PR1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class PR1(HL7Model):
    """HL7 v2 PR1 segment.

    Attributes
    ----------
    pr1_1 : str
        PR1.1 (req) - Set ID - PR1 (SI)

    pr1_2 : str | None
        PR1.2 (opt) - Procedure Coding Method (IS)

    pr1_3 : CE
        PR1.3 (req) - Procedure Code (CE)

    pr1_4 : str | None
        PR1.4 (opt) - Procedure Description (ST)

    pr1_5 : TS
        PR1.5 (req) - Procedure Date/Time (TS)

    pr1_6 : str | None
        PR1.6 (opt) - Procedure Functional Type (IS)

    pr1_7 : str | None
        PR1.7 (opt) - Procedure Minutes (NM)

    pr1_8 : list[XCN] | None
        PR1.8 (opt, rep) - Anesthesiologist (XCN)

    pr1_9 : str | None
        PR1.9 (opt) - Anesthesia Code (IS)

    pr1_10 : str | None
        PR1.10 (opt) - Anesthesia Minutes (NM)

    pr1_11 : list[XCN] | None
        PR1.11 (opt, rep) - Surgeon (XCN)

    pr1_12 : list[XCN] | None
        PR1.12 (opt, rep) - Procedure Practitioner (XCN)

    pr1_13 : CE | None
        PR1.13 (opt) - Consent Code (CE)

    pr1_14 : str | None
        PR1.14 (opt) - Procedure Priority (ID)

    pr1_15 : CE | None
        PR1.15 (opt) - Associated Diagnosis Code (CE)

    pr1_16 : list[CE] | None
        PR1.16 (opt, rep) - Procedure Code Modifier (CE)

    pr1_17 : str | None
        PR1.17 (opt) - Procedure DRG Type (IS)

    pr1_18 : list[CE] | None
        PR1.18 (opt, rep) - Tissue Type Code (CE)
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

    pr1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_2",
            "procedure_coding_method",
            "PR1.2",
        ),
        serialization_alias="PR1.2",
        title="Procedure Coding Method",
        description="Item #392 | Table HL70089",
    )

    pr1_3: CE = Field(
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

    pr1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_4",
            "procedure_description",
            "PR1.4",
        ),
        serialization_alias="PR1.4",
        title="Procedure Description",
        description="Item #394",
    )

    pr1_5: TS = Field(
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

    pr1_6: Optional[str] = Field(
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

    pr1_8: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_8",
            "anesthesiologist",
            "PR1.8",
        ),
        serialization_alias="PR1.8",
        title="Anesthesiologist",
        description="Item #398 | Table HL70010",
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

    pr1_11: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_11",
            "surgeon",
            "PR1.11",
        ),
        serialization_alias="PR1.11",
        title="Surgeon",
        description="Item #401 | Table HL70010",
    )

    pr1_12: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_12",
            "procedure_practitioner",
            "PR1.12",
        ),
        serialization_alias="PR1.12",
        title="Procedure Practitioner",
        description="Item #402 | Table HL70010",
    )

    pr1_13: Optional[CE] = Field(
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

    pr1_15: Optional[CE] = Field(
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

    pr1_16: Optional[List[CE]] = Field(
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

    pr1_17: Optional[str] = Field(
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

    pr1_18: Optional[List[CE]] = Field(
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

    model_config = {"populate_by_name": True}
