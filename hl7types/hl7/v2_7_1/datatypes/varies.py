"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: varies
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class varies(HL7Model):
    """HL7 v2 varies data type."""

    pass

    model_config = {"populate_by_name": True}
