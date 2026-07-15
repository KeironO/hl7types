"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.ELD import ELD


class ERR(HL7Model):
    """Error (S2.16.5).

    Attributes
    ----------
    err_1 : list[ELD]
        ERR.1 - Error Code and Location (ELD) R rep S2.16.5.1
    """

    err_1: List[ELD] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "err_1",
            "error_code_and_location",
            "ERR.1",
        ),
        serialization_alias="ERR.1",
        title="Error Code and Location",
        description="R | Item #00024",
    )

    model_config = {"populate_by_name": True}
