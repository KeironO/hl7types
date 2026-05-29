"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
        ADD.1 (opt) - Addendum Continuation Pointer (ST)
    """

    add_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "add_1",
            "addendum_continuation_pointer",
            "ADD.1",
        ),
        serialization_alias="ADD.1",
        title="Addendum Continuation Pointer",
        description="Item #66",
    )

    model_config = {"populate_by_name": True}
