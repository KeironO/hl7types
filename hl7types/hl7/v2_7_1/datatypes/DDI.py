"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: DDI
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .MO import MO

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class DDI(HL7Model):
    """Daily deductible information (S2.A.15).

    Attributes
    ----------
    ddi_1 : str | None
        DDI.1 (opt) - Delay Days (NM)

    ddi_2 : MO
        DDI.2 (req) - Monetary Amount (MO)

    ddi_3 : str | None
        DDI.3 (opt) - Number of Days (NM)
    """

    ddi_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_1",
            "delay_days",
            "DDI.1",
        ),
        serialization_alias="DDI.1",
        title="Delay Days",
    )

    ddi_2: MO = Field(
        validation_alias=AliasChoices(
            "ddi_2",
            "monetary_amount",
            "DDI.2",
        ),
        serialization_alias="DDI.2",
        title="Monetary Amount",
    )

    ddi_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_3",
            "number_of_days",
            "DDI.3",
        ),
        serialization_alias="DDI.3",
        title="Number of Days",
    )

    @field_validator("ddi_1", "ddi_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
