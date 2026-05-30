"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MOC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .MO import MO


class MOC(HL7Model):
    """HL7 v2 MOC data type.

    Attributes
    ----------
    moc_1 : MO | None
        MOC.1 (opt) - Monetary Amount (MO)

    moc_2 : CE | None
        MOC.2 (opt) - Charge Code (CE)
    """

    moc_1: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "moc_1",
            "monetary_amount",
            "MOC.1",
        ),
        serialization_alias="MOC.1",
        title="Monetary Amount",
    )

    moc_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "moc_2",
            "charge_code",
            "MOC.2",
        ),
        serialization_alias="MOC.2",
        title="Charge Code",
    )

    model_config = {"populate_by_name": True}
