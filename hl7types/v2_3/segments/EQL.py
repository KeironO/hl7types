"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: EQL
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class EQL(BaseModel):
    """HL7 v2 EQL segment."""

    eql_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eql_1",
            "query_tag",
            "EQL.1",
        ),
        serialization_alias="EQL.1",
        title="Query tag",
        description="Item #696",
    )

    eql_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "eql_2",
            "query_response_format_code",
            "EQL.2",
        ),
        serialization_alias="EQL.2",
        title="Query/ Response Format Code",
        description="Item #697 | Table HL70106",
    )

    eql_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "eql_3",
            "eql_query_name",
            "EQL.3",
        ),
        serialization_alias="EQL.3",
        title="EQL Query Name",
        description="Item #709",
    )

    eql_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "eql_4",
            "eql_query_statement",
            "EQL.4",
        ),
        serialization_alias="EQL.4",
        title="EQL Query Statement",
        description="Item #710",
    )

    model_config = {"populate_by_name": True}
