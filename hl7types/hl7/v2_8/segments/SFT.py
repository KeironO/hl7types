"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SFT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.XON import XON


class SFT(HL7Model):
    """HL7 v2 SFT segment.

    Attributes
    ----------
    sft_1 : XON
        SFT.1 (req) - Software Vendor Organization (XON)

    sft_2 : str
        SFT.2 (req) - Software Certified Version or Release Number (ST)

    sft_3 : str
        SFT.3 (req) - Software Product Name (ST)

    sft_4 : str
        SFT.4 (req) - Software Binary ID (ST)

    sft_5 : str | None
        SFT.5 (opt) - Software Product Information (TX)

    sft_6 : str | None
        SFT.6 (opt) - Software Install Date (DTM)
    """

    sft_1: XON = Field(
        validation_alias=AliasChoices(
            "sft_1",
            "software_vendor_organization",
            "SFT.1",
        ),
        serialization_alias="SFT.1",
        title="Software Vendor Organization",
        description="Item #1834",
    )

    sft_2: str = Field(
        validation_alias=AliasChoices(
            "sft_2",
            "software_certified_version_or_release_number",
            "SFT.2",
        ),
        serialization_alias="SFT.2",
        title="Software Certified Version or Release Number",
        description="Item #1835",
    )

    sft_3: str = Field(
        validation_alias=AliasChoices(
            "sft_3",
            "software_product_name",
            "SFT.3",
        ),
        serialization_alias="SFT.3",
        title="Software Product Name",
        description="Item #1836",
    )

    sft_4: str = Field(
        validation_alias=AliasChoices(
            "sft_4",
            "software_binary_id",
            "SFT.4",
        ),
        serialization_alias="SFT.4",
        title="Software Binary ID",
        description="Item #1837",
    )

    sft_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sft_5",
            "software_product_information",
            "SFT.5",
        ),
        serialization_alias="SFT.5",
        title="Software Product Information",
        description="Item #1838",
    )

    sft_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sft_6",
            "software_install_date",
            "SFT.6",
        ),
        serialization_alias="SFT.6",
        title="Software Install Date",
        description="Item #1839",
    )

    @field_validator("sft_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
