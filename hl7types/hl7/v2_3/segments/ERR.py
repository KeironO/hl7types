"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class ERR(HL7Model):
    """HL7 v2 ERR segment.

    Attributes
    ----------
    err_1 : list[str]
        ERR.1 (req, rep) - Error Code and Location (CM)
    """

    err_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "err_1",
            "error_code_and_location",
            "ERR.1",
        ),
        serialization_alias="ERR.1",
        title="Error Code and Location",
        description="Item #24 | Table HL70060",
    )

    model_config = {"populate_by_name": True}
