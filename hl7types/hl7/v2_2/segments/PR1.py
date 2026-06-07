"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PR1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class PR1(HL7Model):
    """HL7 v2 PR1 segment.

    Attributes
    ----------
    pr1_1 : str
        PR1.1 (req) - Set ID - procedure (SI)

    pr1_2 : list[str]
        PR1.2 (req, rep) - Procedure coding method (ID)

    pr1_3 : list[str]
        PR1.3 (req, rep) - Procedure code (ID)

    pr1_4 : list[str] | None
        PR1.4 (opt, rep) - Procedure description (ST)

    pr1_5 : TS
        PR1.5 (req) - Procedure date / time (TS)

    pr1_6 : str
        PR1.6 (req) - Procedure type (ID)

    pr1_7 : str | None
        PR1.7 (opt) - Procedure minutes (NM)

    pr1_8 : str | None
        PR1.8 (opt) - Anesthesiologist (CN)

    pr1_9 : str | None
        PR1.9 (opt) - Anesthesia code (ID)

    pr1_10 : str | None
        PR1.10 (opt) - Anesthesia minutes (NM)

    pr1_11 : str | None
        PR1.11 (opt) - Surgeon (CN)

    pr1_12 : list[str] | None
        PR1.12 (opt, rep) - Procedure Practitioner (CM)

    pr1_13 : str | None
        PR1.13 (opt) - Consent code (ID)

    pr1_14 : str | None
        PR1.14 (opt) - Procedure priority (NM)
    """

    pr1_1: str = Field(
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_procedure",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="Set ID - procedure",
        description="Item #391",
    )

    pr1_2: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pr1_2",
            "procedure_coding_method",
            "PR1.2",
        ),
        serialization_alias="PR1.2",
        title="Procedure coding method",
        description="Item #392 | Table HL70089",
    )

    pr1_3: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pr1_3",
            "procedure_code",
            "PR1.3",
        ),
        serialization_alias="PR1.3",
        title="Procedure code",
        description="Item #393 | Table HL70088",
    )

    pr1_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_4",
            "procedure_description",
            "PR1.4",
        ),
        serialization_alias="PR1.4",
        title="Procedure description",
        description="Item #394",
    )

    pr1_5: TS = Field(
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="Procedure date / time",
        description="Item #395",
    )

    pr1_6: str = Field(
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="Procedure type",
        description="Item #396 | Table HL70090",
    )

    pr1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_7",
            "procedure_minutes",
            "PR1.7",
        ),
        serialization_alias="PR1.7",
        title="Procedure minutes",
        description="Item #397",
    )

    pr1_8: Optional[str] = Field(
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
        title="Anesthesia code",
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
        title="Anesthesia minutes",
        description="Item #400",
    )

    pr1_11: Optional[str] = Field(
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

    pr1_12: Optional[List[str]] = Field(
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

    pr1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_13",
            "consent_code",
            "PR1.13",
        ),
        serialization_alias="PR1.13",
        title="Consent code",
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
        title="Procedure priority",
        description="Item #404",
    )

    @field_validator("pr1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pr1_7", "pr1_10", "pr1_14", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
