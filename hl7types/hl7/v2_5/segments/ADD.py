"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class ADD(HL7Model):
    """Addendum (S2.15.1).

    Attributes
    ----------
    add_1 : str | None
        ADD.1 - Addendum Continuation Pointer (ST) O S2.15.1.1
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
        description="O | Item #00066 | LEN:65536",
    )

    model_config = {"populate_by_name": True}
