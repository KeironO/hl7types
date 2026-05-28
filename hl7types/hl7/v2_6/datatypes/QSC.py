"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QSC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class QSC(BaseModel):
    """HL7 v2 QSC data type."""

    qsc_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qsc_1",
            "segment_field_name",
            "QSC.1",
        ),
        serialization_alias="QSC.1",
        title="Segment Field Name",
    )

    qsc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_2",
            "relational_operator",
            "QSC.2",
        ),
        serialization_alias="QSC.2",
        title="Relational Operator",
    )

    qsc_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_3",
            "value",
            "QSC.3",
        ),
        serialization_alias="QSC.3",
        title="Value",
    )

    qsc_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_4",
            "relational_conjunction",
            "QSC.4",
        ),
        serialization_alias="QSC.4",
        title="Relational Conjunction",
    )

    model_config = {"populate_by_name": True}
