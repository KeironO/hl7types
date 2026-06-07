"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: TX
Type: Datatype
"""
from __future__ import annotations

from hl7types.hl7 import HL7Model


class TX(HL7Model):
    """HL7 v2 TX data type."""

    pass

    model_config = {"populate_by_name": True}
