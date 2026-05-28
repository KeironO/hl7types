"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ODT
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class ODT(BaseModel):
    """HL7 v2 ODT segment."""

    odt_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "odt_1",
            "tray_type",
            "ODT.1",
        ),
        serialization_alias="ODT.1",
        title="Tray Type",
        description="Item #273 | Table HL70160",
    )

    odt_2: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "odt_2",
            "service_period",
            "ODT.2",
        ),
        serialization_alias="ODT.2",
        title="Service Period",
        description="Item #270",
    )

    odt_3: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "odt_3",
            "text_instruction",
            "ODT.3",
        ),
        serialization_alias="ODT.3",
        title="Text Instruction",
        description="Item #272",
    )

    model_config = {"populate_by_name": True}
