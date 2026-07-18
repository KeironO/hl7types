"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class ERR(HL7Model):
    """ERROR (S2.10.3).

    Attributes
    ----------
    err_1 : list[str]
        ERR.1 - Error Code and Location (CM) R rep S2.10.3.1 | 0060 - ERROR CODE
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
        description="R | Item #00024 | Table 0060 - ERROR CODE",
    )

    model_config = ConfigDict(populate_by_name=True)
