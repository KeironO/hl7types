"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QSC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class QSC(BaseModel):
    """HL7 v2 QSC data type."""

    qsc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_1",
            "name_of_field",
            "QSC.1",
        ),
        serialization_alias="QSC.1",
        title="name of field",
    )

    qsc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_2",
            "relational_operator",
            "QSC.2",
        ),
        serialization_alias="QSC.2",
        title="relational operator",
    )

    qsc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_3",
            "value",
            "QSC.3",
        ),
        serialization_alias="QSC.3",
        title="Value",
    )

    qsc_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_4",
            "relational_conjunction",
            "QSC.4",
        ),
        serialization_alias="QSC.4",
        title="relational conjunction",
    )

    model_config = {"populate_by_name": True}
