"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DDI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .MO import MO


class DDI(HL7Model):
    """HL7 v2 DDI data type.

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
        default=...,
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

    model_config = {"populate_by_name": True}
