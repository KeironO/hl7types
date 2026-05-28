"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SID
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class SID(BaseModel):
    """HL7 v2 SID segment."""

    sid_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_1",
            "application_method_identifier",
            "SID.1",
        ),
        serialization_alias="SID.1",
        title="Application / Method Identifier",
        description="Item #1426",
    )

    sid_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_2",
            "substance_lot_number",
            "SID.2",
        ),
        serialization_alias="SID.2",
        title="Substance Lot Number",
        description="Item #1129",
    )

    sid_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_3",
            "substance_container_identifier",
            "SID.3",
        ),
        serialization_alias="SID.3",
        title="Substance Container Identifier",
        description="Item #1428",
    )

    sid_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_4",
            "substance_manufacturer_identifier",
            "SID.4",
        ),
        serialization_alias="SID.4",
        title="Substance Manufacturer Identifier",
        description="Item #1429 | Table HL70385",
    )

    model_config = {"populate_by_name": True}
