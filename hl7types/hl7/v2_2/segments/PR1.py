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
    """PROCEDURES (S6.4.3).

    Attributes
    ----------
    pr1_1 : str
        PR1.1 - Set ID - procedure (SI) R S6.4.3.1

    pr1_2 : list[str]
        PR1.2 - Procedure coding method (ID) R rep S6.4.3.2 | 0089 - PROCEDURE CODING METHOD

    pr1_3 : list[str]
        PR1.3 - Procedure code (ID) R rep S6.4.3.3 | 0088 - PROCEDURE CODE

    pr1_4 : list[str] | None
        PR1.4 - Procedure description (ST) NA rep S6.4.3.4

    pr1_5 : TS
        PR1.5 - Procedure date / time (TS) R S6.4.3.5

    pr1_6 : str
        PR1.6 - Procedure type (ID) R S6.4.3.6 | 0090 - PROCEDURE TYPE

    pr1_7 : str | None
        PR1.7 - Procedure minutes (NM) NA S6.4.3.7

    pr1_8 : str | None
        PR1.8 - Anesthesiologist (CN) NA S6.4.3.8 | 0010 - PHYSICIAN ID

    pr1_9 : str | None
        PR1.9 - Anesthesia code (ID) NA S6.4.3.9 | 0019 - ANESTHESIA CODE

    pr1_10 : str | None
        PR1.10 - Anesthesia minutes (NM) NA S6.4.3.10

    pr1_11 : str | None
        PR1.11 - Surgeon (CN) NA S6.4.3.11 | 0010 - PHYSICIAN ID

    pr1_12 : list[str] | None
        PR1.12 - Procedure Practitioner (CM) NA rep S6.4.3.12 | 0010 - PHYSICIAN ID

    pr1_13 : str | None
        PR1.13 - Consent code (ID) NA S6.4.3.13 | 0059 - CONSENT CODE

    pr1_14 : str | None
        PR1.14 - Procedure priority (NM) NA S6.4.3.14
    """

    pr1_1: str = Field(
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_procedure",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="Set ID - procedure",
        description="R | Item #00391 | LEN:4",
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
        description=(
            "R | Item #00392 | Table 0089 - PROCEDURE CODING METHOD | LEN:2"
        ),
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
        description="R | Item #00393 | Table 0088 - PROCEDURE CODE | LEN:10",
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
        description="NA | Item #00394 | LEN:40",
    )

    pr1_5: TS = Field(
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="Procedure date / time",
        description="R | Item #00395",
    )

    pr1_6: str = Field(
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="Procedure type",
        description="R | Item #00396 | Table 0090 - PROCEDURE TYPE | LEN:2",
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
        description="NA | Item #00397 | LEN:4",
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
        description="NA | Item #00398 | Table 0010 - PHYSICIAN ID",
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
        description="NA | Item #00399 | Table 0019 - ANESTHESIA CODE | LEN:2",
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
        description="NA | Item #00400 | LEN:4",
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
        description="NA | Item #00401 | Table 0010 - PHYSICIAN ID",
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
        description="NA | Item #00402 | Table 0010 - PHYSICIAN ID",
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
        description="NA | Item #00403 | Table 0059 - CONSENT CODE | LEN:2",
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
        description="NA | Item #00404 | LEN:2",
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
