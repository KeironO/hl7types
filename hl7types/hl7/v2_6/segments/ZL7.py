"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ZL7
Type: Segment
"""
from __future__ import annotations

from pydantic import ConfigDict
from hl7types.hl7 import HL7Model


class ZL7(HL7Model):
    """(proposed example only) (S8.6.1)."""

    pass

    model_config = ConfigDict(populate_by_name=True)
