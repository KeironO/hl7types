"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MOC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .MO import MO


class MOC(BaseModel):
    """HL7 v2 MOC data type."""

    moc_1: MO | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "moc_1",
            "monetary_amount",
            "MOC.1",
        ),
        serialization_alias="MOC.1",
        title="Monetary Amount",
    )

    moc_2: CWE | None = Field(
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
