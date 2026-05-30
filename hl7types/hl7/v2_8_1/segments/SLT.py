"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SLT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.EI import EI


class SLT(HL7Model):
    """HL7 v2 SLT segment.

    Attributes
    ----------
    slt_1 : EI | None
        SLT.1 (opt) - Device Number (EI)

    slt_2 : str | None
        SLT.2 (opt) - Device Name (ST)

    slt_3 : EI | None
        SLT.3 (opt) - Lot Number (EI)

    slt_4 : EI | None
        SLT.4 (opt) - Item Identifier (EI)

    slt_5 : str | None
        SLT.5 (opt) - Bar Code (ST)
    """

    slt_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "slt_1",
            "device_number",
            "SLT.1",
        ),
        serialization_alias="SLT.1",
        title="Device Number",
        description="Item #2094",
    )

    slt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "slt_2",
            "device_name",
            "SLT.2",
        ),
        serialization_alias="SLT.2",
        title="Device Name",
        description="Item #2280",
    )

    slt_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "slt_3",
            "lot_number",
            "SLT.3",
        ),
        serialization_alias="SLT.3",
        title="Lot Number",
        description="Item #2095",
    )

    slt_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "slt_4",
            "item_identifier",
            "SLT.4",
        ),
        serialization_alias="SLT.4",
        title="Item Identifier",
        description="Item #2096",
    )

    slt_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "slt_5",
            "bar_code",
            "SLT.5",
        ),
        serialization_alias="SLT.5",
        title="Bar Code",
        description="Item #2097",
    )

    model_config = {"populate_by_name": True}
