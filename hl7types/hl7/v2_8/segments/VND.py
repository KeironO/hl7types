"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: VND
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.EI import EI

_RE_SI = re.compile(r'\d*')


class VND(HL7Model):
    """Purchasing Vendor (S17.4.4).

    Attributes
    ----------
    vnd_1 : str
        VND.1 - Set Id - VND (SI) R S17.4.4.1

    vnd_2 : EI
        VND.2 - Vendor Identifier (EI) R S17.4.4.2

    vnd_3 : str | None
        VND.3 - Vendor Name (ST) O S17.4.4.3

    vnd_4 : EI | None
        VND.4 - Vendor Catalog Number (EI) O S17.4.4.4

    vnd_5 : CNE | None
        VND.5 - Primary Vendor Indicator (CNE) O S17.4.4.5 | 0532 - Expanded Yes/no Indicator
    """

    vnd_1: str = Field(
        validation_alias=AliasChoices(
            "vnd_1",
            "set_id_vnd",
            "VND.1",
        ),
        serialization_alias="VND.1",
        title="Set Id - VND",
        description="R | Item #02217 | LEN:4",
    )

    vnd_2: EI = Field(
        validation_alias=AliasChoices(
            "vnd_2",
            "vendor_identifier",
            "VND.2",
        ),
        serialization_alias="VND.2",
        title="Vendor Identifier",
        description="R | Item #02218",
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
        description="O | Item #02276",
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
        description="O | Item #02219",
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
        description="O | Item #02220 | Table 0532 - Expanded Yes/no Indicator",
    )

    @field_validator("vnd_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
