"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_MOC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .MO import MO


class CM_MOC(HL7Model):
    """HL7 v2 CM_MOC data type.

    Attributes
    ----------
    cm_moc_1 : MO | None
        CM_MOC.1 (opt) - dollar amount (MO)

    cm_moc_2 : CE | None
        CM_MOC.2 (opt) - charge code (CE)
    """

    cm_moc_1: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_moc_1",
            "dollar_amount",
            "CM_MOC.1",
        ),
        serialization_alias="CM_MOC.1",
        title="dollar amount",
    )

    cm_moc_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_moc_2",
            "charge_code",
            "CM_MOC.2",
        ),
        serialization_alias="CM_MOC.2",
        title="charge code",
    )

    model_config = {"populate_by_name": True}
