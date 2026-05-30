"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MOP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class MOP(HL7Model):
    """HL7 v2 MOP data type.

    Attributes
    ----------
    mop_1 : str | None
        MOP.1 (opt) - money or percentage indicator (IS)

    mop_2 : str | None
        MOP.2 (opt) - money or percentage quantity (NM)
    """

    mop_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mop_1",
            "money_or_percentage_indicator",
            "MOP.1",
        ),
        serialization_alias="MOP.1",
        title="money or percentage indicator",
    )

    mop_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mop_2",
            "money_or_percentage_quantity",
            "MOP.2",
        ),
        serialization_alias="MOP.2",
        title="money or percentage quantity",
    )

    model_config = {"populate_by_name": True}
