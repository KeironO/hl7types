"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PSG
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.EI import EI

_RE_SI = re.compile(r'\d*')


class PSG(HL7Model):
    """Product/Service Group (S16.4.5).

    Attributes
    ----------
    psg_1 : EI
        PSG.1 - Provider Product/Service Group Number (EI) R S16.4.5.1

    psg_2 : EI | None
        PSG.2 - Payer Product/Service Group Number (EI) O S16.4.5.2

    psg_3 : str
        PSG.3 - Product/Service Group Sequence Number (SI) R S16.4.5.3

    psg_4 : str
        PSG.4 - Adjudicate as Group (ID) R S16.4.5.4 | 0136 - Yes/no Indicator

    psg_5 : CP
        PSG.5 - Product/Service Group Billed Amount (CP) R S16.4.5.5

    psg_6 : str
        PSG.6 - Product/Service Group Description (ST) R S16.4.5.6
    """

    psg_1: EI = Field(
        validation_alias=AliasChoices(
            "psg_1",
            "provider_product_service_group_number",
            "PSG.1",
        ),
        serialization_alias="PSG.1",
        title="Provider Product/Service Group Number",
        description="R | Item #01950",
    )

    psg_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psg_2",
            "payer_product_service_group_number",
            "PSG.2",
        ),
        serialization_alias="PSG.2",
        title="Payer Product/Service Group Number",
        description="O | Item #01951",
    )

    psg_3: str = Field(
        validation_alias=AliasChoices(
            "psg_3",
            "product_service_group_sequence_number",
            "PSG.3",
        ),
        serialization_alias="PSG.3",
        title="Product/Service Group Sequence Number",
        description="R | Item #01952 | LEN:4",
    )

    psg_4: str = Field(
        validation_alias=AliasChoices(
            "psg_4",
            "adjudicate_as_group",
            "PSG.4",
        ),
        serialization_alias="PSG.4",
        title="Adjudicate as Group",
        description="R | Item #01953 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    psg_5: CP = Field(
        validation_alias=AliasChoices(
            "psg_5",
            "product_service_group_billed_amount",
            "PSG.5",
        ),
        serialization_alias="PSG.5",
        title="Product/Service Group Billed Amount",
        description="R | Item #01954",
    )

    psg_6: str = Field(
        validation_alias=AliasChoices(
            "psg_6",
            "product_service_group_description",
            "PSG.6",
        ),
        serialization_alias="PSG.6",
        title="Product/Service Group Description",
        description="R | Item #02044",
    )

    @field_validator("psg_3", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
