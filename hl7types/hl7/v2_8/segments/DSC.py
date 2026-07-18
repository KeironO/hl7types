"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class DSC(HL7Model):
    """Continuation Pointer (S2.14.4).

    Attributes
    ----------
    dsc_1 : str | None
        DSC.1 - Continuation Pointer (ST) O S2.14.4.1

    dsc_2 : str | None
        DSC.2 - Continuation Style (ID) O S2.14.4.2 | 0398 - Continuation Style Code
    """

    dsc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsc_1",
            "continuation_pointer",
            "DSC.1",
        ),
        serialization_alias="DSC.1",
        title="Continuation Pointer",
        description="O | Item #00014",
    )

    dsc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsc_2",
            "continuation_style",
            "DSC.2",
        ),
        serialization_alias="DSC.2",
        title="Continuation Style",
        description=(
            "O | Item #01354 | Table 0398 - Continuation Style Code | LEN:1"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
