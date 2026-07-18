"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: Zxx
Type: Segment
"""
from __future__ import annotations

from pydantic import ConfigDict
from hl7types.hl7 import HL7Model


class Zxx(HL7Model):
    """any Z segment."""

    pass

    model_config = ConfigDict(populate_by_name=True)
