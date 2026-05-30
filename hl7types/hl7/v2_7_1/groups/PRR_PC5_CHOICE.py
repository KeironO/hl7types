"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PRR_PC5.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class PRR_PC5_CHOICE(HL7Model):
    """HL7 v2 PRR_PC5.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
