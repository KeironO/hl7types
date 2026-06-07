"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QIP
Type: Datatype
"""
from __future__ import annotations

from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class QIP(HL7Model):
    """HL7 v2 QIP data type.

    Attributes
    ----------
    qip_1 : str
        QIP.1 (req) - Segment Field Name (ST)

    qip_2 : str
        QIP.2 (req) - Values (ST)
    """

    qip_1: str = Field(
        max_length=12,
        validation_alias=AliasChoices(
            "qip_1",
            "segment_field_name",
            "QIP.1",
        ),
        serialization_alias="QIP.1",
        title="Segment Field Name",
    )

    qip_2: str = Field(
        validation_alias=AliasChoices(
            "qip_2",
            "values",
            "QIP.2",
        ),
        serialization_alias="QIP.2",
        title="Values",
    )

    model_config = {"populate_by_name": True}
