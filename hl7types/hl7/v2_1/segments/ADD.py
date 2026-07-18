"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class ADD(HL7Model):
    """ADDENDUM (S2.5.1).

    Attributes
    ----------
    add_1 : str | None
        ADD.1 - ADDENDUM CONTINUATION POINTER (ST) O S2-39
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
        description="O | Item #00641 | LEN:60",
    )

    model_config = ConfigDict(populate_by_name=True)
