"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAN_U09.NOTIFICATION
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NDS import NDS
from ..segments.NTE import NTE

_NDS = NDS
_NTE = NTE


class EAN_U09_NOTIFICATION(HL7Model):
    """HL7 v2 EAN_U09.NOTIFICATION group.

    Attributes:
        NDS (NDS): Notification Detail, required
        NTE (Optional[NTE]): Notes and Comments, optional
    """

    NDS: _NDS = Field(
        title="NDS",
        description="Notification Detail",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
