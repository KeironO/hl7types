"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NCK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class NCK(HL7Model):
    """System Clock (SC.2.1.2).

    Attributes
    ----------
    nck_1 : TS | None
        NCK.1 - System Date/Time (TS) NA SC.2.1.1
    """

    nck_1: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nck_1",
            "system_date_time",
            "NCK.1",
        ),
        serialization_alias="NCK.1",
        title="System Date/Time",
        description="NA | Item #01172",
    )

    model_config = {"populate_by_name": True}
