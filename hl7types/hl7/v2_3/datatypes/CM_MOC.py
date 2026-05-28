"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_MOC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .MO import MO


class CM_MOC(BaseModel):
    """HL7 v2 CM_MOC data type."""

    cm_moc_1: MO | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_moc_1",
            "dollar_amount",
            "CM_MOC.1",
        ),
        serialization_alias="CM_MOC.1",
        title="dollar amount",
    )

    cm_moc_2: CE | None = Field(
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
