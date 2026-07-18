"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class ERR(HL7Model):
    """ERROR (S2.5.4).

    Attributes
    ----------
    err_1 : list[str]
        ERR.1 - ERROR CODE AND LOCATION (ID) R rep S2-42 | 0060 - ERROR CODE
    """

    err_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "err_1",
            "error_code_and_location",
            "ERR.1",
        ),
        serialization_alias="ERR.1",
        title="ERROR CODE AND LOCATION",
        description="R | Item #00080 | Table 0060 - ERROR CODE | LEN:80",
    )

    model_config = ConfigDict(populate_by_name=True)
