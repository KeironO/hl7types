"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: DB1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CX import CX


class DB1(HL7Model):
    """HL7 v2 DB1 segment.

    Attributes
    ----------
    db1_1 : str
        DB1.1 (req) - Set ID - DB1 (SI)

    db1_2 : str | None
        DB1.2 (opt) - Disabled person code (IS)

    db1_3 : list[CX] | None
        DB1.3 (opt, rep) - Disabled person identifier (CX)

    db1_4 : str | None
        DB1.4 (opt) - Disabled Indicator (ID)

    db1_5 : str | None
        DB1.5 (opt) - Disability start date (DT)

    db1_6 : str | None
        DB1.6 (opt) - Disability end date (DT)

    db1_7 : str | None
        DB1.7 (opt) - Disability return to work date (DT)

    db1_8 : str | None
        DB1.8 (opt) - Disability unable to work date (DT)
    """

    db1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "db1_1",
            "set_id_db1",
            "DB1.1",
        ),
        serialization_alias="DB1.1",
        title="Set ID - DB1",
        description="Item #1283",
    )

    db1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_2",
            "disabled_person_code",
            "DB1.2",
        ),
        serialization_alias="DB1.2",
        title="Disabled person code",
        description="Item #1284 | Table HL70033",
    )

    db1_3: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_3",
            "disabled_person_identifier",
            "DB1.3",
        ),
        serialization_alias="DB1.3",
        title="Disabled person identifier",
        description="Item #1285",
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
        description="Item #1286 | Table HL70136",
    )

    db1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_5",
            "disability_start_date",
            "DB1.5",
        ),
        serialization_alias="DB1.5",
        title="Disability start date",
        description="Item #1287",
    )

    db1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_6",
            "disability_end_date",
            "DB1.6",
        ),
        serialization_alias="DB1.6",
        title="Disability end date",
        description="Item #1288",
    )

    db1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_7",
            "disability_return_to_work_date",
            "DB1.7",
        ),
        serialization_alias="DB1.7",
        title="Disability return to work date",
        description="Item #1289",
    )

    db1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_8",
            "disability_unable_to_work_date",
            "DB1.8",
        ),
        serialization_alias="DB1.8",
        title="Disability unable to work date",
        description="Item #1290",
    )

    @field_validator("db1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("db1_5", "db1_6", "db1_7", "db1_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
