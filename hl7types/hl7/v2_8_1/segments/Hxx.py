"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: Hxx
Type: Segment
"""
from __future__ import annotations

from hl7types.hl7 import HL7Model


class Hxx(HL7Model):
    """HL7 v2 Hxx segment."""

    pass

    model_config = {"populate_by_name": True}
