"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: VND
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.EI import EI


class VND(HL7Model):
    """Purchasing Vendor (S17.4.4).

    Attributes
    ----------
    vnd_1 : str
        VND.1 (req) - Set Id - VND (SI) S17.4.4.1

    vnd_2 : EI
        VND.2 (req) - Vendor Identifier (EI) S17.4.4.2

    vnd_3 : str | None
        VND.3 (opt) - Vendor Name (ST) S17.4.4.3

    vnd_4 : EI | None
        VND.4 (opt) - Vendor Catalog Number (EI) S17.4.4.4

    vnd_5 : CNE | None
        VND.5 (opt) - Primary Vendor Indicator (CNE) S17.4.4.5 | 0532 - Expanded yes/no indicator
    """

    vnd_1: str = Field(
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
        validation_alias=AliasChoices(
            "vnd_2",
            "vendor_identifier",
            "VND.2",
        ),
        serialization_alias="VND.2",
        title="Vendor Identifier",
        description="Item #2218",
    )

    vnd_3: Optional[str] = Field(
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

    vnd_4: Optional[EI] = Field(
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

    vnd_5: Optional[CNE] = Field(
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

    @field_validator("vnd_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
