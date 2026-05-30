"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class DSC(HL7Model):
    """HL7 v2 DSC segment.

    Attributes
    ----------
    dsc_1 : str | None
        DSC.1 (opt) - CONTINUATION POINTER (ST)
    """

    dsc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsc_1",
            "continuation_pointer",
            "DSC.1",
        ),
        serialization_alias="DSC.1",
        title="CONTINUATION POINTER",
        description="Item #167",
    )

    model_config = {"populate_by_name": True}
