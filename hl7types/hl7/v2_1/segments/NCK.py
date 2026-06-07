"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NCK
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class NCK(HL7Model):
    """HL7 v2 NCK segment.

    Attributes
    ----------
    nck_1 : str
        NCK.1 (req) - SYSTEM DATE/TIME (TS)
    """

    nck_1: str = Field(
        validation_alias=AliasChoices(
            "nck_1",
            "system_date_time",
            "NCK.1",
        ),
        serialization_alias="NCK.1",
        title="SYSTEM DATE/TIME",
        description="Item #742",
    )

    model_config = {"populate_by_name": True}
