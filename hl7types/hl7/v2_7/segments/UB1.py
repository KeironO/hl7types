"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: UB1
Type: Segment
"""
from __future__ import annotations

from pydantic import ConfigDict
from hl7types.hl7 import HL7Model


class UB1(HL7Model):
    """UB82 (S6.5.10)."""

    pass

    model_config = ConfigDict(populate_by_name=True)
