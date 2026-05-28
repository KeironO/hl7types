"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QID
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class QID(BaseModel):
    """HL7 v2 QID segment."""

    qid_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qid_1",
            "query_tag",
            "QID.1",
        ),
        serialization_alias="QID.1",
        title="Query Tag",
        description="Item #696",
    )

    qid_2: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "qid_2",
            "message_query_name",
            "QID.2",
        ),
        serialization_alias="QID.2",
        title="Message Query Name",
        description="Item #1375 | Table HL70471",
    )

    model_config = {"populate_by_name": True}
