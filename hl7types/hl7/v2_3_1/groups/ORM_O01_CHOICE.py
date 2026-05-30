"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORM_O01.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class ORM_O01_CHOICE(HL7Model):
    """HL7 v2 ORM_O01.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
