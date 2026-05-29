"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class DSC(BaseModel):
    """HL7 v2 DSC segment.

    Attributes
    ----------
    dsc_1 : str | None
        DSC.1 (opt) - Continuation Pointer (ST)
    """

    dsc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsc_1",
            "continuation_pointer",
            "DSC.1",
        ),
        serialization_alias="DSC.1",
        title="Continuation Pointer",
        description="Item #60",
    )

    model_config = {"populate_by_name": True}
