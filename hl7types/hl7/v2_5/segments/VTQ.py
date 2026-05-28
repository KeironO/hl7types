"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: VTQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.QSC import QSC


class VTQ(BaseModel):
    """HL7 v2 VTQ segment."""

    vtq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vtq_1",
            "query_tag",
            "VTQ.1",
        ),
        serialization_alias="VTQ.1",
        title="Query Tag",
        description="Item #696",
    )

    vtq_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "vtq_2",
            "query_response_format_code",
            "VTQ.2",
        ),
        serialization_alias="VTQ.2",
        title="Query/Response Format Code",
        description="Item #697 | Table HL70106",
    )

    vtq_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "vtq_3",
            "vt_query_name",
            "VTQ.3",
        ),
        serialization_alias="VTQ.3",
        title="VT Query Name",
        description="Item #698",
    )

    vtq_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "vtq_4",
            "virtual_table_name",
            "VTQ.4",
        ),
        serialization_alias="VTQ.4",
        title="Virtual Table Name",
        description="Item #699",
    )

    vtq_5: Optional[List[QSC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vtq_5",
            "selection_criteria",
            "VTQ.5",
        ),
        serialization_alias="VTQ.5",
        title="Selection Criteria",
        description="Item #700",
    )

    model_config = {"populate_by_name": True}
