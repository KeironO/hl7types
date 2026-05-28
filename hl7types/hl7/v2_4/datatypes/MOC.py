"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MOC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .MO import MO


class MOC(BaseModel):
    """HL7 v2 MOC data type."""

    moc_1: MO | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "moc_1",
            "dollar_amount",
            "MOC.1",
        ),
        serialization_alias="MOC.1",
        title="dollar amount",
    )

    moc_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "moc_2",
            "charge_code",
            "MOC.2",
        ),
        serialization_alias="MOC.2",
        title="charge code",
    )

    model_config = {"populate_by_name": True}
