"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: DB1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX


class DB1(BaseModel):
    """HL7 v2 DB1 segment."""

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

    db1_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_2",
            "disabled_person_code",
            "DB1.2",
        ),
        serialization_alias="DB1.2",
        title="Disabled Person Code",
        description="Item #1284 | Table HL70334",
    )

    db1_3: list[CX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_3",
            "disabled_person_identifier",
            "DB1.3",
        ),
        serialization_alias="DB1.3",
        title="Disabled Person Identifier",
        description="Item #1285",
    )

    db1_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_4",
            "disability_indicator",
            "DB1.4",
        ),
        serialization_alias="DB1.4",
        title="Disability Indicator",
        description="Item #1286 | Table HL70136",
    )

    db1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_5",
            "disability_start_date",
            "DB1.5",
        ),
        serialization_alias="DB1.5",
        title="Disability Start Date",
        description="Item #1287",
    )

    db1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_6",
            "disability_end_date",
            "DB1.6",
        ),
        serialization_alias="DB1.6",
        title="Disability End Date",
        description="Item #1288",
    )

    db1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_7",
            "disability_return_to_work_date",
            "DB1.7",
        ),
        serialization_alias="DB1.7",
        title="Disability Return to Work Date",
        description="Item #1289",
    )

    db1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "db1_8",
            "disability_unable_to_work_date",
            "DB1.8",
        ),
        serialization_alias="DB1.8",
        title="Disability Unable to Work Date",
        description="Item #1290",
    )

    model_config = {"populate_by_name": True}
