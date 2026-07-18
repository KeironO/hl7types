"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RCD
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RCD(HL7Model):
    """Row column definition (S2.8.32).

    Attributes
    ----------
    rcd_1 : str | None
        RCD.1 (opt) - HL7 item number (ST)

    rcd_2 : str | None
        RCD.2 (opt) - HL7 date type (ST)

    rcd_3 : str | None
        RCD.3 (opt) - maximum column width (NM)
    """

    rcd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_1",
            "hl7_item_number",
            "RCD.1",
        ),
        serialization_alias="RCD.1",
        title="HL7 item number",
    )

    rcd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_2",
            "hl7_date_type",
            "RCD.2",
        ),
        serialization_alias="RCD.2",
        title="HL7 date type",
    )

    rcd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_3",
            "maximum_column_width",
            "RCD.3",
        ),
        serialization_alias="RCD.3",
        title="maximum column width",
    )

    @field_validator("rcd_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
