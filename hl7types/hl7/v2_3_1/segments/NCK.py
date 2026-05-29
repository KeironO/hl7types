"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NCK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


class NCK(BaseModel):
    """HL7 v2 NCK segment.

    Attributes
    ----------
    nck_1 : TS | None
        NCK.1 (opt) - System Date/Time (TS)
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
        description="Item #1172",
    )

    model_config = {"populate_by_name": True}
