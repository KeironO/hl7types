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
    """CONTINUATION POINTER (S5.3.1).

    Attributes
    ----------
    dsc_1 : str | None
        DSC.1 - CONTINUATION POINTER (ST) O
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
        description="O | Item #00167 | LEN:60",
    )

    model_config = {"populate_by_name": True}
