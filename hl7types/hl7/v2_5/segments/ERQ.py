"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ERQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.QIP import QIP


class ERQ(BaseModel):
    """HL7 v2 ERQ segment."""

    erq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erq_1",
            "query_tag",
            "ERQ.1",
        ),
        serialization_alias="ERQ.1",
        title="Query Tag",
        description="Item #696",
    )

    erq_2: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "erq_2",
            "event_identifier",
            "ERQ.2",
        ),
        serialization_alias="ERQ.2",
        title="Event Identifier",
        description="Item #706",
    )

    erq_3: Optional[List[QIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erq_3",
            "input_parameter_list",
            "ERQ.3",
        ),
        serialization_alias="ERQ.3",
        title="Input Parameter List",
        description="Item #705",
    )

    model_config = {"populate_by_name": True}
