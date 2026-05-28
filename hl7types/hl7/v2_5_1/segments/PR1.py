"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PR1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class PR1(BaseModel):
    """HL7 v2 PR1 segment."""

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

    pr1_2: str | None = Field(
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

    pr1_4: str | None = Field(
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

    pr1_6: str | None = Field(
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

    pr1_7: str | None = Field(
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

    pr1_8: list[XCN] | None = Field(
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

    pr1_9: str | None = Field(
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

    pr1_10: str | None = Field(
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

    pr1_11: list[XCN] | None = Field(
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

    pr1_12: list[XCN] | None = Field(
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

    pr1_13: CE | None = Field(
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

    pr1_14: str | None = Field(
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

    pr1_15: CE | None = Field(
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

    pr1_16: list[CE] | None = Field(
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

    pr1_17: str | None = Field(
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

    pr1_18: list[CE] | None = Field(
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

    pr1_19: EI | None = Field(
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

    pr1_20: str | None = Field(
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

    model_config = {"populate_by_name": True}
