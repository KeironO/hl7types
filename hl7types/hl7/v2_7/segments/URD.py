"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: URD
Type: Segment
"""
from __future__ import annotations

from hl7types.hl7 import HL7Model


class URD(HL7Model):
    """HL7 v2 URD segment."""

    pass

    model_config = {"populate_by_name": True}
