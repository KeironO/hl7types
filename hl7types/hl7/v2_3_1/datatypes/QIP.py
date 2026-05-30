"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        QIP.1 (opt) - field name (ST)

    qip_2 : str | None
        QIP.2 (opt) - value1&value2&value3 (ST)
    """

    qip_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qip_1",
            "field_name",
            "QIP.1",
        ),
        serialization_alias="QIP.1",
        title="field name",
    )

    qip_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qip_2",
            "value1_value2_value3",
            "QIP.2",
        ),
        serialization_alias="QIP.2",
        title="value1&value2&value3",
    )

    model_config = {"populate_by_name": True}
