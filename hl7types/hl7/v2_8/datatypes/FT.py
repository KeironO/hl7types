"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: FT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class FT(HL7Model):
    """HL7 v2 FT data type."""

    pass

    model_config = {"populate_by_name": True}
