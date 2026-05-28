"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: IAM
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN


class IAM(BaseModel):
    """HL7 v2 IAM segment."""

    iam_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "iam_1",
            "set_id_iam",
            "IAM.1",
        ),
        serialization_alias="IAM.1",
        title="Set ID - IAM",
        description="Item #1612",
    )

    iam_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_2",
            "allergen_type_code",
            "IAM.2",
        ),
        serialization_alias="IAM.2",
        title="Allergen Type Code",
        description="Item #204 | Table HL70127",
    )

    iam_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "iam_3",
            "allergen_code_mnemonic_description",
            "IAM.3",
        ),
        serialization_alias="IAM.3",
        title="Allergen Code/Mnemonic/Description",
        description="Item #205",
    )

    iam_4: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_4",
            "allergy_severity_code",
            "IAM.4",
        ),
        serialization_alias="IAM.4",
        title="Allergy Severity Code",
        description="Item #206 | Table HL70128",
    )

    iam_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_5",
            "allergy_reaction_code",
            "IAM.5",
        ),
        serialization_alias="IAM.5",
        title="Allergy Reaction Code",
        description="Item #207",
    )

    iam_6: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "iam_6",
            "allergy_action_code",
            "IAM.6",
        ),
        serialization_alias="IAM.6",
        title="Allergy Action Code",
        description="Item #1551 | Table HL70206",
    )

    iam_7: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_7",
            "allergy_unique_identifier",
            "IAM.7",
        ),
        serialization_alias="IAM.7",
        title="Allergy Unique Identifier",
        description="Item #1552",
    )

    iam_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_8",
            "action_reason",
            "IAM.8",
        ),
        serialization_alias="IAM.8",
        title="Action Reason",
        description="Item #1553",
    )

    iam_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_9",
            "sensitivity_to_causative_agent_code",
            "IAM.9",
        ),
        serialization_alias="IAM.9",
        title="Sensitivity to Causative Agent Code",
        description="Item #1554 | Table HL70436",
    )

    iam_10: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_10",
            "allergen_group_code_mnemonic_description",
            "IAM.10",
        ),
        serialization_alias="IAM.10",
        title="Allergen Group Code/Mnemonic/Description",
        description="Item #1555",
    )

    iam_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_11",
            "onset_date",
            "IAM.11",
        ),
        serialization_alias="IAM.11",
        title="Onset Date",
        description="Item #1556",
    )

    iam_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_12",
            "onset_date_text",
            "IAM.12",
        ),
        serialization_alias="IAM.12",
        title="Onset Date Text",
        description="Item #1557",
    )

    iam_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_13",
            "reported_date_time",
            "IAM.13",
        ),
        serialization_alias="IAM.13",
        title="Reported Date/Time",
        description="Item #1558",
    )

    iam_14: XPN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_14",
            "reported_by",
            "IAM.14",
        ),
        serialization_alias="IAM.14",
        title="Reported By",
        description="Item #1559",
    )

    iam_15: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_15",
            "relationship_to_patient_code",
            "IAM.15",
        ),
        serialization_alias="IAM.15",
        title="Relationship to Patient Code",
        description="Item #1560 | Table HL70063",
    )

    iam_16: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_16",
            "alert_device_code",
            "IAM.16",
        ),
        serialization_alias="IAM.16",
        title="Alert Device Code",
        description="Item #1561 | Table HL70437",
    )

    iam_17: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_17",
            "allergy_clinical_status_code",
            "IAM.17",
        ),
        serialization_alias="IAM.17",
        title="Allergy Clinical Status Code",
        description="Item #1562 | Table HL70438",
    )

    iam_18: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_18",
            "statused_by_person",
            "IAM.18",
        ),
        serialization_alias="IAM.18",
        title="Statused by Person",
        description="Item #1563",
    )

    iam_19: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_19",
            "statused_by_organization",
            "IAM.19",
        ),
        serialization_alias="IAM.19",
        title="Statused by Organization",
        description="Item #1564",
    )

    iam_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_20",
            "statused_at_date_time",
            "IAM.20",
        ),
        serialization_alias="IAM.20",
        title="Statused at Date/Time",
        description="Item #1565",
    )

    iam_21: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_21",
            "inactivated_by_person",
            "IAM.21",
        ),
        serialization_alias="IAM.21",
        title="Inactivated by Person",
        description="Item #2294",
    )

    iam_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_22",
            "inactivated_date_time",
            "IAM.22",
        ),
        serialization_alias="IAM.22",
        title="Inactivated Date/Time",
        description="Item #2295",
    )

    iam_23: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_23",
            "initially_recorded_by_person",
            "IAM.23",
        ),
        serialization_alias="IAM.23",
        title="Initially Recorded by Person",
        description="Item #2296",
    )

    iam_24: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_24",
            "initially_recorded_date_time",
            "IAM.24",
        ),
        serialization_alias="IAM.24",
        title="Initially Recorded Date/Time",
        description="Item #2297",
    )

    iam_25: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_25",
            "modified_by_person",
            "IAM.25",
        ),
        serialization_alias="IAM.25",
        title="Modified by Person",
        description="Item #2298",
    )

    iam_26: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_26",
            "modified_date_time",
            "IAM.26",
        ),
        serialization_alias="IAM.26",
        title="Modified Date/Time",
        description="Item #2299",
    )

    iam_27: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_27",
            "clinician_identified_code",
            "IAM.27",
        ),
        serialization_alias="IAM.27",
        title="Clinician Identified Code",
        description="Item #2300",
    )

    iam_28: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_28",
            "initially_recorded_by_organization",
            "IAM.28",
        ),
        serialization_alias="IAM.28",
        title="Initially Recorded by Organization",
        description="Item #3293",
    )

    iam_29: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_29",
            "modified_by_organization",
            "IAM.29",
        ),
        serialization_alias="IAM.29",
        title="Modified by Organization",
        description="Item #3294",
    )

    iam_30: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_30",
            "inactivated_by_organization",
            "IAM.30",
        ),
        serialization_alias="IAM.30",
        title="Inactivated by Organization",
        description="Item #3295",
    )

    model_config = {"populate_by_name": True}
