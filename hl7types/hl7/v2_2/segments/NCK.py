"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NCK
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class NCK(HL7Model):
    """System Clock.

    Attributes
    ----------
    nck_1 : TS
        NCK.1 - System Date/Time (TS) R SC-3
    """

    nck_1: TS = Field(
        validation_alias=AliasChoices(
            "nck_1",
            "system_date_time",
            "NCK.1",
        ),
        serialization_alias="NCK.1",
        title="System Date/Time",
        description="R | Item #00742",
    )

    model_config = {"populate_by_name": True}
