"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: PR1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PR1(HL7Model):
    """PROCEDURES (S6.3.7).

    Attributes
    ----------
    pr1_1 : list[str]
        PR1.1 - SET ID - PROCEDURE (SI) R rep S6-15

    pr1_2 : str
        PR1.2 - PROCEDURE CODING METHOD. (ID) R | 0089 - PROCEDURE CODING METHOD

    pr1_3 : str
        PR1.3 - PROCEDURE CODE (ID) R | 0088 - PROCEDURE CODE

    pr1_4 : str | None
        PR1.4 - PROCEDURE DESCRIPTION (ST) O

    pr1_5 : str
        PR1.5 - PROCEDURE DATE/TIME (TS) R

    pr1_6 : str
        PR1.6 - PROCEDURE TYPE (ID) R | 0090 - PROCEDURE TYPE

    pr1_7 : str | None
        PR1.7 - PROCEDURE MINUTES (NM) O

    pr1_8 : str | None
        PR1.8 - ANESTHESIOLOGIST (CN) O | 0010 - PHYSICIAN ID

    pr1_9 : str | None
        PR1.9 - ANESTHESIA CODE (ID) O | 0019 - ANESTHESIA CODE

    pr1_10 : str | None
        PR1.10 - ANESTHESIA MINUTES (NM) O

    pr1_11 : str | None
        PR1.11 - SURGEON (CN) O | 0010 - PHYSICIAN ID

    pr1_12 : str | None
        PR1.12 - RESIDENT CODE (CN) O | 0010 - PHYSICIAN ID

    pr1_13 : str | None
        PR1.13 - CONSENT CODE (ID) O | 0059 - CONSENT CODE
    """

    pr1_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_procedure",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="SET ID - PROCEDURE",
        description="R | Item #00304 | LEN:4",
    )

    pr1_2: str = Field(
        validation_alias=AliasChoices(
            "pr1_2",
            "procedure_coding_method",
            "PR1.2",
        ),
        serialization_alias="PR1.2",
        title="PROCEDURE CODING METHOD.",
        description=(
            "R | Item #00393 | Table 0089 - PROCEDURE CODING METHOD | LEN:2"
        ),
    )

    pr1_3: str = Field(
        validation_alias=AliasChoices(
            "pr1_3",
            "procedure_code",
            "PR1.3",
        ),
        serialization_alias="PR1.3",
        title="PROCEDURE CODE",
        description="R | Item #00305 | Table 0088 - PROCEDURE CODE | LEN:10",
    )

    pr1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_4",
            "procedure_description",
            "PR1.4",
        ),
        serialization_alias="PR1.4",
        title="PROCEDURE DESCRIPTION",
        description="O | Item #00306 | LEN:40",
    )

    pr1_5: str = Field(
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="PROCEDURE DATE/TIME",
        description="R | Item #00307 | LEN:19",
    )

    pr1_6: str = Field(
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="PROCEDURE TYPE",
        description="R | Item #00309 | Table 0090 - PROCEDURE TYPE | LEN:2",
    )

    pr1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_7",
            "procedure_minutes",
            "PR1.7",
        ),
        serialization_alias="PR1.7",
        title="PROCEDURE MINUTES",
        description="O | Item #00310 | LEN:4",
    )

    pr1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_8",
            "anesthesiologist",
            "PR1.8",
        ),
        serialization_alias="PR1.8",
        title="ANESTHESIOLOGIST",
        description="O | Item #00311 | Table 0010 - PHYSICIAN ID | LEN:60",
    )

    pr1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_9",
            "anesthesia_code",
            "PR1.9",
        ),
        serialization_alias="PR1.9",
        title="ANESTHESIA CODE",
        description="O | Item #00313 | Table 0019 - ANESTHESIA CODE | LEN:2",
    )

    pr1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_10",
            "anesthesia_minutes",
            "PR1.10",
        ),
        serialization_alias="PR1.10",
        title="ANESTHESIA MINUTES",
        description="O | Item #00314 | LEN:4",
    )

    pr1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_11",
            "surgeon",
            "PR1.11",
        ),
        serialization_alias="PR1.11",
        title="SURGEON",
        description="O | Item #00315 | Table 0010 - PHYSICIAN ID | LEN:60",
    )

    pr1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_12",
            "resident_code",
            "PR1.12",
        ),
        serialization_alias="PR1.12",
        title="RESIDENT CODE",
        description="O | Item #00318 | Table 0010 - PHYSICIAN ID | LEN:60",
    )

    pr1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_13",
            "consent_code",
            "PR1.13",
        ),
        serialization_alias="PR1.13",
        title="CONSENT CODE",
        description="O | Item #00317 | Table 0059 - CONSENT CODE | LEN:2",
    )

    @field_validator("pr1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pr1_7", "pr1_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
