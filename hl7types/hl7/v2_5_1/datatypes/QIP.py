"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class QIP(HL7Model):
    """HL7 v2 QIP data type.

    Attributes
    ----------
    qip_1 : str | None
        QIP.1 (opt) - Segment Field Name (ST)

    qip_2 : str | None
        QIP.2 (opt) - Values (ST)
    """

    qip_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qip_1",
            "segment_field_name",
            "QIP.1",
        ),
        serialization_alias="QIP.1",
        title="Segment Field Name",
    )

    qip_2: Optional[str] = Field(
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
