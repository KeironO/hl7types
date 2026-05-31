"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class PT(HL7Model):
    """HL7 v2 PT data type.

    Attributes
    ----------
    pt_1 : str | None
        PT.1 (opt) - Processing ID (ID)

    pt_2 : str | None
        PT.2 (opt) - Processing Mode (ID)
    """

    pt_1: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "pt_1",
            "processing_id",
            "PT.1",
        ),
        serialization_alias="PT.1",
        title="Processing ID",
    )

    pt_2: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "pt_2",
            "processing_mode",
            "PT.2",
        ),
        serialization_alias="PT.2",
        title="Processing Mode",
    )

    model_config = {"populate_by_name": True}
