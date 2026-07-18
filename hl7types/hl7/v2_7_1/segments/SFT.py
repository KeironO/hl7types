"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SFT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.XON import XON

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class SFT(HL7Model):
    """Software Segment (S2.14.12).

    Attributes
    ----------
    sft_1 : XON
        SFT.1 - Software Vendor Organization (XON) R S2.14.12.1

    sft_2 : str
        SFT.2 - Software Certified Version or Release Number (ST) R S2.14.12.2

    sft_3 : str
        SFT.3 - Software Product Name (ST) R S2.14.12.3

    sft_4 : str
        SFT.4 - Software Binary ID (ST) R S2.14.12.4

    sft_5 : str | None
        SFT.5 - Software Product Information (TX) O S2.14.12.5

    sft_6 : str | None
        SFT.6 - Software Install Date (DTM) O S2.14.12.6
    """

    sft_1: XON = Field(
        validation_alias=AliasChoices(
            "sft_1",
            "software_vendor_organization",
            "SFT.1",
        ),
        serialization_alias="SFT.1",
        title="Software Vendor Organization",
        description="R | Item #01834",
    )

    sft_2: str = Field(
        validation_alias=AliasChoices(
            "sft_2",
            "software_certified_version_or_release_number",
            "SFT.2",
        ),
        serialization_alias="SFT.2",
        title="Software Certified Version or Release Number",
        description="R | Item #01835",
    )

    sft_3: str = Field(
        validation_alias=AliasChoices(
            "sft_3",
            "software_product_name",
            "SFT.3",
        ),
        serialization_alias="SFT.3",
        title="Software Product Name",
        description="R | Item #01836",
    )

    sft_4: str = Field(
        validation_alias=AliasChoices(
            "sft_4",
            "software_binary_id",
            "SFT.4",
        ),
        serialization_alias="SFT.4",
        title="Software Binary ID",
        description="R | Item #01837",
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
        description="O | Item #01838",
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
        description="O | Item #01839",
    )

    @field_validator("sft_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
