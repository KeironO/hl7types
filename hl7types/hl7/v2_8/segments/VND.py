"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: VND
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.EI import EI


class VND(BaseModel):
    """HL7 v2 VND segment."""

    vnd_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "vnd_1",
            "set_id_vnd",
            "VND.1",
        ),
        serialization_alias="VND.1",
        title="Set Id - VND",
        description="Item #2217",
    )

    vnd_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "vnd_2",
            "vendor_identifier",
            "VND.2",
        ),
        serialization_alias="VND.2",
        title="Vendor Identifier",
        description="Item #2218",
    )

    vnd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vnd_3",
            "vendor_name",
            "VND.3",
        ),
        serialization_alias="VND.3",
        title="Vendor Name",
        description="Item #2276",
    )

    vnd_4: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vnd_4",
            "vendor_catalog_number",
            "VND.4",
        ),
        serialization_alias="VND.4",
        title="Vendor Catalog Number",
        description="Item #2219",
    )

    vnd_5: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vnd_5",
            "primary_vendor_indicator",
            "VND.5",
        ),
        serialization_alias="VND.5",
        title="Primary Vendor Indicator",
        description="Item #2220 | Table HL70532",
    )

    model_config = {"populate_by_name": True}
