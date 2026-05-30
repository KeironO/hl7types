"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SDR_S31.ANTI-MICROBIAL_DEVICE_DATA
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class SDR_S31_ANTI_MICROBIAL_DEVICE_DATA(HL7Model):
    """HL7 v2 SDR_S31.ANTI-MICROBIAL_DEVICE_DATA group."""

    pass

    model_config = {"populate_by_name": True}
