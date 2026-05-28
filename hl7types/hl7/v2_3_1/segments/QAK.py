"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: QAK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class QAK(BaseModel):
    """HL7 v2 QAK segment."""

    qak_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_1",
            "query_tag",
            "QAK.1",
        ),
        serialization_alias="QAK.1",
        title="Query Tag",
        description="Item #696",
    )

    qak_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_2",
            "query_response_status",
            "QAK.2",
        ),
        serialization_alias="QAK.2",
        title="Query Response Status",
        description="Item #708 | Table HL70208",
    )

    model_config = {"populate_by_name": True}
