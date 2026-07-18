"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: QRY_A19
Type: Message
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QRD import QRD

_MSH = MSH
_QRD = QRD


class QRY_A19(HL7Model):
    """HL7 v2 QRY_A19 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        QRD (QRD): QUERY DEFINITION, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="QUERY DEFINITION",
    )

    model_config = ConfigDict(populate_by_name=True)
