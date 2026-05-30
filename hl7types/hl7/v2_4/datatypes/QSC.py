"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    qsc_1 : str | None
        QSC.1 (opt) - segment field name (ST)

    qsc_2 : str | None
        QSC.2 (opt) - relational operator (ID)

    qsc_3 : str | None
        QSC.3 (opt) - Value (ST)

    qsc_4 : str | None
        QSC.4 (opt) - relational conjunction (ID)
    """

    qsc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qsc_1",
            "segment_field_name",
            "QSC.1",
        ),
        serialization_alias="QSC.1",
        title="segment field name",
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
