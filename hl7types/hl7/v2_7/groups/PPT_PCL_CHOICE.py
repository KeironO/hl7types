"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PPT_PCL.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class PPT_PCL_CHOICE(HL7Model):
    """HL7 v2 PPT_PCL.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
