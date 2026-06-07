"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: IAM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN


class IAM(HL7Model):
    """HL7 v2 IAM segment.

    Attributes
    ----------
    iam_1 : str
        IAM.1 (req) - Set ID - IAM (SI)

    iam_2 : CWE | None
        IAM.2 (opt) - Allergen Type Code (CWE)

    iam_3 : CWE
        IAM.3 (req) - Allergen Code/Mnemonic/Description (CWE)

    iam_4 : CWE | None
        IAM.4 (opt) - Allergy Severity Code (CWE)

    iam_5 : list[str] | None
        IAM.5 (opt, rep) - Allergy Reaction Code (ST)

    iam_6 : CNE
        IAM.6 (req) - Allergy Action Code (CNE)

    iam_7 : EI | None
        IAM.7 (opt) - Allergy Unique Identifier (EI)

    iam_8 : str | None
        IAM.8 (opt) - Action Reason (ST)

    iam_9 : CWE | None
        IAM.9 (opt) - Sensitivity to Causative Agent Code (CWE)

    iam_10 : CWE | None
        IAM.10 (opt) - Allergen Group Code/Mnemonic/Description (CWE)

    iam_11 : str | None
        IAM.11 (opt) - Onset Date (DT)

    iam_12 : str | None
        IAM.12 (opt) - Onset Date Text (ST)

    iam_13 : str | None
        IAM.13 (opt) - Reported Date/Time (DTM)

    iam_14 : XPN | None
        IAM.14 (opt) - Reported By (XPN)

    iam_15 : CWE | None
        IAM.15 (opt) - Relationship to Patient Code (CWE)

    iam_16 : CWE | None
        IAM.16 (opt) - Alert Device Code (CWE)

    iam_17 : CWE | None
        IAM.17 (opt) - Allergy Clinical Status Code (CWE)

    iam_18 : XCN | None
        IAM.18 (opt) - Statused by Person (XCN)

    iam_19 : XON | None
        IAM.19 (opt) - Statused by Organization (XON)

    iam_20 : str | None
        IAM.20 (opt) - Statused at Date/Time (DTM)
    """

    iam_1: str = Field(
        validation_alias=AliasChoices(
            "iam_1",
            "set_id_iam",
            "IAM.1",
        ),
        serialization_alias="IAM.1",
        title="Set ID - IAM",
        description="Item #1612",
    )

    iam_2: Optional[CWE] = Field(
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
        validation_alias=AliasChoices(
            "iam_3",
            "allergen_code_mnemonic_description",
            "IAM.3",
        ),
        serialization_alias="IAM.3",
        title="Allergen Code/Mnemonic/Description",
        description="Item #205",
    )

    iam_4: Optional[CWE] = Field(
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

    iam_5: Optional[List[str]] = Field(
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
        validation_alias=AliasChoices(
            "iam_6",
            "allergy_action_code",
            "IAM.6",
        ),
        serialization_alias="IAM.6",
        title="Allergy Action Code",
        description="Item #1551 | Table HL70206",
    )

    iam_7: Optional[EI] = Field(
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

    iam_8: Optional[str] = Field(
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

    iam_9: Optional[CWE] = Field(
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

    iam_10: Optional[CWE] = Field(
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

    iam_11: Optional[str] = Field(
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

    iam_12: Optional[str] = Field(
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

    iam_13: Optional[str] = Field(
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

    iam_14: Optional[XPN] = Field(
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

    iam_15: Optional[CWE] = Field(
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

    iam_16: Optional[CWE] = Field(
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

    iam_17: Optional[CWE] = Field(
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

    iam_18: Optional[XCN] = Field(
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

    iam_19: Optional[XON] = Field(
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

    iam_20: Optional[str] = Field(
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

    @field_validator("iam_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("iam_11", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("iam_13", "iam_20", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
