"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: varies
Type: Datatype
"""
from __future__ import annotations

from hl7types.hl7 import HL7Model


class varies(HL7Model):
    """HL7 v2 varies data type."""

    pass

    model_config = {"populate_by_name": True}
