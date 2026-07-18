"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: DB1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CX import CX

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class DB1(HL7Model):
    """Disability (S3.4.11).

    Attributes
    ----------
    db1_1 : str
        DB1.1 - Set ID - DB1 (SI) R S3.4.11.1

    db1_2 : str | None
        DB1.2 - Disabled Person Code (IS) O S3.4.11.2 | 0334 - Disabled Person Code

    db1_3 : list[CX] | None
        DB1.3 - Disabled Person Identifier (CX) O rep S3.4.11.3

    db1_4 : str | None
        DB1.4 - Disabled Indicator (ID) O S3.4.11.4 | 0136 - Yes/no indicator

    db1_5 : str | None
        DB1.5 - Disability Start Date (DT) O S3.4.11.5

    db1_6 : str | None
        DB1.6 - Disability End Date (DT) O S3.4.11.6

    db1_7 : str | None
        DB1.7 - Disability Return to Work Date (DT) O S3.4.11.7

    db1_8 : str | None
        DB1.8 - Disability Unable to Work Date (DT) O S3.4.11.8
    """

    db1_1: str = Field(
        validation_alias=AliasChoices(
            "db1_1",
            "set_id_db1",
            "DB1.1",
        ),
        serialization_alias="DB1.1",
        title="Set ID - DB1",
        description="R | Item #01283 | LEN:4",
    )

    db1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_2",
            "disabled_person_code",
            "DB1.2",
        ),
        serialization_alias="DB1.2",
        title="Disabled Person Code",
        description=(
            "O | Item #01284 | Table 0334 - Disabled Person Code | LEN:2"
        ),
    )

    db1_3: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_3",
            "disabled_person_identifier",
            "DB1.3",
        ),
        serialization_alias="DB1.3",
        title="Disabled Person Identifier",
        description="O | Item #01285",
    )

    db1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_4",
            "disabled_indicator",
            "DB1.4",
        ),
        serialization_alias="DB1.4",
        title="Disabled Indicator",
        description="O | Item #01286 | Table 0136 - Yes/no indicator | LEN:1",
    )

    db1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_5",
            "disability_start_date",
            "DB1.5",
        ),
        serialization_alias="DB1.5",
        title="Disability Start Date",
        description="O | Item #01287 | LEN:8",
    )

    db1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_6",
            "disability_end_date",
            "DB1.6",
        ),
        serialization_alias="DB1.6",
        title="Disability End Date",
        description="O | Item #01288 | LEN:8",
    )

    db1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_7",
            "disability_return_to_work_date",
            "DB1.7",
        ),
        serialization_alias="DB1.7",
        title="Disability Return to Work Date",
        description="O | Item #01289 | LEN:8",
    )

    db1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_8",
            "disability_unable_to_work_date",
            "DB1.8",
        ),
        serialization_alias="DB1.8",
        title="Disability Unable to Work Date",
        description="O | Item #01290 | LEN:8",
    )

    @field_validator("db1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("db1_5", "db1_6", "db1_7", "db1_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
