"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class ADD(BaseModel):
    """HL7 v2 ADD segment.

    Attributes
    ----------
    add_1 : str | None
        ADD.1 (opt) - ADDENDUM CONTINUATION POINTER (ST)
    """

    add_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "add_1",
            "addendum_continuation_pointer",
            "ADD.1",
        ),
        serialization_alias="ADD.1",
        title="ADDENDUM CONTINUATION POINTER",
        description="Item #641",
    )

    model_config = {"populate_by_name": True}
