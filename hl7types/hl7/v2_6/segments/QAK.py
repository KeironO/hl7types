"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QAK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


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

    qak_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_3",
            "message_query_name",
            "QAK.3",
        ),
        serialization_alias="QAK.3",
        title="Message Query Name",
        description="Item #1375 | Table HL70471",
    )

    qak_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_4",
            "hit_count_total",
            "QAK.4",
        ),
        serialization_alias="QAK.4",
        title="Hit Count Total",
        description="Item #1434",
    )

    qak_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_5",
            "this_payload",
            "QAK.5",
        ),
        serialization_alias="QAK.5",
        title="This payload",
        description="Item #1622",
    )

    qak_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_6",
            "hits_remaining",
            "QAK.6",
        ),
        serialization_alias="QAK.6",
        title="Hits remaining",
        description="Item #1623",
    )

    model_config = {"populate_by_name": True}
