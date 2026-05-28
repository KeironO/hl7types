"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: BLG
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CK import CK


class BLG(BaseModel):
    """HL7 v2 BLG segment."""

    blg_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_1",
            "when_to_charge",
            "BLG.1",
        ),
        serialization_alias="BLG.1",
        title="When to Charge",
        description="Item #234 | Table HL70100",
    )

    blg_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_2",
            "charge_type",
            "BLG.2",
        ),
        serialization_alias="BLG.2",
        title="Charge Type",
        description="Item #235 | Table HL70122",
    )

    blg_3: CK | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_3",
            "account_id",
            "BLG.3",
        ),
        serialization_alias="BLG.3",
        title="Account ID",
        description="Item #236",
    )

    model_config = {"populate_by_name": True}
