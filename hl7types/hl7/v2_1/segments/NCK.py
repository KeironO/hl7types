"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NCK
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class NCK(HL7Model):
    """SYSTEM CLOCK.

    Attributes
    ----------
    nck_1 : str
        NCK.1 - SYSTEM DATE/TIME (TS) R
    """

    nck_1: str = Field(
        validation_alias=AliasChoices(
            "nck_1",
            "system_date_time",
            "NCK.1",
        ),
        serialization_alias="NCK.1",
        title="SYSTEM DATE/TIME",
        description="R | Item #00742 | LEN:19",
    )

    model_config = ConfigDict(populate_by_name=True)
