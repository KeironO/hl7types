"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class DSC(HL7Model):
    """CONTINUATION POINTER (S2.10.8).

    Attributes
    ----------
    dsc_1 : str | None
        DSC.1 - Continuation Pointer (ST) NA S2.10.8.1
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
        description="NA | Item #00060 | LEN:180",
    )

    model_config = ConfigDict(populate_by_name=True)
