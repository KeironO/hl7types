"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QIP
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class QIP(BaseModel):
    """HL7 v2 QIP data type."""

    qip_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qip_1",
            "segment_field_name",
            "QIP.1",
        ),
        serialization_alias="QIP.1",
        title="Segment Field Name",
    )

    qip_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qip_2",
            "values",
            "QIP.2",
        ),
        serialization_alias="QIP.2",
        title="Values",
    )

    model_config = {"populate_by_name": True}
