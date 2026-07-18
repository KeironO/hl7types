"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: URS
Type: Segment
"""
from __future__ import annotations

from pydantic import ConfigDict
from hl7types.hl7 import HL7Model


class URS(HL7Model):
    """deprecated."""

    pass

    model_config = ConfigDict(populate_by_name=True)
