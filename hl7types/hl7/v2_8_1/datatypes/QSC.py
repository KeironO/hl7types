"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QSC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class QSC(HL7Model):
    """HL7 v2 QSC data type.

    Attributes
    ----------
    qsc_1 : str
        QSC.1 (req) - Segment Field Name (ST)

    qsc_2 : str | None
        QSC.2 (opt) - Relational Operator (ID)

    qsc_3 : str | None
        QSC.3 (opt) - Value (ST)

    qsc_4 : str | None
        QSC.4 (opt) - Relational Conjunction (ID)
    """

    qsc_1: str = Field(
        validation_alias=AliasChoices(
            "qsc_1",
            "segment_field_name",
            "QSC.1",
        ),
        serialization_alias="QSC.1",
        title="Segment Field Name",
    )

    qsc_2: Optional[str] = Field(
        default=None,
        max_length=2,
        validation_alias=AliasChoices(
            "qsc_2",
            "relational_operator",
            "QSC.2",
        ),
        serialization_alias="QSC.2",
        title="Relational Operator",
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
        max_length=3,
        validation_alias=AliasChoices(
            "qsc_4",
            "relational_conjunction",
            "QSC.4",
        ),
        serialization_alias="QSC.4",
        title="Relational Conjunction",
    )

    model_config = {"populate_by_name": True}
