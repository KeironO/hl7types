"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ED
Type: Segment
"""
from __future__ import annotations

from pydantic import ConfigDict
from hl7types.hl7 import HL7Model


class ED(HL7Model):
    """Encapsulated Data (wrong segment) (S7.11.2)."""

    pass

    model_config = ConfigDict(populate_by_name=True)
