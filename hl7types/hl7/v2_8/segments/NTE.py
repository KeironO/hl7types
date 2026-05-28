"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: NTE
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.FT import FT
from ..datatypes.XCN import XCN


class NTE(BaseModel):
    """HL7 v2 NTE segment."""

    nte_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_nte",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="Set ID - NTE",
        description="Item #96",
    )

    nte_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_2",
            "source_of_comment",
            "NTE.2",
        ),
        serialization_alias="NTE.2",
        title="Source of Comment",
        description="Item #97 | Table HL70105",
    )

    nte_3: list[FT] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="Comment",
        description="Item #98",
    )

    nte_4: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_4",
            "comment_type",
            "NTE.4",
        ),
        serialization_alias="NTE.4",
        title="Comment Type",
        description="Item #1318 | Table HL70364",
    )

    nte_5: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_5",
            "entered_by",
            "NTE.5",
        ),
        serialization_alias="NTE.5",
        title="Entered By",
        description="Item #224",
    )

    nte_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_6",
            "entered_date_time",
            "NTE.6",
        ),
        serialization_alias="NTE.6",
        title="Entered Date/Time",
        description="Item #661",
    )

    nte_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_7",
            "effective_start_date",
            "NTE.7",
        ),
        serialization_alias="NTE.7",
        title="Effective Start Date",
        description="Item #1004",
    )

    nte_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_8",
            "expiration_date",
            "NTE.8",
        ),
        serialization_alias="NTE.8",
        title="Expiration Date",
        description="Item #2185",
    )

    model_config = {"populate_by_name": True}
