"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PGL_PC6.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class PGL_PC6_CHOICE(HL7Model):
    """HL7 v2 PGL_PC6.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
