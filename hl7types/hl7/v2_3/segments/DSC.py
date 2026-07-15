"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: DSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class DSC(HL7Model):
    """Continuation pointer segment (S2.24.8).

    Attributes
    ----------
    dsc_1 : str | None
        DSC.1 - Continuation Pointer (ST) O S2.24.1
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
        description="O | Item #00014 | LEN:180",
    )

    model_config = {"populate_by_name": True}
