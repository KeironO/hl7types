"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SPR
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.QIP import QIP


class SPR(BaseModel):
    """HL7 v2 SPR segment."""

    spr_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spr_1",
            "query_tag",
            "SPR.1",
        ),
        serialization_alias="SPR.1",
        title="Query tag",
        description="Item #696",
    )

    spr_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "spr_2",
            "query_response_format_code",
            "SPR.2",
        ),
        serialization_alias="SPR.2",
        title="Query/ Response Format Code",
        description="Item #697 | Table HL70106",
    )

    spr_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "spr_3",
            "stored_procedure_name",
            "SPR.3",
        ),
        serialization_alias="SPR.3",
        title="Stored procedure name",
        description="Item #704",
    )

    spr_4: list[QIP] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "spr_4",
            "input_parameter_list",
            "SPR.4",
        ),
        serialization_alias="SPR.4",
        title="Input parameter list",
        description="Item #705",
    )

    model_config = {"populate_by_name": True}
